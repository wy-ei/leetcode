---
title: 实现 Trie (前缀树)
qid: 208
tags: [设计,字典树]
---


- 难度： 中等
- 通过率： 35.6%
- 题目链接：[https://leetcode-cn.com/problems/implement-trie-prefix-tree](https://leetcode-cn.com/problems/implement-trie-prefix-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>实现一个 Trie (前缀树)，包含&nbsp;<code>insert</code>,&nbsp;<code>search</code>, 和&nbsp;<code>startsWith</code>&nbsp;这三个操作。</p>

<p><strong>示例:</strong></p>

<pre>Trie trie = new Trie();

trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // 返回 true
trie.search(&quot;app&quot;);     // 返回 false
trie.startsWith(&quot;app&quot;); // 返回 true
trie.insert(&quot;app&quot;);   
trie.search(&quot;app&quot;);     // 返回 true</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>你可以假设所有的输入都是由小写字母&nbsp;<code>a-z</code>&nbsp;构成的。</li>
	<li>保证所有输入均为非空字符串。</li>
</ul>


## 解法：


前缀树，没什么好说的。这里使用了智能指针，性能稍稍受损。像树这样的结构，还是使用普通指针比较好。只需要在析构函数中释放内存即可。

```cpp
class Trie {
public:
    struct Node;
    struct Node{
        Node():tail(false){}
        bool tail;
        shared_ptr<Node> next['z'-'a'+1];
    };


    /** Initialize your data structure here. */
    Trie() {
        root = make_shared<Node>();
    }

    /** Inserts a word into the trie. */
    void insert(string word) {
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

    /** Returns if the word is in the trie. */
    bool search(string word) {
        shared_ptr<Node> p = root;
        for(char ch : word){
            int index = ch - 'a';
            if(p->next[index] == nullptr){
                return false;
            }
            p = p->next[index];
        }
        return p->tail;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        shared_ptr<Node> p = root;
        for(char ch : prefix){
            int index = ch - 'a';
            if(p->next[index] == nullptr){
                return false;
            }
            p = p->next[index];
        }
        return true;
    }

private:
    shared_ptr<Node> root;
};
```