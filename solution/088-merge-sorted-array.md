## 88. Merge Sorted Array

- 难度： 简单
- 通过率： 34.2%
- 题目链接：[https://leetcode.com/problems/merge-sorted-array](https://leetcode.com/problems/merge-sorted-array)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定两个有序整数数组&nbsp;<em>nums1 </em>和 <em>nums2</em>，将 <em>nums2 </em>合并到&nbsp;<em>nums1&nbsp;</em>中<em>，</em>使得&nbsp;<em>num1 </em>成为一个有序数组。</p>

<p><strong>说明:</strong></p>

<ul>
	<li>初始化&nbsp;<em>nums1</em> 和 <em>nums2</em> 的元素数量分别为&nbsp;<em>m</em> 和 <em>n</em>。</li>
	<li>你可以假设&nbsp;<em>nums1&nbsp;</em>有足够的空间（空间大小大于或等于&nbsp;<em>m + n</em>）来保存 <em>nums2</em> 中的元素。</li>
</ul>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong>
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

<strong>输出:</strong>&nbsp;[1,2,2,3,5,6]</pre>


## 解法：

思路：把较大的元素放到 `nums1` 的后面。

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        k = m + n - 1
        nums1_i = m - 1
        nums2_i = n - 1
        
        while nums1_i >=0 and nums2_i >= 0:
            if nums1[nums1_i] > nums2[nums2_i]:
                nums1[k] = nums1[nums1_i]
                nums1_i -= 1
            else:
                nums1[k] = nums2[nums2_i]
                nums2_i -= 1
            
            k -= 1
        
        while nums2_i >= 0:
            nums1[k] = nums2[nums2_i]
            k -= 1
            nums2_i -= 1    
```