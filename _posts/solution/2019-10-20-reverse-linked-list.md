---
title: 反转链表
qid: 206
tags: [链表]
---


- 难度： 简单
- 通过率： 51.4%
- 题目链接：[https://leetcode-cn.com/problems/reverse-linked-list](https://leetcode-cn.com/problems/reverse-linked-list)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>反转一个单链表。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL
<strong>输出:</strong> 5-&gt;4-&gt;3-&gt;2-&gt;1-&gt;NULL</pre>

<p><strong>进阶:</strong><br>
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？</p>


## 解法：

把链表节点以此插到新链表的头部即可。

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *p = head;
        ListNode *next;        
        head = nullptr;
        while(p){
            next = p->next;
            p->next = head;
            head = p;
            p = next;
        }
        return head;
    }
};
```