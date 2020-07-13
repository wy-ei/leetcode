---
title: 复原IP地址
qid: 93
tags: [字符串,回溯算法]
---


- 难度： 中等
- 通过率： 30.2%
- 题目链接：[https://leetcode-cn.com/problems/restore-ip-addresses](https://leetcode-cn.com/problems/restore-ip-addresses)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> &quot;25525511135&quot;
<strong>输出:</strong> <code>[&quot;255.255.11.135&quot;, &quot;255.255.111.35&quot;]</code></pre>


## 解法：

此题使用递归来解答相当容易，每次从字符串前分别取 1,2,3 个字符，如果符合要求，就加入 `parts` 中，在余下的字符串中继续添加下一部分。当发现 `parts` 长度为 4，且没有剩余的字符时，将其加入到结果中。如果长度已经为 4，但余下字符尚不为空，说明 `parts` 中的解不对，因此要退出递归。当余下字符串不够长了，此时也退出。

整个字符串可以在多处断开，因此所有可能的分隔情况构成了一棵搜索树。这里采用了深度优先去搜索这棵树，在合适的条件下对树进行减枝。在搜索到符合要求的结果是，将其保存。

```python
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        vector<string> parts;
        dfs(s, 0, parts, result);
        return result;
    }

    void dfs(const string& s, size_t start, vector<string>& parts, vector<string>& result){
        if(start == s.size() && parts.size() == 4){
            result.push_back(parts[0] + '.' +parts[1] + '.' + parts[2] + '.' + parts[3]);
            return;
        }
        if(parts.size() == 4){
            return;
        }
        // 余下的字符串不够长了
        if(s.size() - start < (4 - parts.size())){
            return;
        }
        // 余下的字符串太长
        if(s.size() - start > (4 - parts.size()) * 3){
            return;
        }
        int num = 0;
        size_t end = min(start+3, s.size());
        for(size_t i = start; i < end; i++){
            num = num * 10 + (s[i] - '0');
            if(num > 255){
                continue;
            }

            parts.push_back(s.substr(start, i - start + 1));
            dfs(s, i + 1, parts, result);
            parts.pop_back();

            // '012' 跳过这样的
            // 当首字符为 0 时，后面的都不用再看了
            if(num == 0){
                break;
            }

        }
    }
};
```