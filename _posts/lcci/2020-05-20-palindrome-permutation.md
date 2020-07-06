---
title: 回文排列
qid: 01.04
tags: [哈希表,字符串]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/palindrome-permutation-lcci/](https://leetcode-cn.com/problems/palindrome-permutation-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。</p>

<p>回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。</p>

<p>回文串不一定是字典当中的单词。</p>



<p><strong>示例1：</strong></p>

<pre><strong>输入：&quot;</strong>tactcoa&quot;
<strong>输出：</strong>true（排列有&quot;tacocat&quot;、&quot;atcocta&quot;，等等）
</pre>




## 解法：

回文排列的特点是：要么所有字符都出现偶数次，要么只有一个字符串出现奇数次。因此，可以使用一个集合，遍历每个字符，如果该字符在集合中已经存在，那就删除字符，否则就插入字符。最终集合为空，或者只有一个元素，说明此字符串中的字符可以构成一个回文串。

```c++
class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_set<char> chars;
        for(char ch: s){
            if(chars.count(ch) == 1){
                chars.erase(ch);
            }else{
                chars.insert(ch);
            }
        }
        return chars.size() <= 1;
    }
};
```