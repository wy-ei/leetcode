---
title: 无重复字符串的排列组合
qid: 08.07
tags: [回溯算法]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/permutation-i-lcci/](https://leetcode-cn.com/problems/permutation-i-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。</p>

<p> <strong>示例1:</strong></p>

<pre>
<strong> 输入</strong>：S = "qwe"
<strong> 输出</strong>：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
</pre>

<p> <strong>示例2:</strong></p>

<pre>
<strong> 输入</strong>：S = "ab"
<strong> 输出</strong>：["ab", "ba"]
</pre>

<p> <strong>提示:</strong></p>

<ol>
<li>字符都是英文字母。</li>
<li>字符串长度在[1, 9]之间。</li>
</ol>


## 解法一：迭代


考虑字符集合`{a,b,c}`，首先取一个字符 `a` 构成字符串 `a`，然后在取一个字符，在先前构成的字符串的各个位置插入 `b`，就可以得到新的字符串。
同理，在前一步生成的各个字符串的各个位置插入字符 `c`，又可以得到大量新的字符串。


```
a

ab
ba

cab
acb
abc
cba
bca
bac
```

基于以上分析，可以写出如下代码：

```c++
class Solution {
public:
    vector<string> permutation(string s) {
        vector<string> result;
        result.push_back("");

        for(char ch: s){
            vector<string> new_result;
            for(const string& perm: result){
                for(int i = 0; i <= perm.size(); i++){
                    string next_perm = perm;
                    next_perm.insert(i, 1, ch);
                    new_result.push_back(std::move(next_perm));
                }
            }
            result = std::move(new_result);
        }
        return result;
    }
};
```


## 解法二：回溯法

采用回溯法，首先可以在所有字符中选择一个作为第一个字符，然后余下的字符中选择第二个，...直到没得选，这样就得到了一个排列组合了。

```c++
class Solution {
public:
    vector<string> permutation(string s) {
        vector<string> result;
        vector<bool> visited(s.size(), false);
        string path;
        dfs(path, s, visited, result);
        return result;
    }

    void dfs(string& path, const string &s, vector<bool>& visited, vector<string>& result){
        if(path.size() == s.size()){
            result.push_back(path);
            return;
        }
        
        for(int i = 0; i < s.size(); i++){
            if(visited[i]){
                continue;
            }
            visited[i] = true;
            path += s[i];
            dfs(path, s, visited, result);
            visited[i] = false;
            path.pop_back();
        }
    }
};
```

## 解法三：下一个排列组合

先排序，让字符串中各个字符呈现升序排列。然后不断调用 `next_permutation`，得到所有的组合。关于 `next_permutation` 的详细解释可以参考 {% include post_link qid="31" %}。


```c++
class Solution {
public:
    vector<string> permutation(string s) {
        vector<string> ret;        
        sort(s.begin(), s.end());
        ret.push_back(s);
        while(next_permutation(s)){
            ret.push_back(s);
        }
        return ret;
    }

    bool next_permutation(string& s){
        int i = s.size() - 2;
        while(i >= 0 && s[i] >= s[i+1]){
            i--;
        }
        if(i < 0){
            return false;
        }
        int j = s.size() - 1;
        while(j >= 0 && s[j] <= s[i]){
            j--;
        }
        ::swap(s[i], s[j]);
        reverse(s.begin()+i+1, s.end());
        return true;
    }
};
```
