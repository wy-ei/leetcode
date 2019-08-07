## 137. Single Number II

- 难度： 中等
- 通过率： 44.6%
- 题目链接：[https://leetcode.com/problems/single-number-ii](https://leetcode.com/problems/single-number-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个<strong>非空</strong>整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。</p>

<p><strong>说明：</strong></p>

<p>你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [2,2,3,2]
<strong>输出:</strong> 3
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [0,1,0,1,0,1,99]
<strong>输出:</strong> 99</pre>


## 解法：

当一个数出现三次的时候，如果能够通过某种方式将其抵消掉，这样就可以保留下只出现过一次的数了。

注意到下面的运算规律：

```
0 ^ a = a
a ^ a = 0

0 & a = 0
a & a = a
a & ~a = 0
```


```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        even, odd, mask = 0, 0, 0
        for num in nums:
            even ^= odd & num
            odd ^= num
            mask = (odd & even)
            even &= ~mask
            odd &= ~mask
        return odd
```
