## 51. N-Queens

- 难度： 困难
- 通过率： 36.7%
- 题目链接：[https://leetcode.com/problems/n-queens](https://leetcode.com/problems/n-queens)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p><em>n&nbsp;</em>皇后问题研究的是如何将 <em>n</em>&nbsp;个皇后放置在 <em>n</em>&times;<em>n</em> 的棋盘上，并且使皇后彼此之间不能相互攻击。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png"></p>

<p><small>上图为 8 皇后问题的一种解法。</small></p>

<p>给定一个整数 <em>n</em>，返回所有不同的&nbsp;<em>n&nbsp;</em>皇后问题的解决方案。</p>

<p>每一种解法包含一个明确的&nbsp;<em>n</em> 皇后问题的棋子放置方案，该方案中 <code>&#39;Q&#39;</code> 和 <code>&#39;.&#39;</code> 分别代表了皇后和空位。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 4
<strong>输出:</strong> [
 [&quot;.Q..&quot;,  // 解法 1
  &quot;...Q&quot;,
  &quot;Q...&quot;,
  &quot;..Q.&quot;],

 [&quot;..Q.&quot;,  // 解法 2
  &quot;Q...&quot;,
  &quot;...Q&quot;,
  &quot;.Q..&quot;]
]
<strong>解释:</strong> 4 皇后问题存在两个不同的解法。
</pre>


### 解法：

采用回溯剪枝策略，在每次深入前检查当前位置是否会产生冲突。

在检查是否发生冲突的时候，需要根据前面排定的行中皇后的位置，来决定当前位置是否合法。

同在一列的时候不合法，处于一条斜线上时不合法。

- 同一列：x 相同
- 斜线：x 之差，等于 y 之差

```
        x
----------------->
. o . . . . . .  |
. . . . . . . o  |
. x . x . . x x  | y
                 |
                 v
```

```python
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        
        self.__n_queues(n, (), solutions)
        
        return [self.__format(solution) for solution in solutions]
        
    def __conflict(self, state, x):
        y = len(state)
        for i in range(y):
            if abs(state[i] - x) in (0, y - i):
                return True
        return False
            
    def __n_queues(self, n, state, solutions):
        for pos in range(n):
            if self.__conflict(state, pos):
                continue
            next_state = state + (pos,)
            if len(next_state) == n:
                solutions.append(next_state)
            else:
                self.__n_queues(n, state + (pos,), solutions)
                
    def __format(self, solution):
        n = len(solution)
        return ['.' * pos + 'Q' + '.' * (n - pos -1) for pos in solution]
```