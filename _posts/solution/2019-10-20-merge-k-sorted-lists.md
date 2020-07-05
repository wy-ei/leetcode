---
title: 合并K个排序链表
qid: 23
tags: [堆,链表,分治算法]
---


- 难度： 困难
- 通过率： 31.9%
- 题目链接：[https://leetcode.com/problems/merge-k-sorted-lists](https://leetcode.com/problems/merge-k-sorted-lists)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>合并&nbsp;<em>k&nbsp;</em>个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong>
[
&nbsp; 1-&gt;4-&gt;5,
&nbsp; 1-&gt;3-&gt;4,
&nbsp; 2-&gt;6
]
<strong>输出:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6</pre>


## 解法：

使用一个优先队列来存储链表的头结点，这样就可以很方便地取到值最小的节点了。取出值最小的节点后，如果它的下一个节点不为空，再加入到优先队列中。当优先队列为空时，就合并完成了。

```c++
class Solution {
public:
    ListNode *mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty()) return nullptr;
        auto cmp = [](ListNode *a, ListNode *b) {
            return a->val > b->val;
        };
        priority_queue<ListNode *, vector<ListNode *>, decltype(cmp)> pq(cmp);
        for_each(lists.begin(), lists.end(), [&pq](ListNode *node) {
            if(node){
                pq.push(node);
            }
        });

        ListNode dummy(0);
        ListNode *p = &dummy;
        while (!pq.empty()) {
            ListNode *node = pq.top();
            pq.pop();

            p->next = node;
            p = p->next;
            node = node->next;

            if (node) {
                pq.push(node);
            }
        }
        return dummy.next;
    }
};
```