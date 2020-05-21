## 19. 正则表达式匹配

- 难度：Hard
- 题目链接：[https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>请实现一个函数用来匹配包含<code>&#39;. &#39;</code>和<code>&#39;*&#39;</code>的正则表达式。模式中的字符<code>&#39;.&#39;</code>表示任意一个字符，而<code>&#39;*&#39;</code>表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串<code>&quot;aaa&quot;</code>与模式<code>&quot;a.a&quot;</code>和<code>&quot;ab*ac*a&quot;</code>匹配，但与<code>&quot;aa.a&quot;</code>和<code>&quot;ab*a&quot;</code>均不匹配。</p>

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
<strong>解释:</strong>&nbsp;因为 &#39;*&#39; 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 &#39;a&#39;。因此，字符串 &quot;aa&quot; 可被视为 &#39;a&#39; 重复了一次。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong>
s = &quot;ab&quot;
p = &quot;.*&quot;
<strong>输出:</strong> true
<strong>解释:</strong>&nbsp;&quot;.*&quot; 表示可匹配零个或多个（&#39;*&#39;）任意字符（&#39;.&#39;）。
</pre>

<p><strong>示例 4:</strong></p>

<pre><strong>输入:</strong>
s = &quot;aab&quot;
p = &quot;c*a*b&quot;
<strong>输出:</strong> true
<strong>解释:</strong>&nbsp;因为 &#39;*&#39; 表示零个或多个，这里 &#39;c&#39; 为 0 个, &#39;a&#39; 被重复一次。因此可以匹配字符串 &quot;aab&quot;。
</pre>

<p><strong>示例 5:</strong></p>

<pre><strong>输入:</strong>
s = &quot;mississippi&quot;
p = &quot;mis*is*p*.&quot;
<strong>输出:</strong> false</pre>

<ul>
	<li><code>s</code>&nbsp;可能为空，且只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母。</li>
	<li><code>p</code>&nbsp;可能为空，且只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母以及字符&nbsp;<code>.</code>&nbsp;和&nbsp;<code>*</code>，无连续的 <code>&#39;*&#39;</code>。</li>
</ul>

<p>注意：本题与主站 10&nbsp;题相同：<a href="https://leetcode-cn.com/problems/regular-expression-matching/">https://leetcode-cn.com/problems/regular-expression-matching/</a></p>


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