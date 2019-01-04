## 17. Letter Combinations of a Phone Number

- 难度： 中等
- 通过率： 39.5%
- 题目链接：[https://leetcode.com/problems/letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个仅包含数字&nbsp;<code>2-9</code>&nbsp;的字符串，返回所有它能表示的字母组合。</p>

<p>给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。</p>

<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png"></p>

<p><strong>示例:</strong></p>

<pre><strong>输入：</strong>&quot;23&quot;
<strong>输出：</strong>[&quot;ad&quot;, &quot;ae&quot;, &quot;af&quot;, &quot;bd&quot;, &quot;be&quot;, &quot;bf&quot;, &quot;cd&quot;, &quot;ce&quot;, &quot;cf&quot;].
</pre>

<p><strong>说明:</strong><br>
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。</p>



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