---
title: 单词拆分
qid: 139
tags: [动态规划]
---


- 难度： 中等
- 通过率： 33.7%
- 题目链接：[https://leetcode-cn.com/problems/word-break](https://leetcode-cn.com/problems/word-break)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个<strong>非空</strong>字符串 <em>s</em> 和一个包含<strong>非空</strong>单词列表的字典 <em>wordDict</em>，判定&nbsp;<em>s</em> 是否可以被空格拆分为一个或多个在字典中出现的单词。</p>

<p><strong>说明：</strong></p>

<ul>
	<li>拆分时可以重复使用字典中的单词。</li>
	<li>你可以假设字典中没有重复的单词。</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> s = &quot;leetcode&quot;, wordDict = [&quot;leet&quot;, &quot;code&quot;]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 &quot;leetcode&quot; 可以被拆分成 &quot;leet code&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> s = &quot;applepenapple&quot;, wordDict = [&quot;apple&quot;, &quot;pen&quot;]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 <code>&quot;</code>applepenapple<code>&quot;</code> 可以被拆分成 <code>&quot;</code>apple pen apple<code>&quot;</code>。
&nbsp;    注意你可以重复使用字典中的单词。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]
<strong>输出:</strong> false
</pre>


## 解法：

### 解法 1. 广度优先搜索

整个字符串是由多个单词拼接而成的，这些单词的拼接组合构成了一颗巨大的树。如果有一条路径上的单词可以构成该字符串，则说明有解。但是暴力搜索这个树，其时间复杂度为 `O(n^n)`。

基于广度优先的搜索方法，可以大幅度减少时间复杂度。其思想是，在字典中寻找字符串的前缀，然后移除前缀，继续寻找前缀。直到最后字符串为空时，认为字典里的单词可以构成该字符串。

下面的代码中，从下标 0 开始，寻找前缀字符串，然后将结尾下标入队列，下一次取出该值作为新的起始下标。

```python
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        queue = [0]
        words = set(wordDict)
        
        while queue:
            start = queue.pop(0)
            if start == len(s):
                return True
            
            for end in range(start+1, len(s)+1):
                if s[start:end] in words:
                    queue.append(end)
            
        return False
```

但是上面这种方法依然超时了，动态规划能够得到更低的时间复杂度。


### 解法 2. 动态规划

对于字符串 `s`，如果 `s[:i]` 和 `s[i:]` 均可以由字典中的单词组成，那么整个字符串 `s` 也就可以由字典中单词组成。

用 `dp[i]` 表示 `s[:i]` 是否可由字典中单词组成。

```python
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        words = set(wordDict)
        
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
                    
        return dp[-1]
```