## 78. Subsets

- 难度： 中等
- 通过率： 49.6%
- 题目链接：[https://leetcode.com/problems/subsets](https://leetcode.com/problems/subsets)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一组<strong>不含重复元素</strong>的整数数组&nbsp;<em>nums</em>，返回该数组所有可能的子集（幂集）。</p>

<p><strong>说明：</strong>解集不能包含重复的子集。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> nums = [1,2,3]
<strong>输出:</strong>
[
  [3],
&nbsp; [1],
&nbsp; [2],
&nbsp; [1,2,3],
&nbsp; [1,3],
&nbsp; [2,3],
&nbsp; [1,2],
&nbsp; []
]</pre>


## 解法：

### 解法 1 - 深度优先遍历

这算是常规操作，比较容易理解。

```python
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        
        self.__subsets(nums, 0, [], results)
        
        return results
    
    def __subsets(self, nums, i, subset, results):
        results.append(subset)
        
        for i in range(i, len(nums)):
            self.__subsets(nums, i+1, subset + [nums[i]], results) 
```


### 解法 2 - 位运算

数组 `[1,2,3]` 的子集也就是其中的三个元素取与不取的组合。把它想象为二进制的三个 bit 位 `1 1 1`，那么从 `0 0 0` 到 `1 1 1` 的 8 个数，就构成了所有子集的选取情况。比如 `0 0 1` 表示取第1个元素，`0 1 1` 表示取前两个元素。

```python
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        
        subsets_size = 2 ** len(nums)

        n = 0
        while n < subsets_size:
            subset = []
            
            i = 0
            bits = n
            while bits > 0:
                if bits & 1 == 1:
                    subset.append(nums[i])
                i += 1
                bits = bits >> 1
            
            n += 1
            results.append(subset)
        
        return results
```