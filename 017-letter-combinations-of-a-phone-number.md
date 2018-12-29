## 17. Letter Combinations of a Phone Number


- 难度： 中等
- 通过率： 39.4%
- 题目链接：[https://leetcode.com/problems/letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)



### 解法一：

使用深度优先遍历

```python
class Solution:
    digits_map = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def dfs(self, digits, prefix, depth, result):
        digit = digits[depth]
        for c in self.digits_map[digit]:
            if depth < len(digits) - 1:
                self.dfs(digits, prefix + c, depth+1, result)
            else:
                result.append(prefix + c)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        digits = list(digits)

        result = []
        self.dfs(digits, '', 0, result)
        return result
```

### 解法二

使用递归

```python
class Solution:
    digits_map = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.digits_map[digits[0]])
        
        combinations = []
        for item in self.letterCombinations(digits[1:]):
            for letter in self.digits_map[digits[0]]:
                combinations.append(letter + item)
        return combinations
```