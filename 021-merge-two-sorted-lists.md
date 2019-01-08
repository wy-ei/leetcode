## 21. Merge Two Sorted Lists

- 难度： 简单
- 通过率： 44.7%
- 题目链接：[https://leetcode.com/problems/merge-two-sorted-lists](https://leetcode.com/problems/merge-two-sorted-lists)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>1-&gt;2-&gt;4, 1-&gt;3-&gt;4
<strong>输出：</strong>1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4
</pre>


### 解法：

本题很容易解答，其中一个技巧是创建一个 head，这样可以避免单独从 l1 和 l2 中找出头结点。

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0);
        p = head
        
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        
        if l1:
            p.next = l1
        else:
            p.next = l2
        
        return head.next
```