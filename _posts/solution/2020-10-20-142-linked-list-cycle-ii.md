---
title: 环形链表 II
qid: 142
tag: [链表, 双指针]
---

- 难度： 中等
- 通过率： 30.1%
- 题目链接：[https://leetcode-cn.com/problems/linked-list-cycle-ii](https://leetcode-cn.com/problems/linked-list-cycle-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个链表，返回链表开始入环的第一个节点。&nbsp;如果链表无环，则返回&nbsp;<code>null</code>。</p>

<p>为了表示给定链表中的环，我们使用整数 <code>pos</code> 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 <code>pos</code> 是 <code>-1</code>，则在该链表中没有环。</p>

<p><strong>说明：</strong>不允许修改给定的链表。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>head = [3,2,0,-4], pos = 1
<strong>输出：</strong>tail connects to node index 1
<strong>解释：</strong>链表中有一个环，其尾部连接到第二个节点。
</pre>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" style="height: 97px; width: 300px;"></p>

<p><strong>示例&nbsp;2：</strong></p>

<pre><strong>输入：</strong>head = [1,2], pos = 0
<strong>输出：</strong>tail connects to node index 0
<strong>解释：</strong>链表中有一个环，其尾部连接到第一个节点。
</pre>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 74px; width: 141px;"></p>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>head = [1], pos = -1
<strong>输出：</strong>no cycle
<strong>解释：</strong>链表中没有环。
</pre>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 45px; width: 45px;"></p>

<p>&nbsp;</p>

<p><strong>进阶：</strong><br>
你是否可以不用额外空间解决此题？</p>


## 解法：

思路：

- 链表是否有环
- 相交链表的交点

```c++
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(!head){
            return nullptr;
        }
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* joined_node = nullptr;
        while(fast->next && fast->next->next){
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow){
                joined_node = fast;
                break;
            }
        }
        // no circle
        if(!joined_node){
            return nullptr;
        }

        ListNode* p1 = head;
        ListNode* p2 = joined_node->next;
        while(p1 != p2){
            p1 = p1->next;
            p2 = (p2 == joined_node) ? head : p2->next;
        }
        return p1;
    }
};
```