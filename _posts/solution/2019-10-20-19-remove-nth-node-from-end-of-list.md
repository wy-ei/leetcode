---
title: 删除链表的倒数第N个节点
qid: 19
tags: [链表,双指针]
---


- 难度： 中等
- 通过率： 33.8%
- 题目链接：[https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个链表，删除链表的倒数第&nbsp;<em>n&nbsp;</em>个节点，并且返回链表的头结点。</p>

<p><strong>示例：</strong></p>

<pre>给定一个链表: <strong>1-&gt;2-&gt;3-&gt;4-&gt;5</strong>, 和 <strong><em>n</em> = 2</strong>.

当删除了倒数第二个节点后，链表变为 <strong>1-&gt;2-&gt;3-&gt;5</strong>.
</pre>

<p><strong>说明：</strong></p>

<p>给定的 <em>n</em>&nbsp;保证是有效的。</p>

<p><strong>进阶：</strong></p>

<p>你能尝试使用一趟扫描实现吗？</p>


## 解法：

快慢指针，先让快指针先走 n 步，然后慢指针开始出发，当快指针到达尾部的时候，慢指针就处于倒数第 n 个节点处。要删除节点 node，需要得到 node 前一个节点。因此，可以考虑让 fast 多走一步，但是如果要删除的实际上是头结点呢，所以增加一个伪结点是比较方便的做法。

```c++
class Solution {
public:
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode dummy(-1);
        dummy.next = head;
        ListNode *fast = &dummy, *slow = &dummy;
        for (int i = 0; i < n; i++) {
            fast = fast->next;
        }

        while (fast->next) {
            fast = fast->next;
            slow = slow->next;
        }

        ListNode *next = slow->next;
        slow->next = slow->next->next;
        delete next;
        return dummy.next;
    }
};
```