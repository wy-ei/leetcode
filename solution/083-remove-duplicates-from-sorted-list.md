## 83. Remove Duplicates from Sorted List

- 难度： 简单
- 通过率： 41.5%
- 题目链接：[https://leetcode.com/problems/remove-duplicates-from-sorted-list](https://leetcode.com/problems/remove-duplicates-from-sorted-list)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 1-&gt;1-&gt;2
<strong>输出:</strong> 1-&gt;2
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;3
<strong>输出:</strong> 1-&gt;2-&gt;3</pre>


## 解法：

## 解法 1

当前节点的值 `p.val` 如果等于后一个节点的值，这就出现了重复，此时可令 `p.next = p.next.next`，这样便跳过了后一个重复的节点。

如果当前节点的值 `p.val` 不等于后一个节点的值，那就用 p 指向后一个节点。

这个方法只需要一个指针 `p` 即可，代码很清晰。

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
        
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        
        return head
```

## 解法 2

这个方法就是使用两个指针，`cur` 用来遍历链表，`pre` 用来指向结果链表的尾部。当 `pre.val != cur.val` 时，将 `cur` 接到 `pre` 后面，然后将 `pre` 后移。

需要注意的一点是，`pre.next = cur` 这意味着从 `pre` 开始可以遍历到原链表的结尾。

比如下面的例子，遍历完了之后 `pre` 后面跟着一大串值重复的节点。 

```
1 2 3 4 4 4 4 4 4 None
      ^            ^
     pre          cur
```

因此需要在遍历结束后，将 `pre.next` 置为 `None` 以断开链表。

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
        
        while cur:
            if cur.val != pre.val:
                pre.next = cur
                pre = pre.next

            cur = cur.next
            
        pre.next = None
        
        return head
```