---
title: 两两交换链表中的节点
qid: 24
tags: [链表]
---


- 难度： 中等
- 通过率： 42.1%
- 题目链接：[https://leetcode-cn.com/problems/swap-nodes-in-pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。</p>

<p><strong>示例:</strong></p>

<pre>给定 <code>1-&gt;2-&gt;3-&gt;4</code>, 你应该返回 <code>2-&gt;1-&gt;4-&gt;3</code>.</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>你的算法只能使用常数的额外空间。</li>
	<li><strong>你不能只是单纯的改变节点内部的值</strong>，而是需要实际的进行节点交换。</li>
</ul>


## 解法一

使用栈。这个方法可以解决，k 个一组进行翻转的问题。

```c++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0);
        ListNode* q = &dummy;
        stack<ListNode*> stk;
        for(head != nullptr; head = head->next){
            stk.push(head);
            if(stk.size() == 2){
                while(!stk.empty()){
                    ListNode* node = stk.top();
                    stk.pop();
                    q->next = node;
                    q = q->next;
                }
            }
        }
        if(!stk.empty()){
            q->next = stk.top();
            q = q->next;
        }
        q->next = nullptr;  // 这个非常非常重要，如果不设置最后一个节点的 next 为 nullptr，链表就会出现环。
        return dummy.next;
    }
};
```

## 方法二：

使用递归:

```c++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(!head){
            return nullptr;
        }
        if(!head->next){
            return head;
        }
        ListNode* next = head->next;
        head->next = swapPairs(next->next);
        next->next = head;
        return next;
    }
};
```

## 解法三

```c++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0);
        ListNode* pre = &dummy;
        pre->next = head;

        while(pre->next && pre->next->next){
            ListNode* curr = pre->next;
            ListNode* next = curr->next;

            pre->next = next;
            curr->next = next->next;
            next->next = curr;

            pre = curr;
        }
        return dummy.next;
    }
};
```