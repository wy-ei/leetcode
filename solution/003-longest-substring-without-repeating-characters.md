## 3. Longest Substring Without Repeating Characters

- 难度： 中等
- 通过率： 25.7%
- 题目链接：[https://leetcode.com/problems/longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)


## 题目描述

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


## 解法一：滑动窗口

本题最容易想到的就是滑动窗口的解法，从左到右遍历字符串，使用一个集合保存字符，不断扩大窗口右边界，如果发现右边界的值已经存在于窗口中了，那就收缩窗口左边界。

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charset;
        int max_len = 0;
        int lo = 0, hi = 0;
        for(;hi < s.size();hi++){
            while(charset.count(s[hi]) == 1){
                charset.erase(s[lo++]);
            }
            charset.insert(s[hi]);
            max_len = ::max(max_len, hi - lo + 1);
        }
        return max_len;
    }
};
```

## 解法二：哈希表

滑动窗口在收缩窗口左边界的时候需要向后遍历，这导致算法时间复杂度为 `O(n^2)`，向右遍历的目的就是寻找等于 `s[hi]` 的值，如果能够把窗口中的值的下标记录下来，就省了内层的遍历了。

如发现了重复的字符，窗口的起始位置就要更新为先前出现的重复字符的后一个位置处。

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> mp;
        int start = 0;
        int max_len = 0;
        for(int i=0;i<s.size();i++){
            char ch = s[i];
            if(mp.find(ch) != mp.end()){
                start = ::max(start, mp[ch] + 1);
            }
            mp[ch] = i;
            max_len = ::max(max_len, i - start + 1);
        }
        return max_len;
    }
};
```

