## 40. 最小的k个数

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>输入整数数组 <code>arr</code> ，找出其中最小的 <code>k</code> 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [3,2,1], k = 2
<strong>输出：</strong>[1,2] 或者 [2,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [0,1,2,1], k = 1
<strong>输出：</strong>[0]</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul>
	<li><code>0 &lt;= k &lt;= arr.length &lt;= 10000</code></li>
	<li><code>0 &lt;= arr[i]&nbsp;&lt;= 10000</code></li>
</ul>


## 解法一：使用 `partition`

快速排序中，使用切分的方法，将原数组分为两部分。前一部分小于 pivot，第二部分大于 pivot。如果切分点在下标 k 处，那么前 k 个元素不就是最小的 k 个元素了吗。

```c++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& nums, int k) {
        int lo = 0, hi = nums.size();
        while(lo < hi){
            int i = partition(nums, lo, hi);
            if(i < k){
                lo = i + 1;
            }else if(i > k){
                hi = i;
            }else{
                break;
            }
        }
        return vector<int>(nums.begin(), nums.begin()+k);
    }
private:
    static int partition(vector<int>& a, int lo, int hi) {
        int v = a[lo];
        int i = lo;
        int j = hi;
        while (true) {
            while (++i < hi && a[i] < v);
            while (a[--j] > v);
            if (i >= j) break;
            ::swap(a[i], a[j]);
        }
        ::swap(a[lo], a[j]);
        return j;
    }
};
```


C++ 中有 `nth_element` 算法，这个算法的实现思路和上面的思路一致。

```c++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& nums, int k) {
        nth_element(nums.begin(), nums.begin()+k, nums.end());
        return vector<int>(nums.begin(), nums.begin()+k);
    }
};
```

## 使用优先队列

使用优先队列记录下最小的 k 个元素。

```c++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& nums, int k) {
        priority_queue<int> pq;

        for(int n: nums){
            pq.push(n);
            if(pq.size() == k + 1){
                pq.pop();
            }
        }

        vector<int> ret;
        while(!pq.empty()){
            ret.push_back(pq.top());
            pq.pop();
        }

        return ret;
    }
};
```