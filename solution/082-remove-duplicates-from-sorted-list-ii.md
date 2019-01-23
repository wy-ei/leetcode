## 82. Remove Duplicates from Sorted List II

- 难度： 中等
- 通过率： 31.7%
- 题目链接：[https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中&nbsp;<em>没有重复出现&nbsp;</em>的数字。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 1-&gt;2-&gt;3-&gt;3-&gt;4-&gt;4-&gt;5
<strong>输出:</strong> 1-&gt;2-&gt;5
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> 1-&gt;1-&gt;1-&gt;2-&gt;3
<strong>输出:</strong> 2-&gt;3</pre>


## 解法：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return head
        
        p = head
        ret = ListNode(0)
        q = ret
        count = 0

        while head:
            if p.val == head.val:
                count += 1
            else:
                if count == 1:
                    q.next = p
                    q = q.next
                    q.next = None

                p = head
                count = 1
                
            head = head.next
            
        if count == 1:
            q.next = p

        return ret.next        
```