## 38. Count and Say

- 难度： 简单
- 通过率： 38.8%
- 题目链接：[https://leetcode.com/problems/count-and-say](https://leetcode.com/problems/count-and-say)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：</p>

<pre>1.     1
2.     11
3.     21
4.     1211
5.     111221
</pre>

<p><code>1</code>&nbsp;被读作&nbsp;&nbsp;<code>&quot;one 1&quot;</code>&nbsp;&nbsp;(<code>&quot;一个一&quot;</code>) , 即&nbsp;<code>11</code>。<br>
<code>11</code> 被读作&nbsp;<code>&quot;two 1s&quot;</code>&nbsp;(<code>&quot;两个一&quot;</code>）, 即&nbsp;<code>21</code>。<br>
<code>21</code> 被读作&nbsp;<code>&quot;one 2&quot;</code>, &nbsp;&quot;<code>one 1&quot;</code>&nbsp;（<code>&quot;一个二&quot;</code>&nbsp;,&nbsp;&nbsp;<code>&quot;一个一&quot;</code>)&nbsp;, 即&nbsp;<code>1211</code>。</p>

<p>给定一个正整数 <em>n</em>（1 &le;&nbsp;<em>n</em>&nbsp;&le; 30），输出报数序列的第 <em>n</em> 项。</p>

<p>注意：整数顺序将表示为一个字符串。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 1
<strong>输出:</strong> &quot;1&quot;
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> 4
<strong>输出:</strong> &quot;1211&quot;
</pre>


## 解法：

```c++
class Solution {
public:
    string countAndSay(int n) {
        string s = "1";
        while(--n){
            s = next(s);
        }
        return s;
    }

    string next(const string& s){
        string t;
        for(auto i = s.begin(); i != s.end();){
            auto j = find_if(i, s.end(), bind(not_equal_to<>(), placeholders::_1, *i));
            t.push_back(distance(i, j) + '0');
            t.push_back(*i);
            i = j;
        }
        return t;
    }
};
```