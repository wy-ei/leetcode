## 5. Longest Palindromic Substring

- 难度： 中等
- 通过率： 25.9%
- 题目链接：[https://leetcode.com/problems/longest-palindromic-substring](https://leetcode.com/problems/longest-palindromic-substring)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串 <code>s</code>，找到 <code>s</code> 中最长的回文子串。你可以假设&nbsp;<code>s</code> 的最大长度为 1000。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> &quot;babad&quot;
<strong>输出:</strong> &quot;bab&quot;
<strong>注意:</strong> &quot;aba&quot; 也是一个有效答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> &quot;cbbd&quot;
<strong>输出:</strong> &quot;bb&quot;
</pre>


## 解法 1

直接暴力搜索，尝试所有的开头和结尾。时间复杂度为 `O(n^3)`，不符合要求。

```python
class Solution:
    def is_palindrome(self, s, start, end):
        end -= 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        max_palindrome_len = 0
        max_palindrome_range = (0, 0)
        for start in range(len(s) - 1):
            for end in range(len(s), start, -1):
                if self.is_palindrome(s, start, end):
                    palindrome_len = end - start
                    if max_palindrome_len < palindrome_len:
                        max_palindrome_len = palindrome_len
                        max_palindrome_range = (start, end)
        return s[max_palindrome_range[0]:max_palindrome_range[1]]
```


## 解法 2

确定一个中心，然后向两边扩展找到各个中心的对应的最长回文串。因为回文串中心可以是一个字符，也可以是两个字符（或中心位于两个字符中间），这样以来共有 2n - 1 个可能的中心，因此时间复杂度为 `O(n^2)`

```python
class Solution:
    def expand(self, s, left, right):
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        max_len = 0
        start = 0

        for i in range(len(s) - 1):
            l1 = self.expand(s, i-1, i+1)
            l2 = self.expand(s, i, i+1)
            max_l = max(l1, l2)

            if max_l > max_len:
                max_len = max_l
                start = i - (max_l - 1) // 2

        return s[start: start + max_len]
```