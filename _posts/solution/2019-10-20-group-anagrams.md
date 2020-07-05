---
title: 字母异位词分组
qid: 49
tags: [哈希表,字符串]
---


- 难度： 中等
- 通过率： 43.4%
- 题目链接：[https://leetcode.com/problems/group-anagrams](https://leetcode.com/problems/group-anagrams)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> <code>[&quot;eat&quot;, &quot;tea&quot;, &quot;tan&quot;, &quot;ate&quot;, &quot;nat&quot;, &quot;bat&quot;]</code>,
<strong>输出:</strong>
[
  [&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;],
  [&quot;nat&quot;,&quot;tan&quot;],
  [&quot;bat&quot;]
]</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>所有输入均为小写字母。</li>
	<li>不考虑答案输出的顺序。</li>
</ul>


## 解法：

这个题的重点是找到一种办法，把字母组成相同的单词，编码成一个相同的 `key`，然后将通过一个 `map` 把这些单词存在同一个数组中。

我太欠缺这种经验了，考虑到字母只有 `a-z` 这 26 个，可以使用一个长度为 26 的数组，用来保存各个字符在单词中出现的次数。这样以来字母组成相同的单词得到的这个数组就是相同的。

把这个数组转换为 tuple 或者字符串，作为 `map` 的减值，此问题就能够解决了。

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        ord_a = ord('a')

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord_a] += 1
            
            ans[tuple(count)].append(s)
            
            
        return list(ans.values())
```