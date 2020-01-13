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



## 解法

确定一个中心，然后向两边扩展找到各个中心的对应的最长回文串。因为回文串中心可以是一个字符，也可以是两个字符（或中心位于两个字符中间），这样以来共有 2n - 1 个可能的中心，因此时间复杂度为 `O(n^2)`

```cpp

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() < 2) return s;

        int max_len = 0;
        int start = 0;
        for(int i = 0;i<s.size();i++) {
            int len1 = expand(s, i - 1, i + 1);
            int len2 = expand(s, i, i + 1);
            int len = max(len1, len2);
            if (len > max_len) {
                start = i - (len - 1) / 2;
                max_len = len;
            }
        }
        return s.substr(start, max_len);
    }

    int expand(const string &s, int lo, int hi){
        while(lo >= 0 && hi < s.size() && s[lo] == s[hi]){
            --lo;
            ++hi;
        }
        return hi - lo - 1;
    }
};
```