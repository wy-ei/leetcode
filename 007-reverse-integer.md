## 7. Reverse Integer


- 难度： 简单
- 通过率： 24.8%
- 题目链接：[https://leetcode.com/problems/reverse-integer](https://leetcode.com/problems/reverse-integer)



### 解法

这题很容易，需要注意的是负数取余在 Python 中和 C 语言不同。为了避免出错，不妨转换为正数后处理。

```python
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_32_MIN = - 2**31
        INT_32_MAX = 2**31

        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        x_reverse = 0.0
        while x > 0:
            x_reverse = x_reverse * 10 + x % 10
            x = x // 10
            
        x_reverse *= sign
        
        if x_reverse < INT_32_MIN or x_reverse > INT_32_MAX:
            return 0

        return int(x_reverse)
```
