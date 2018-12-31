## 24. Swap Nodes in Pairs


- 难度： 中等
- 通过率： 42.1%
- 题目链接：[https://leetcode.com/problems/swap-nodes-in-pairs](https://leetcode.com/problems/swap-nodes-in-pairs)



### 解法：

一开始考虑到没有 pre 结点，在循环中加了不少判断，代码写的很长。后来看了看别人的代码，发现可以自己创建一个 pre 节点，一下就把问题简化了。
在 while 循环中给 `pre.next`, `pre.next.next` 起名字 `cur`，`_next` 可以让逻辑更清晰一些。

返回的头结点是交换后的头结点，但这个头结点一定是开始创建的 `pre.next`，在 `while` 循环执行第一次未更新 pre 的时候，`pre.next` 就是返回值。所以只需要使用一个变量将 `pre` 记录下来即可。

真是太聪明了。

使用 `_next` 是因为 `next` 是 Python 中的关键字。

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre_copy = pre
        pre.next = head
        
        while pre.next and pre.next.next:
            cur = pre.next
            _next = cur.next
            
            pre.next = _next
            cur.next = _next.next
            _next.next = cur
            
            pre = cur

        return pre_copy.next
```