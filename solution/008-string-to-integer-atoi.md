## 8. String to Integer (atoi)

- 难度： 中等
- 通过率： 14.3%
- 题目链接：[https://leetcode.com/problems/string-to-integer-atoi](https://leetcode.com/problems/string-to-integer-atoi)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>请你来实现一个&nbsp;<code>atoi</code>&nbsp;函数，使其能将字符串转换成整数。</p>

<p>首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。</p>

<p>当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。</p>

<p>该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。</p>

<p>注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。</p>

<p>在任何情况下，若函数不能进行有效的转换时，请返回 0。</p>

<p><strong>说明：</strong></p>

<p>假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为&nbsp;[&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]。如果数值超过这个范围，qing返回 &nbsp;INT_MAX (2<sup>31&nbsp;</sup>&minus; 1) 或&nbsp;INT_MIN (&minus;2<sup>31</sup>) 。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> &quot;42&quot;
<strong>输出:</strong> 42
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> &quot;   -42&quot;
<strong>输出:</strong> -42
<strong>解释: </strong>第一个非空白字符为 &#39;-&#39;, 它是一个负号。
&nbsp;    我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong> &quot;4193 with words&quot;
<strong>输出:</strong> 4193
<strong>解释:</strong> 转换截止于数字 &#39;3&#39; ，因为它的下一个字符不为数字。
</pre>

<p><strong>示例&nbsp;4:</strong></p>

<pre><strong>输入:</strong> &quot;words and 987&quot;
<strong>输出:</strong> 0
<strong>解释:</strong> 第一个非空字符是 &#39;w&#39;, 但它不是数字或正、负号。
     因此无法执行有效的转换。</pre>

<p><strong>示例&nbsp;5:</strong></p>

<pre><strong>输入:</strong> &quot;-91283472332&quot;
<strong>输出:</strong> -2147483648
<strong>解释:</strong> 数字 &quot;-91283472332&quot; 超过 32 位有符号整数范围。 
&nbsp;    因此返回 INT_MIN (&minus;2<sup>31</sup>) 。
</pre>


## 解法：

思路如下：

1. 跳过空格，使用 while 循环跳过空格
2. 检查符号，即 `-` 和 `+`，使用 if 语句判断
3. 处理数字，使用 while 循环，如果不是数字就结束

当输入是空串或者全部是空白的字符串时，为了避免发生越界错误，需要判断 `i` 是否在范围内，可以在字符串尾巴上加一个哨兵字符。

```python
def atoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    sign = 1
    x = 0
    str += '#'  # guard        
    i = 0

    while str[i].isspace():
        i += 1

    if str[i] == '-':
        sign = -1
        i += 1
    elif str[i] == '+':
        i += 1

    while str[i].isdigit():
        x = x * 10 + int(str[i])
        i += 1

    x *= sign

    if x < -2 ** 31:
        return -2 ** 31

    if x > 2 ** 31 - 1:
        return 2 ** 31 - 1

    return x
```

用 C++ 解：

```cpp
int myAtoi(string str) {
    int n = 0;
    auto it = str.begin();
    while(isblank(*it)){
        ++it;
    }
    int sign = 1;

    if(*it == '+' || *it == '-'){
        if(*it == '-'){
            sign = -1;
        }
        ++it;
    }


    int int_min = numeric_limits<int>::min();
    int int_max = numeric_limits<int>::max();

    while(isdigit(*it) && it != str.end()){
        int m = sign * (*it - '0');

        if(sign == 1){
            if((int_max / 10 < n) || (int_max / 10 == n && int_max % 10 <= m)){
                return int_max;
            }
        }else{
            if((int_min / 10 > n) || (int_min / 10 == n && int_min % 10 >= m)){
                return int_min;
            }
        }

        n = n * 10 + m;
        ++it;
    }

    return n;
}
```