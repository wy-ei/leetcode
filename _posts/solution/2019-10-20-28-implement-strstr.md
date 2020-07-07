---
title: 实现 strStr()
qid: 28
tags: [双指针,字符串]
---


- 难度： 简单
- 通过率： 30.7%
- 题目链接：[https://leetcode-cn.com/problems/implement-strstr](https://leetcode-cn.com/problems/implement-strstr)


## 题目描述

<p>实现&nbsp;<a href="https://baike.baidu.com/item/strstr/811469" target="_blank">strStr()</a>&nbsp;函数。</p>

<p>给定一个&nbsp;haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回&nbsp; <strong>-1</strong>。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> haystack = &quot;hello&quot;, needle = &quot;ll&quot;
<strong>输出:</strong> 2
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> haystack = &quot;aaaaa&quot;, needle = &quot;bba&quot;
<strong>输出:</strong> -1
</pre>

<p><strong>说明:</strong></p>

<p>当&nbsp;<code>needle</code>&nbsp;是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。</p>

<p>对于本题而言，当&nbsp;<code>needle</code>&nbsp;是空字符串时我们应当返回 0 。这与C语言的&nbsp;<a href="https://baike.baidu.com/item/strstr/811469" target="_blank">strstr()</a>&nbsp;以及 Java的&nbsp;<a href="https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)" target="_blank">indexOf()</a>&nbsp;定义相符。</p>


## 解法：

面试中暴力解法就够了，本题最关键的是要细心。尤其是使用 C++ 来实现，存在很多坑。



```C++
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.size() < needle.size()) return -1;
        if (needle.empty()) return 0;

        const size_t N = haystack.size() - needle.size() + 1;
        for (size_t i = 0; i < N; i++) {
            int j = 0;
            while (j < needle.size() && needle[j] == haystack[i + j]) {
                j++;
            }
            if (j == needle.size()) return i;
        }
        return -1;
    }
};      
```


我第一次写出了下面这样的代码，出现了严重的 BUG。因为 `haystack` 可能比 `needle` 短，此时 `haystack.size() - needle.size()` 有可能会是负的，但是因为 `size` 返回的是无符号的数，因此发生了下溢。结果变成了一个非常大的正数。

```c++
for (size_t i = 0; i <= haystack.size() - needle.size(); i++){

}
```

