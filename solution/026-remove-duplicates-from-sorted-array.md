## 26. Remove Duplicates from Sorted Array

- 难度： 简单
- 通过率： 38.9%
- 题目链接：[https://leetcode.com/problems/remove-duplicates-from-sorted-array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个排序数组，你需要在<strong><a href="http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。</p>

<p>不要使用额外的数组空间，你必须在<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a>修改输入数组</strong>并在使用 O(1) 额外空间的条件下完成。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>给定数组 <em>nums</em> = <strong>[1,1,2]</strong>, 

函数应该返回新的长度 <strong>2</strong>, 并且原数组 <em>nums </em>的前两个元素被修改为 <strong><code>1</code></strong>, <strong><code>2</code></strong>。 

你不需要考虑数组中超出新长度后面的元素。</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>给定<em> nums </em>= <strong>[0,0,1,1,1,2,2,3,3,4]</strong>,

函数应该返回新的长度 <strong>5</strong>, 并且原数组 <em>nums </em>的前五个元素被修改为 <strong><code>0</code></strong>, <strong><code>1</code></strong>, <strong><code>2</code></strong>, <strong><code>3</code></strong>, <strong><code>4</code></strong>。

你不需要考虑数组中超出新长度后面的元素。
</pre>

<p><strong>说明:</strong></p>

<p>为什么返回数值是整数，但输出的答案是数组呢?</p>

<p>请注意，输入数组是以<strong>&ldquo;引用&rdquo;</strong>方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。</p>

<p>你可以想象内部操作如下:</p>

<pre>// <strong>nums</strong> 是以&ldquo;引用&rdquo;方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中<strong>该长度范围内</strong>的所有元素。
for (int i = 0; i &lt; len; i++) {
&nbsp; &nbsp; print(nums[i]);
}
</pre>


## 解法 1

使用一个下标 i 指向数组第一个元素，然后从第二个元素开始和 nums[i] 比较，如果发现不同，那么就要把这个元素放到 i+1 的位置上。

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.empty()) return 0;
        int i = 0;
        for(int j=1;j<nums.size();j++){
            if(nums[j] != nums[i]){
                i++;
                nums[i] = nums[j];
            }
        }
        return i+1;
    }
};
```

## 解法 2：

在[这里](https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11782/Share-my-clean-C%2B%2B-code)看到如下解法，稍作改进如下：

思路是使用一个变量记录下重复的元素个数，这样下标 `i-count` 就是当前未重复的元素的位置了。结果用总长度减去重复元素个数就好了。

```c++
class Solution {
public:
    int removeDuplicates(vector<int> &nums) {
        if (nums.empty()) return 0;
        int count = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                count++;
            } else {
                if (count > 0) {
                    nums[i - count] = nums[i];
                }
            }
        }
        return nums.size() - count;
    }
};
```