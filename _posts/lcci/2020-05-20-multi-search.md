---
title: 多次搜索
qid: 17.17
tags: [字典树,字符串]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/multi-search-lcci/](https://leetcode-cn.com/problems/multi-search-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个较长字符串<code>big</code>和一个包含较短字符串的数组<code>smalls</code>，设计一个方法，根据<code>smalls</code>中的每一个较短字符串，对<code>big</code>进行搜索。输出<code>smalls</code>中的字符串在<code>big</code>里出现的所有位置<code>positions</code>，其中<code>positions[i]</code>为<code>smalls[i]</code>出现的所有位置。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
big = &quot;mississippi&quot;
smalls = [&quot;is&quot;,&quot;ppi&quot;,&quot;hi&quot;,&quot;sis&quot;,&quot;i&quot;,&quot;ssippi&quot;]
<strong>输出：</strong> [[1,4],[8],[],[3],[1,4,7,10],[5]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= len(big) &lt;= 1000</code></li>
	<li><code>0 &lt;= len(smalls[i]) &lt;= 1000</code></li>
	<li><code>smalls</code>的总字符数不会超过 100000。</li>
	<li>你可以认为<code>smalls</code>中没有重复字符串。</li>
	<li>所有出现的字符均为英文小写字母。</li>
</ul>


## 解法一：暴力搜索

```c++
class Solution {
public:
    vector<vector<int>> multiSearch(string big, vector<string>& smalls) {
        vector<vector<int>> ret;
        for(string& s: smalls){
            vector<int> positions;
            if(s.empty()){
                ret.push_back(::move(positions));
                continue;
            }
            int start = 0;
            int i = big.find(s, start);
            
            while(i != string::npos){
                positions.push_back(i);
                start = i + 1;
                i = big.find(s, start);
            }
            ret.push_back(::move(positions));
        }
        return ret;
    }
};
```

## 解法二：Trie

把所有短单词都存储在 Trie 中。然后使用 `big[i:]` 去 Trie 树中寻找 `big[i:]` 的前缀。 

