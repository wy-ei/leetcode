## 46. Permutations

- 难度： 中等
- 通过率： 52.1%
- 题目链接：[https://leetcode.com/problems/permutations](https://leetcode.com/problems/permutations)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个<strong>没有重复</strong>数字的序列，返回其所有可能的全排列。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [1,2,3]
<strong>输出:</strong>
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]</pre>


## 解法 1. Heap Permute：

采用著名的 [Heap's algorithm](https://en.wikipedia.org/wiki/Heap's_algorithm) 来解答。

```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        
        self.__heap_permute(nums, len(nums), results)
        
        return results
        
    def __heap_permute(self, nums, n, results):
        if n == 1:
            results.append(nums.copy())
        else:
            for i in range(n):
                self.__heap_permute(nums, n-1, results)
                if n % 2 == 1:
                    nums[0], nums[n-1] = nums[n-1],nums[0]
                else:
                    nums[i], nums[n-1] = nums[n-1], nums[i]
```


当 n（即数组长度）为奇数时候，算法结束后 `nums[0:n]` 会保持原先的位置，而当 n 为偶数时，`nums[0:n]` 中的元素会循环右移一位。

当 n = 1时，输出数组 nums 的拷贝

当 n > 1 时:

1. 当 n 为偶数时，heap_permute(n-1) 会生对前 n-1 个元素进行全排列，结束后保持原样。因此在循环中，只需要将第 n 个元素和第 i 个元素交换，就能得到前 n 个元素的全排列。
2. 当 n 为奇数时，heap_permute(n-1) 会生对前 n-1 个元素进行全排列，结果是 nums 中前 n-1 个元素循环右移了一位。因此只需要在循环中将第一个元素和第 n 个元素进行交换。迭代完成后，就能得到前 n 个元素的全排列。


**时间复杂度：**

- 当 n = 1 时，T(n) = 1。 
- 当 n > 1 时，T(n) = nT(n-1) + 2。

将其展开有：

T(n) = n((n-1)((n-2)((n-3)… + 2) + 2) + 2

故时间复杂度为 O(n!)

## 解法 2. DFS

这个方法就简单多了，只需要深度优先搜索就可以了。

```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        
        self.__permute(nums, [], results)
        return results
        
    def __permute(self, remain_nums, path, results):
        if len(remain_nums) == 0:
            results.append(path + remain_nums)
        else:
            for i, n in enumerate(remain_nums):
                self.__permute(remain_nums[:i] + remain_nums[i+1:], path + [n], results)
```

