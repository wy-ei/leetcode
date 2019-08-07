## 115. Distinct Subsequences

- 难度： 困难
- 通过率： 34.1%
- 题目链接：[https://leetcode.com/problems/distinct-subsequences](https://leetcode.com/problems/distinct-subsequences)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串&nbsp;<strong>S&nbsp;</strong>和一个字符串&nbsp;<strong>T</strong>，计算在 <strong>S</strong> 的子序列中 <strong>T</strong> 出现的个数。</p>

<p>一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，<code>&quot;ACE&quot;</code>&nbsp;是&nbsp;<code>&quot;ABCDE&quot;</code>&nbsp;的一个子序列，而&nbsp;<code>&quot;AEC&quot;</code>&nbsp;不是）</p>


## 解法：


### 动态规划

`table[i, j]` 代表 T 的前 i 个字符，可以由 S 的前 j 个字符构成的个数。

转移方程:

**1.** 当 `S[j] == T[i]` 时，`S[j]` 有两种选择：

- `S[j]` 参与构成用于与 T 进行匹配的字串，此时就是为 `S[:j]` 和 `T[:i]` 各拼接了一个相同的字符，因此 `S[:j+1]` 和 `T[:i+1]` 得出的个数，与 `S[:j]` 和 `T[:i]` 得出的个数相同。此个数就等于 `table[i-1, j-1]`。

- `S[j]` 不参与构成字串，此时需要用 `S[:j]` 来构成和 `T[:i+1]` 匹配的子串，个数为 `table[i, j-1]`。 

因此 `table[i, j] = table[i-1, j-1] + table[i, j-1]`

**2.** 当 `S[j] != T[i]`  时：

`S[j]` 没法参与构成字串，只能依赖于 `S[:j]]` 来构成和 `T[:i+1]` 匹配的子串。因此：`table[i, j] = table[i, j-1]`

举例如下：

![](./images/115_dp.png)
图来源于 https://leetcode-cn.com/problems/two-sum/solution/dong-tai-gui-hua-by-powcai-5/

第一行, T 为空串，因为空串是所有字符串子集，且仅有一种可能, 所以第一行都是 1。

第一列, S 为空，这样组成 T 个数自然为 0。

```python
import numpy as np

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        table = np.zeros((1 + len(t), 1 + len(s)), dtype=int)
        table[:, 0] = 0
        table[0] = 1
        
        for i, t_char in enumerate(t, 1):
            for j, s_char in enumerate(s, 1):
                if s_char == t_char:
                    table[i, j] = table[i-1, j-1] + table[i, j-1]
                else:
                    table[i, j] = table[i, j-1]
        return table[-1,-1]
```