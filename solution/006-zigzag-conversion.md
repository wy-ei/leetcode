## 6. ZigZag Conversion

- 难度： 中等
- 通过率： 29.8%
- 题目链接：[https://leetcode.com/problems/zigzag-conversion](https://leetcode.com/problems/zigzag-conversion)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>将一个给定字符串根据给定的行数，以从上往下、从左到右进行&nbsp;Z 字形排列。</p>

<p>比如输入字符串为 <code>&quot;LEETCODEISHIRING&quot;</code>&nbsp;行数为 3 时，排列如下：</p>

<pre>L   C   I   R
E T O E S I I G
E   D   H   N
</pre>

<p>之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：<code>&quot;LCIRETOESIIGEDHN&quot;</code>。</p>

<p>请你实现这个将字符串进行指定行数变换的函数：</p>

<pre>string convert(string s, int numRows);</pre>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> s = &quot;LEETCODEISHIRING&quot;, numRows = 3
<strong>输出:</strong> &quot;LCIRETOESIIGEDHN&quot;
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> s = &quot;LEETCODEISHIRING&quot;, numRows =&nbsp;4
<strong>输出:</strong>&nbsp;&quot;LDREOEIIECIHNTSG&quot;
<strong>解释:</strong>

L     D     R
E   O E   I I
E C   I H   N
T     S     G</pre>



## 解法 1

顺序地遍历每个字符，然后判断该字符应该放在哪一行。可以在迭代的过程中维护一个行指针，该指针用于指出当前字符应该放在哪一行。这个指针在 0 到 `num_rows` 之间往返。

```python
class Solution:
    def convert(self, s, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if num_rows == 1:
            return s

        rows = [''] * num_rows
        row_index = 0
        direction = 1

        for c in s:
            rows[row_index] += c

            if row_index == num_rows - 1:
                direction = -1
            elif row_index == 0:
                direction = 1

            row_index += direction

        return ''.join(rows)
```

## 解法 2

如果仔细分析每一行的各个字符在字符串中的下标，是能够发现规律的。这里不再尝试该方法了。详见[Solution](https://leetcode.com/problems/zigzag-conversion/solution/)。