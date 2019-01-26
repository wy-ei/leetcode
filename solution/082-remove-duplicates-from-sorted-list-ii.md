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

对重复节点进行计数，使用 `pre` 指向具有相同值得节点中的第一个，`cur` 以此遍历链表，同时和 `pre` 的值比较，值相同的 `count += 1`，不相同的时候判断 `count` 是不是 1，如果是 1，就将 `pre` 加入结果中。

在遍历结束后，`pre` 节点因为还没有遇到下一个值不同的节点，所以还没有做处理（插入结果链表中，或是抛弃），这个时候只需要判断 `count` 的值是否为 1 即可。

当 `count == 1` 时，将 `pre` 接到结果中，此时 `pre` 定为原链表中最后一个节点。

当 `count != 1` 时，`pre` 及其后面的节点需要被抛弃，此时结果链表的结尾，即 `p.next` 还连接在原链表的某个部分，因此需要断开，设置 `p.next = None`。

Tips：当不确定 `head` 中第一个元素会不会出现在结果链表中时，创建一个超头节点是很方便的事情。

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
        
        pre = head
        cur = head.next
        
        ret = ListNode(0)
        p = ret
        
        count = 1
        while cur:
            if pre.val == cur.val:
                count += 1
            else:
                if count == 1:
                    p.next = pre
                    p = pre

                pre = cur
                count = 1
                
            cur = cur.next
            
        if count == 1:
            p.next = pre
        else:
            p.next = None

        return ret.next   
```