## 93. Restore IP Addresses

- 难度： 中等
- 通过率： 30.2%
- 题目链接：[https://leetcode.com/problems/restore-ip-addresses](https://leetcode.com/problems/restore-ip-addresses)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> &quot;25525511135&quot;
<strong>输出:</strong> <code>[&quot;255.255.11.135&quot;, &quot;255.255.111.35&quot;]</code></pre>


## 解法：

此题使用递归来解答相当容易，每次从字符串前分别取 1,2,3 个字符，如果符合要求，就加入当前的 `ip_parts` 中，再在余下的字符中，找 ip 的下一部分。当发现 `ip_parts` 长度为 4，且没有剩余的字符时，将其加入到结果中。如果长度已经为 4，但余下字符尚不为空，说明 `ip_parts` 中的解不对，因此要退出递归。无论何时，当 `s` 为空，就不再递归。

```python
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []

        self.__restoreIpAddresses(s, [], results)

        return results
    
    def __restoreIpAddresses(self, s, ip_parts, results):
        if len(ip_parts) == 4 and not s:
            results.append('.'.join(ip_parts))
            return

        if len(ip_parts) == 4 or not s:
            return
        
        for length in range(1, min(3, len(s)) + 1):
            part = s[0:length]

            if length > 1 and part[0] == '0':
                return
            
            if length == 3 and int(part) > 255:
                return

            self.__restoreIpAddresses(s[length:], ip_parts + [part], results)
```