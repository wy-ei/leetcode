## 6. ZigZag Conversion


- 难度： 中等
- 通过率： 29.8%
- 题目链接：[https://leetcode.com/problems/zigzag-conversion](https://leetcode.com/problems/zigzag-conversion)


### 解法 1

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

### 解法 2

如果仔细分析每一行的各个字符在字符串中的下标，是能够发现规律的。这里不再尝试该方法了。详见[Solution](https://leetcode.com/problems/zigzag-conversion/solution/)。