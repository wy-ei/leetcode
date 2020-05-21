## 50. 第一个只出现一次的字符

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。</p>

<p><strong>示例:</strong></p>

<pre>s = &quot;abaccdeff&quot;
返回 &quot;b&quot;

s = &quot;&quot; 
返回 &quot; &quot;
</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= s 的长度 &lt;= 50000</code></p>


## 解法：

先遍历字符串，使用 map 记录下各个字符出现的次数。然后再次顺序遍历字符串，找出第一个出现一次的字符。

```c++
class Solution {
public:
    char firstUniqChar(string s) {
        unordered_map<char, int> mp;
        for(char ch: s){
            mp[ch] += 1;
        }
        for(char ch: s){
            if(mp[ch] == 1){
                return ch;
            }
        }
        return ' ';
    }
};
```