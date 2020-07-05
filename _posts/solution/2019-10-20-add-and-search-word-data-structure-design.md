---
title: 添加与搜索单词 - 数据结构设计
qid: 211
tags: [设计,字典树,回溯算法]
---


- 难度： 中等
- 通过率： 28.3%
- 题目链接：[https://leetcode.com/problems/add-and-search-word-data-structure-design](https://leetcode.com/problems/add-and-search-word-data-structure-design)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>设计一个支持以下两种操作的数据结构：</p>

<pre>void addWord(word)
bool search(word)
</pre>

<p>search(word)&nbsp;可以搜索文字或正则表达式字符串，字符串只包含字母&nbsp;<code>.</code>&nbsp;或&nbsp;<code>a-z</code>&nbsp;。&nbsp;<code>.</code> 可以表示任何一个字母。</p>

<p><strong>示例:</strong></p>

<pre>addWord(&quot;bad&quot;)
addWord(&quot;dad&quot;)
addWord(&quot;mad&quot;)
search(&quot;pad&quot;) -&gt; false
search(&quot;bad&quot;) -&gt; true
search(&quot;.ad&quot;) -&gt; true
search(&quot;b..&quot;) -&gt; true
</pre>

<p><strong>说明:</strong></p>

<p>你可以假设所有单词都是由小写字母 <code>a-z</code>&nbsp;组成的。</p>


## 解法：

解法一：字典树

```cpp
class WordDictionary {
public:
    struct Node;
    struct Node{
        Node():tail(false){}
        bool tail;
        shared_ptr<Node> next['z'-'a'+1];
    };


    WordDictionary() {
        root = make_shared<Node>();
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        return dfs(root, word, 0);
    }

    /** Adds a word into the data structure. */
    void addWord(string word) {
        shared_ptr<Node> p = root;
        for(char ch : word){
            int index = ch - 'a';
            if(p->next[index] == nullptr){
                p->next[index] = make_shared<Node>();
            }
            p = p->next[index];
        }
        p->tail = true;
    }

private:
    bool dfs(shared_ptr<Node> node, const string &word, size_t i){
        if(i == word.size()){
            return node->tail;
        }

        char ch = word[i];
        if(ch == '.'){
            for(const auto& p: node->next){
                if(p != nullptr && dfs(p, word, i+1)){
                    return true;
                }
            }
            return false;
        }else{
            int index = ch - 'a';
            if(node->next[index] == nullptr){
                return false;
            }
            return dfs(node->next[index], word, i+1);
        }
    }

    shared_ptr<Node> root;
};
```