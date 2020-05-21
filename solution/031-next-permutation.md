## 31. Next Permutation


- 难度： 中等
- 通过率： 29.7%
- 题目链接：[https://leetcode.com/problems/next-permutation](https://leetcode.com/problems/next-permutation)

## 题目描述

<p>实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。</p>

<p>如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。</p>

<p>必须<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>修改，只允许使用额外常数空间。</p>

<p>以下是一些例子，输入位于左侧列，其相应输出位于右侧列。<br>
<code>1,2,3</code> &rarr; <code>1,3,2</code><br>
<code>3,2,1</code> &rarr; <code>1,2,3</code><br>
<code>1,1,5</code> &rarr; <code>1,5,1</code></p>


## 解法：

下一个排列，即比当前排列大的最小排列，为了得到这样的排列，需要把当前排列尾部的某个数和前面较小的数交换，这样整个数就变大了。但是为了改变后的值尽可能小，需要要让后面的元素呈升序排列，这样才能构成最小的后缀。


下面以 `5 4 8 7 6` 举例子，要想让这个数变大，因为 `876` 已经是最大的后缀了，因此需要用一个数来替换 `4` 的位置，让前缀 `54` 变得更大一些，这里显然应该选择 `876` 中最小的数，即 `6`。

```
5 4 8 7 6
  ^
5 6 4 7 8
  ^
```

把 6 放到 4 的位置后，需要让后缀最小，也就是 `{8,7,4}` 这三个数构成的数最小，即 `478`，这样就得到了答案，`5 6 4 7 8`


这个 4 的寻找方法，就是从后向前，找第一个满足 `nums[i] < nums[i+1]` 的这个 `nums[i]`，也就是第一个比后一个元素小的元素。只有替换这个元素，原数组构成的数才会增大。

找到这个数之后，在去它后面的数中，寻找第一个大于它的数 `nums[j]`，把这个数和 `nums[i]` 交互，而后对 i 后面的所有元素排序，让这些元素呈升序排列，这就得到了答案。

但是值得注意的是，在交换之前 `nums[i]` 之后的元素是递减的，交换之后，依然没有打破递减的规律，所以不需要进行排序，只需要翻转一下即可。 


```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size() < 2) return;
        int i = nums.size() - 2;
        while(i >= 0 && nums[i] >= nums[i+1]){
            i--;
        }
        if(i < 0){
            reverse(nums.begin(), numss.end());
            return;
        }
        int j = nums.size() - 1;
        while(j >= 0 && nums[j] <= nums[i]){
            j--;
        }
        ::swap(nums[i], nums[j]);
        reverse(nums.begin()+i+1, nums.end());
    }
};
```