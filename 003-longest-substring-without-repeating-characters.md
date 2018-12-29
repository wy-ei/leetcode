## 3. Longest Substring Without Repeating Characters


- 难度： 中等
- 通过率： 25.7%
- 题目链接：[https://leetcode.com/problems/longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)



### 解法：

使用 `substring_start_index` 始终指向子字符串的开头，在一个 `map` 中记录各个字符出现的索引，如果在 `map` 中发现之前出现过的字符，那么子字符串的起始位置就应该调整到前面那个重复的字符处，因为子字符串不可能包含那个重复的字符。最长的子字符串只能出现在非重复的字符出现的时候。

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_length = 0
        substring_start_index = -1

        for i, c in enumerate(s):
            if c in char_map and char_map[c] > substring_start_index:
                substring_start_index = char_map[c]
                char_map[c] = i
            else:
                char_map[c] = i
                if i - substring_start_index > max_length:
                    max_length = i - substring_start_index

        return max_length
```

