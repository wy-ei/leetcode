---
title: 单词转换
qid: 17.22
tags: [深度优先搜索,广度优先搜索,数组,字符串]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/word-transformer-lcci/](https://leetcode-cn.com/problems/word-transformer-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。</p>

<p>编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

<strong>输出:</strong>
[&quot;hit&quot;,&quot;hot&quot;,&quot;dot&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

<strong>输出: </strong>[]

<strong>解释:</strong>&nbsp;<em>endWord</em> &quot;cog&quot; 不在字典中，所以不存在符合要求的转换序列。</pre>


## 解法：

DFS 加剪枝。剪枝的策略很简单，使用一个集合保存使用过的 word，避免绕圈子。

```c++
class Solution {
public:
    vector<string> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> word_set(wordList.begin(), wordList.end());
        unordered_set<string> seen_words;
        
        vector<string> path{beginWord};
        bool found = dfs(beginWord, endWord, word_set, seen_words, path);
        if(found){
            return path;
        }else{
            return {};
        }
    }


    bool dfs(const string& head, const string& tail, unordered_set<string>& word_set, unordered_set<string>& seen_words, vector<string>& path){
        if(head == tail){
            return true;
        }
        word_set.erase(head);
        for(int i=0;i<head.size();i++){
            string w = head;
            for(char ch='a'; ch <= 'z'; ch++){
                w[i] = ch;
                if(word_set.count(w) == 1 && seen_words.count(w) == 0){
                    seen_words.insert(w);
                    path.push_back(w);
                    bool found = dfs(w, tail, word_set, seen_words, path);
                    if(found){
                        return true;
                    }
                    path.pop_back();
                }
            }
        }
        word_set.insert(head);
        return false;
    }
};
```