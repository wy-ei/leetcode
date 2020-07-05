---
title: 移除重复节点
qid: 02.01
tags: [链表]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/remove-duplicate-node-lcci/](https://leetcode-cn.com/problems/remove-duplicate-node-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。</p>

<p> <strong>示例1:</strong></p>

<pre>
<strong> 输入</strong>：[1, 2, 3, 3, 2, 1]
<strong> 输出</strong>：[1, 2, 3]
</pre>

<p> <strong>示例2:</strong></p>

<pre>
<strong> 输入</strong>：[1, 1, 1, 1, 2]
<strong> 输出</strong>：[1, 2]
</pre>

<p><strong>提示：</strong></p>

<ol>
<li>链表长度在[0, 20000]范围内。</li>
<li>链表元素在[0, 20000]范围内。</li>
</ol>

<p> <strong>进阶：</strong></p>

<p>如果不得使用临时缓冲区，该怎么解决？</p>


## 解法：

遍历链表，并使用集合记录下已经遇到过的节点，如果遇到重复的节点，就删除掉。

```c++
class Solution {
public:
    ListNode* removeDuplicateNodes(ListNode* head) {
        unordered_set<int> seen;
        ListNode *prev, *node;
        node = head;
        while(node != nullptr){
            if(seen.count(node->val) == 0){
                seen.insert(node->val);
                prev = node;
            }else{
                prev->next = node->next;
            }
            node = node->next;
        }
        return head;
    }
};
```