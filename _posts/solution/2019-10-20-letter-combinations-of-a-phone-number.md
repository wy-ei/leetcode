---
title: 电话号码的字母组合
qid: 17
tags: [字符串,回溯算法]
---


- 难度： 中等
- 通过率： 39.5%
- 题目链接：[https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个仅包含数字&nbsp;<code>2-9</code>&nbsp;的字符串，返回所有它能表示的字母组合。</p>

<p>给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。</p>

<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png"></p>

<p><strong>示例:</strong></p>

<pre><strong>输入：</strong>&quot;23&quot;
<strong>输出：</strong>[&quot;ad&quot;, &quot;ae&quot;, &quot;af&quot;, &quot;bd&quot;, &quot;be&quot;, &quot;bf&quot;, &quot;cd&quot;, &quot;ce&quot;, &quot;cf&quot;].
</pre>

<p><strong>说明:</strong><br>
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。</p>



## 解法：

以 23 为例，遇到 2 就往结果中加入 `"a" "b" "c"` 三个字符串，遇到 3 就往结果集中的每一个后面分别添加 `'d' 'e' 'f'`，如此就得到了最终结果。

```c++
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits.empty()) return {};
        vector<string> result{""};
        unordered_map<char, string> table{
            {'0', " "},
            {'1', "*"},
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        for(char n: digits) {
            vector<string> t;
            for(char ch: table[n]){
                for(auto& s: result){
                    t.push_back(s + ch);
                }
            }
            result = ::move(t);
        }
        return result;
    }
};
```