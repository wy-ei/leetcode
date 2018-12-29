## 8. String to Integer (atoi)


- 难度： 中等
- 通过率： 14.3%
- 题目链接：[https://leetcode.com/problems/string-to-integer-atoi](https://leetcode.com/problems/string-to-integer-atoi)



### 解法：

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