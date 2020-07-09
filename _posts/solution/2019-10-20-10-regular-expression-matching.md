---
title: 正则表达式匹配
qid: 10
tags: [字符串,动态规划,回溯算法]
---


- 难度： 困难
- 通过率： 24.7%
- 题目链接：[https://leetcode-cn.com/problems/regular-expression-matching](https://leetcode-cn.com/problems/regular-expression-matching)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串&nbsp;(<code>s</code>) 和一个字符模式&nbsp;(<code>p</code>)。实现支持 <code>&#39;.&#39;</code>&nbsp;和&nbsp;<code>&#39;*&#39;</code>&nbsp;的正则表达式匹配。</p>

<pre>&#39;.&#39; 匹配任意单个字符。
&#39;*&#39; 匹配零个或多个前面的元素。
</pre>

<p>匹配应该覆盖<strong>整个</strong>字符串&nbsp;(<code>s</code>) ，而不是部分字符串。</p>

<p><strong>说明:</strong></p>

<ul>
	<li><code>s</code>&nbsp;可能为空，且只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母。</li>
	<li><code>p</code>&nbsp;可能为空，且只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母，以及字符&nbsp;<code>.</code>&nbsp;和&nbsp;<code>*</code>。</li>
</ul>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
s = &quot;aa&quot;
p = &quot;a&quot;
<strong>输出:</strong> false
<strong>解释:</strong> &quot;a&quot; 无法匹配 &quot;aa&quot; 整个字符串。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
s = &quot;aa&quot;
p = &quot;a*&quot;
<strong>输出:</strong> true
<strong>解释:</strong>&nbsp;&#39;*&#39; 代表可匹配零个或多个前面的元素, 即可以匹配 &#39;a&#39; 。因此, 重复 &#39;a&#39; 一次, 字符串可变为 &quot;aa&quot;。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong>
s = &quot;ab&quot;
p = &quot;.*&quot;
<strong>输出:</strong> true
<strong>解释:</strong>&nbsp;&quot;.*&quot; 表示可匹配零个或多个(&#39;*&#39;)任意字符(&#39;.&#39;)。
</pre>

<p><strong>示例 4:</strong></p>

<pre><strong>输入:</strong>
s = &quot;aab&quot;
p = &quot;c*a*b&quot;
<strong>输出:</strong> true
<strong>解释:</strong>&nbsp;&#39;c&#39; 可以不被重复, &#39;a&#39; 可以被重复一次。因此可以匹配字符串 &quot;aab&quot;。
</pre>

<p><strong>示例 5:</strong></p>

<pre><strong>输入:</strong>
s = &quot;mississippi&quot;
p = &quot;mis*is*p*.&quot;
<strong>输出:</strong> false</pre>



## 解法：动态规划

设字符串为 s，模式串为 p。使用 i 作为 s 的下标，使用 j 作为 p 的下标。使用 `match[i][j] = true` 来表示 `s[0:i]` 与 `p[0:j]` 匹配。这里采用 python 中的表示法，`s[0:0]` 代表空串。`match[0][0] = true`，表示空字符串和空模式串匹配。

模式串中有三类字符：

- 常规字符：若 `s[i] == p[j]` 且 `match[i][j] == true` 时 `match[i+1][j+1] == true`。
- `.`：因为`.`能匹配任意字符，此时 `match[i+1][j+1] = match[i][j]`
- `*`：`*` 可以把前面的字符重复 0 次或数次。因此，只需要考虑这两种情况：
  - 重复 0 次，那么就忽略 `*` 和 `*` 前面的字符。`match[i+1][j+1] = match[i+1][j-1]`
  - 重复多次，需要满足 `s[i] == p[j-1] || p[j-1] == '.'`，此时 `match[i+1][j+1] = match[i][j+1]`。即查看 `s[0:i]` 是否和 p[:j+1] 匹配，由于 `p[j]` 是 `*`，如果匹配，那么必然有 `s[i] == s[i-1]`。


初始状态：

- `match[0][0] = true`
- 空字符串可能和非空模式串匹配，比如 `" "` 和 `"a*b*c*"` 匹配。空串时，遇到 `*` 比如选择重复其之前的字符 0 次，此时 `match[0][i+1] = match[0][i-1]`。


```c++
class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> match(s.size()+1, vector<bool>(p.size()+1, false));
        match[0][0] = true;
        for(int i=0;i<p.size();i++){
            if(p[i] == '*'){
                match[0][i+1] = match[0][i-1];
            }
        }
        for(int i=0;i<s.size();i++){
            for(int j=0;j<p.size();j++){
                if(p[j] == s[i] || p[j] == '.'){
                    match[i+1][j+1] = match[i][j];
                }
                if( p[j] == '*'){
                    match[i+1][j+1] = match[i+1][j-1];

                    if(p[j-1] == '.' || p[j-1] == s[i]){
                        match[i+1][j+1] = match[i+1][j+1] || match[i][j+1];
                    }
                }
            }
        }
        return match[s.size()][p.size()];
    }
};
```

## 解法 2

另外可以使用 NFA（非确定有限状态机）来解决，参加普林斯顿出的算法（第四版）

```python

class Digraph:
    def __init__(self, V):
        self.__V = V
        self.__E = 0
        self.__adj = [set() for _ in range(V)]

    def add_edge(self, v, w):
        self.__adj[v].add(w)
        self.__E += 1

    def V(self):
        return self.__V

    def E(self):
        return self.__E

    def adj(self, v):
        return self.__adj[v]

from collections import Iterable

class DirectedDFS:
    def __init__(self, graph, source):
        self.__marked = [0] * graph.V()
        if isinstance(source, Iterable):
            for s in source:
                self.dfs(graph, s)
        else:
            self.dfs(graph, source)

    def dfs(self, graph, v):
        self.__marked[v] = 1
        for w in graph.adj(v):
            if self.__marked[w] == 0:
                self.dfs(graph, w)

    def marked(self, v):
        return self.__marked[v]


# 非确定有限自动机
def NFA(regexp):
    M = len(regexp)
    g = Digraph(M + 1)
    for i, c in enumerate(regexp):
        if i < M - 1 and regexp[i+1] == '*':
            g.add_edge(i, i+1)
            g.add_edge(i+1, i)

        if regexp[i] == '*':
            g.add_edge(i, i+1)
    return g


def recognizes(txt, regexp):
    digraph = NFA(regexp)
    dfs = DirectedDFS(digraph, 0)
    pc = set()

    for v in range(digraph.V()):
        if dfs.marked(v):
            pc.add(v)

    for i, c in enumerate(txt):
        match = set()

        for v in pc:
            if v < len(regexp):
                if regexp[v] == txt[i] or regexp[v] == '.':
                    match.add(v+1)

        pc = set()
        dfs = DirectedDFS(digraph, match)
        for v in range(digraph.V()):
            if dfs.marked(v):
                pc.add(v)

    for v in pc:
        if v == len(regexp):
            return True

    return False

```