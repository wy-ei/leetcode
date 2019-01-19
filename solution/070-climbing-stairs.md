## 70. Climbing Stairs

- 难度： 简单
- 通过率： 42.7%
- 题目链接：[https://leetcode.com/problems/climbing-stairs](https://leetcode.com/problems/climbing-stairs)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>假设你正在爬楼梯。需要 <em>n</em>&nbsp;阶你才能到达楼顶。</p>

<p>每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>

<p><strong>注意：</strong>给定 <em>n</em> 是一个正整数。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> 2
<strong>输出：</strong> 2
<strong>解释：</strong> 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong> 3
<strong>输出：</strong> 3
<strong>解释：</strong> 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
</pre>


### 解法：

上 n 层楼梯，可以上到 n-1 层然后一步跨一阶上去，也可以上到 n-2 层一步跨两阶上去。因此上 n 层楼的走法等于上 n-1 层楼和上 n-2 层楼的走法之和。这也算是动态规划类型的问题了。


递归解，使用一个变量缓存结果，这样的解法往往出现在讲编程技巧的书籍中，实际场景中当然希望避免使用递归。

```python
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        
        return self.__climb(n, cache)
    
    def __climb(self, n, cache):
        if n in cache:
            return cache[n]
        
        if n <= 2:
            return n
        
        cache[n] = self.__climb(n-1, cache) + self.__climb(n-2, cache)
        
        return cache[n]
```

使用迭代，显然会加快计算的速度。

```python
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return n
        
        a = 1
        b = 2
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            
        return c
```