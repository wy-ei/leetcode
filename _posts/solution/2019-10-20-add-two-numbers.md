---
title: 两数相加
qid: 2
tags: [链表,数学]
---


- 难度： 中等
- 通过率： 30.0%
- 题目链接：[https://leetcode-cn.com/problems/add-two-numbers](https://leetcode-cn.com/problems/add-two-numbers)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给出两个&nbsp;<strong>非空</strong> 的链表用来表示两个非负的整数。其中，它们各自的位数是按照&nbsp;<strong>逆序</strong>&nbsp;的方式存储的，并且它们的每个节点只能存储&nbsp;<strong>一位</strong>&nbsp;数字。</p>

<p>如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。</p>

<p>您可以假设除了数字 0 之外，这两个数都不会以 0&nbsp;开头。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>(2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)
<strong>输出：</strong>7 -&gt; 0 -&gt; 8
<strong>原因：</strong>342 + 465 = 807
</pre>


## 解法：

```c++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode *p = &dummy;
        int carry = 0;
        while(l1 || l2 || carry){
            int sum = carry;
            if(l1){
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2){
                sum += l2->val;
                l2 = l2->next;
            }
            p->next = new ListNode(sum % 10);
            cy = sum / 10;
            p = p->next;
        }
        return dummy.next;
    }
};
```