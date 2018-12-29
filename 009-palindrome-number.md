## 9. Palindrome Number


- 难度： 简单
- 通过率： 40.5%
- 题目链接：[https://leetcode.com/problems/palindrome-number](https://leetcode.com/problems/palindrome-number)



### 解法：

超级简单，根据题意负数不可能是回文数，把数字逆转过来，如果和原来的数相等，就是回文数。

```python
def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    x_copy = x
    x_reverse = 0
    while x:
        x_reverse = x_reverse * 10 + x % 10
        x = x // 10

    return x_reverse == x_copy
    
```