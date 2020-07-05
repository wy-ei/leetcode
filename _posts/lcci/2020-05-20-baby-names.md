---
title: 婴儿名字
qid: 17.07
tags: [深度优先搜索,广度优先搜索,并查集]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/baby-names-lcci/](https://leetcode-cn.com/problems/baby-names-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。</p>

<p>在结果列表中，选择<strong>字典序最小</strong>的名字作为真实名字。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>names = [&quot;John(15)&quot;,&quot;Jon(12)&quot;,&quot;Chris(13)&quot;,&quot;Kris(4)&quot;,&quot;Christopher(19)&quot;], synonyms = [&quot;(Jon,John)&quot;,&quot;(John,Johnny)&quot;,&quot;(Chris,Kris)&quot;,&quot;(Chris,Christopher)&quot;]
<strong>输出：</strong>[&quot;John(27)&quot;,&quot;Chris(36)&quot;]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>names.length &lt;= 100000</code></li>
</ul>


## 解法：

使用 union find（并查集）即可。

```c++
class union_find{
public:
    union_find():id(0){}
    void connect(const string& s1, const string& s2){
        const string& s1_root = find(s1);
        const string& s2_root = find(s2);

        if(s1_root == s2_root){
            return;
        }

        int id1 = str_to_id[s1_root];
        int id2 = str_to_id[s2_root];
        if(s1_root < s2_root){
            mp[id2] = id1;
        }else{
            mp[id1] = id2;
        }
    }

    const string& find(const string& s){
        add_word_if_non_exist(s);
        int sid = str_to_id[s];
        if(mp.find(sid) == mp.end()){
            mp[sid] = sid;
        }
        
        while(mp[sid] != sid){
            mp[sid] = mp[mp[sid]];
            sid = mp[sid];
        }
        return id_to_str[sid];
    }
private:
    void add_word_if_non_exist(const string& s){
        if(str_to_id.find(s) == str_to_id.end()){
            str_to_id[s] = id;
            id_to_str[id] = s;
            id++;
        }
    }

    unordered_map<int, int> mp;
    unordered_map<string, int> str_to_id;
    unordered_map<int, string> id_to_str;
    int id;
};

class Solution {
public:
    vector<string> trulyMostPopular(vector<string>& names, vector<string>& synonyms) {
        union_find uf;
        for(string& s: synonyms){
            int i = s.find(',');
            string s1 = s.substr(1, i - 1);
            string s2 = s.substr(i+1, s.size() - i - 2);
            uf.connect(s1, s2);
        }

        unordered_map<string, int> mp;
        for(string& s: names){
            int i = s.find('(');
            string name = s.substr(0, i);
            string num = s.substr(i+1, s.size() - 2 - i);
            int n = stoi(num);
            mp[uf.find(name)] += n;
        }

        vector<string> ret;
        for(auto& item: mp){
            string s = item.first;
            s += '(';
            s += to_string(item.second);
            s += ')';
            ret.push_back(s);
        }

        return ret;
    }
};
```