## 148. Sort List

- 难度： 中等
- 通过率： 33.0%
- 题目链接：[https://leetcode.com/problems/sort-list](https://leetcode.com/problems/sort-list)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>在&nbsp;<em>O</em>(<em>n</em>&nbsp;log&nbsp;<em>n</em>) 时间复杂度和常数级空间复杂度下，对链表进行排序。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 4-&gt;2-&gt;1-&gt;3
<strong>输出:</strong> 1-&gt;2-&gt;3-&gt;4
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> -1-&gt;5-&gt;3-&gt;4-&gt;0
<strong>输出:</strong> -1-&gt;0-&gt;3-&gt;4-&gt;5</pre>


## 解法：


使用归并排序。

```cpp
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next) return head;
        // fast = head->next   this is very important
        // can't be fast=head
        ListNode *fast = head->next, *slow = head, *middle;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        middle = slow->next;
        slow->next = nullptr;

        head = sortList(head);
        middle = sortList(middle);
        return merge(head, middle);
    }

    ListNode* merge(ListNode* l1, ListNode* l2){
        ListNode pre(-1);
        ListNode *p = &pre;
        while(l1 != nullptr && l2 != nullptr){
            if(l1->val < l2->val){
                p->next = l1;
                l1 = l1->next;
            }else{
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        p->next = (l1 == nullptr) ? l2 : l1;
        return pre.next;
    }
};
```