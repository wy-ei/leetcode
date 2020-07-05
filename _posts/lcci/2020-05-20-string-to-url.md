---
title: URL化
qid: 01.03
tags: [字符串]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/string-to-url-lcci/](https://leetcode-cn.com/problems/string-to-url-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>URL化。编写一种方法，将字符串中的空格全部替换为<code>%20</code>。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的&ldquo;真实&rdquo;长度。（注：用<code>Java</code>实现的话，请使用字符数组实现，以便直接在数组上操作。）</p>

<p><strong>示例1:</strong></p>

<pre><strong> 输入</strong>：&quot;Mr John Smith    &quot;, 13
<strong> 输出</strong>：&quot;Mr%20John%20Smith&quot;
</pre>

<p><strong>示例2:</strong></p>

<pre><strong> 输入</strong>：&quot;               &quot;, 5
<strong> 输出</strong>：&quot;%20%20%20%20%20&quot;
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>字符串长度在[0, 500000]范围内。</li>
</ol>


## 解法：

原意可能是原地修改，但是需要保证输入的字符串尾部有多余的空间，在很多编程语言中，字符串扩容会引起内存的复制。因此，不如直接得到新的字符串。


```c++
class Solution {
public:
    string replaceSpaces(string s, int length) {
        string result;
        for(int i=0;i<length;i++){
            if(s[i] != ' '){
                result.push_back(s[i]);
            }else{
                result += "%20";
            }
        }
        return result;
    }
};
```