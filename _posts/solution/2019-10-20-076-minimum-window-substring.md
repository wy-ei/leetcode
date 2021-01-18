---
title: 最小覆盖子串
qid: 76
tag: [哈希表, 双指针, 字符串]
---

- 难度： 困难
- 通过率： 29.2%
- 题目链接：[https://leetcode-cn.com/problems/minimum-window-substring](https://leetcode-cn.com/problems/minimum-window-substring)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入: S</strong> = &quot;ADOBECODEBANC&quot;, <strong>T</strong> = &quot;ABC&quot;
<strong>输出:</strong> &quot;BANC&quot;</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>如果 S 中不存这样的子串，则返回空字符串 <code>&quot;&quot;</code>。</li>
	<li>如果 S 中存在这样的子串，我们保证它是唯一的答案。</li>
</ul>


## 解法：

```c++
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> required_counter;
        int required_num = t.size();
        for(char ch: t){
            required_counter[ch]++;
        }
        int min_len = s.size();
        int start = 0;
        bool found = false;

        for(int lo=0,hi=0; hi < s.size(); hi++){
            char ch = s[hi];
            if(required_counter.count(ch) == 1){
                if(required_counter[ch] > 0){
                    required_num--;
                }
                required_counter[ch]--;
            }

            if(required_num == 0){
                found = true;
                while(lo < hi){
                    if(required_counter.find(s[lo]) == required_counter.end()){
                        lo++;
                    }else if(required_counter[s[lo]] < 0){
                        required_counter[s[lo]]++;
                        lo++;
                    }else{
                        break;
                    }
                }
                if(min_len > hi - lo + 1){
                    min_len = hi - lo + 1;
                    start = lo;
                }
            }
        }
        if(found){
            return s.substr(start, min_len);
        }else{
            return "";
        }
    }
};
```