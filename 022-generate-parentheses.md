## 22. Generate Parentheses


- 难度： 中等
- 通过率： 51.8%
- 题目链接：[https://leetcode.com/problems/generate-parentheses](https://leetcode.com/problems/generate-parentheses)



### 解法：

想了好久没想出来，看了看答案，看到了这个解法。

用一个空字符串，先尝试添加左括号，再添加右括号，利用递归的写法，会优先尝试添加左括号，而后尝试添加右括号，得出的答案符合题目要求。

这个解法可以看做是一种深度优先的搜索，只是在搜索过程中有某些限制条件，即每经过一个左括号，之后可以经过一个右括号。所以需要在搜索的过程中记录下剩余的左括号数，以及当前为封闭的左括号数。


```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.__generateParenthesis(n, 0, '', results)
        return results

    def __generateParenthesis(self, left_remained, left_opened, s, results):
        if left_remained == 0 and left_opened == 0:
            results.append(s)
            return

        if left_remained > 0:
            self.__generateParenthesis(left_remained - 1, left_opened + 1, '(' + s, results)

        if left_opened > 0:
            self.__generateParenthesis(left_remained, left_opened - 1, s + ')', results)
```