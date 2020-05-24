## 38. 字符串的排列

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>输入一个字符串，打印出该字符串中字符的所有排列。</p>

<p>&nbsp;</p>

<p>你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入：</strong>s = &quot;abc&quot;
<strong>输出：[</strong>&quot;abc&quot;,&quot;acb&quot;,&quot;bac&quot;,&quot;bca&quot;,&quot;cab&quot;,&quot;cba&quot;<strong>]</strong>
</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>1 &lt;= s 的长度 &lt;= 8</code></p>


## 解法：

先排序，让字符串中各个字符呈现升序排列。然后不断调用 `next_permutation`，得到所有的组合。

关于 `next_permutation` 可以参考 leetcode 31 题。


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