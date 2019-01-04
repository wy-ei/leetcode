## 3. Longest Substring Without Repeating Characters

- 难度： 中等
- 通过率： 25.7%
- 题目链接：[https://leetcode.com/problems/longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串，请你找出其中不含有重复字符的&nbsp;<strong>最长子串&nbsp;</strong>的长度。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong>&quot;abcabcbb&quot;
<strong>输出: </strong>3 
<strong>解释:</strong> 因为无重复字符的最长子串是 <code>&quot;abc&quot;，所以其</code>长度为 3。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>&quot;bbbbb&quot;
<strong>输出: </strong>1
<strong>解释: </strong>因为无重复字符的最长子串是 <code>&quot;b&quot;</code>，所以其长度为 1。
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入: </strong>&quot;pwwkew&quot;
<strong>输出: </strong>3
<strong>解释: </strong>因为无重复字符的最长子串是&nbsp;<code>&quot;wke&quot;</code>，所以其长度为 3。
&nbsp;    请注意，你的答案必须是 <strong>子串 </strong>的长度，<code>&quot;pwke&quot;</code>&nbsp;是一个<em>子序列，</em>不是子串。
</pre>


### 解法：

使用 `substring_start_index` 始终指向子字符串的开头，在一个 `map` 中记录各个字符出现的索引，如果在 `map` 中发现之前出现过的字符，那么子字符串的起始位置就应该调整到前面那个重复的字符处，因为子字符串不可能包含那个重复的字符。最长的子字符串只能出现在非重复的字符出现的时候。

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_length = 0
        substring_start_index = -1

        for i, c in enumerate(s):
            if c in char_map and char_map[c] > substring_start_index:
                substring_start_index = char_map[c]
                char_map[c] = i
            else:
                char_map[c] = i
                if i - substring_start_index > max_length:
                    max_length = i - substring_start_index

        return max_length
```

