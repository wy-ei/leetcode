## 1. Two Sum

- 难度： 简单
- 通过率： 39.7%
- 题目链接：[https://leetcode.com/problems/two-sum](https://leetcode.com/problems/two-sum)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个整数数组 <code>nums</code>&nbsp;和一个目标值 <code>target</code>，请你在该数组中找出和为目标值的那&nbsp;<strong>两个</strong>&nbsp;整数，并返回他们的数组下标。</p>

<p>你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。</p>

<p><strong>示例:</strong></p>

<pre>给定 nums = [2, 7, 11, 15], target = 9

因为 nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9
所以返回 [<strong>0, 1</strong>]
</pre>

### 解法：

需要在数组中寻找两个数使其和为 target，可以将数组中的值存放在 map 中并记录下标，这样在遍历的过程中，如果当前元素为 a，那么寻找 target - a 的值时就能够得到加速。


```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in mp:
                return [mp[other], i]
            else:
                mp[num] = i
                
        return [0, 0]
```