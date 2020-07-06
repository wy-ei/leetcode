---
title: 单词拆分 II
qid: 140
tags: [动态规划,回溯算法]
---


- 难度： 困难
- 通过率： 26.2%
- 题目链接：[https://leetcode-cn.com/problems/word-break-ii](https://leetcode-cn.com/problems/word-break-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个<strong>非空</strong>字符串 <em>s</em> 和一个包含<strong>非空</strong>单词列表的字典 <em>wordDict</em>，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。</p>

<p><strong>说明：</strong></p>

<ul>
	<li>分隔时可以重复使用字典中的单词。</li>
	<li>你可以假设字典中没有重复的单词。</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:
</strong>s = &quot;<code>catsanddog</code>&quot;
wordDict = <code>[&quot;cat&quot;, &quot;cats&quot;, &quot;and&quot;, &quot;sand&quot;, &quot;dog&quot;]</code>
<strong>输出:
</strong><code>[
&nbsp; &quot;cats and dog&quot;,
&nbsp; &quot;cat sand dog&quot;
]</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:
</strong>s = &quot;pineapplepenapple&quot;
wordDict = [&quot;apple&quot;, &quot;pen&quot;, &quot;applepen&quot;, &quot;pine&quot;, &quot;pineapple&quot;]
<strong>输出:
</strong>[
&nbsp; &quot;pine apple pen apple&quot;,
&nbsp; &quot;pineapple pen apple&quot;,
&nbsp; &quot;pine applepen apple&quot;
]
<strong>解释:</strong> 注意你可以重复使用字典中的单词。
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre><strong>输入:
</strong>s = &quot;catsandog&quot;
wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]
<strong>输出:
</strong>[]
</pre>


## 解法：

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        if not self.can_break(s, words):
            return []
        
        dp = [['']] + [[] for _ in s]
        
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in words:
                    for sub in dp[j]:
                        if sub:
                            sub = sub + ' '
                        dp[i].append(sub + s[j:i])
                
        return dp[-1]
    
    def can_break(self, s, words):
        dp = [True] + [False] * len(s)
        
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break;
        return dp[-1]
```

```cpp
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> words = unordered_set<string>(wordDict.begin(), wordDict.end());

        if(!this->can_break(s, words)){
            return vector<string> ret(0);
        }

        vector<vector<string>> dp(s.size()+1);
        dp[0].push_back("");

        for(size_t i=1;i<=s.size();i++){
            for(size_t j=0;j<i;j++){
                string word = s.substr(j, i-j);
                if(dp[j].size() > 0 && words.find(word) != words.end()){
                    for(string sub: dp[j]){
                        if(!sub.empty()){
                            sub += " ";
                        }
                        dp[i].push_back(sub + word);
                    }
                }
            }
        }
        return dp[s.size()];
    }
    
    bool can_break(string s, unordered_set<string>& words){
        vector<bool> dp(s.size()+1);
        dp[0] = true;

        for(size_t i = 1; i<=s.size();i++){
            for(size_t j=0;j<i;j++){
                string word = s.substr(j, i-j);
                if(dp[j] && words.find(word) != words.end()){
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.size()];
    }
};
```