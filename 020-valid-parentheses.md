## 20. Valid Parentheses


- 难度： 简单
- 通过率： 35.3%
- 题目链接：[https://leetcode.com/problems/valid-parentheses](https://leetcode.com/problems/valid-parentheses)



### 解法：

使用栈很容易解决，需要注意的是在 `pop` 的时候需要检查栈是否为空。

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = {'(', '[', '{'}
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in start:
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != mapping[c]:
                return False
        return len(stack) == 0
```