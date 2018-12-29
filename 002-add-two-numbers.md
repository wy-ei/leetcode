## 2. Add Two Numbers


- 难度： 中等
- 通过率： 29.9%
- 题目链接：[https://leetcode.com/problems/add-two-numbers](https://leetcode.com/problems/add-two-numbers)



### 解法：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = []
        carry = 0
        while l1 or l2:
            sum_ = carry
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            carry = sum_ // 10
            ret.append(sum_ % 10)

        if carry > 0:
            ret.append(carry)
        return ret
```