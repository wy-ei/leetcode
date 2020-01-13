## 19. Remove Nth Node From End of List

- 难度： 中等
- 通过率： 33.8%
- 题目链接：[https://leetcode.com/problems/remove-nth-node-from-end-of-list](https://leetcode.com/problems/remove-nth-node-from-end-of-list)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个链表，删除链表的倒数第&nbsp;<em>n&nbsp;</em>个节点，并且返回链表的头结点。</p>

<p><strong>示例：</strong></p>

<pre>给定一个链表: <strong>1-&gt;2-&gt;3-&gt;4-&gt;5</strong>, 和 <strong><em>n</em> = 2</strong>.

当删除了倒数第二个节点后，链表变为 <strong>1-&gt;2-&gt;3-&gt;5</strong>.
</pre>

<p><strong>说明：</strong></p>

<p>给定的 <em>n</em>&nbsp;保证是有效的。</p>

<p><strong>进阶：</strong></p>

<p>你能尝试使用一趟扫描实现吗？</p>


## 解法：

```cpp
class Solution {
public:
	/*
		n = 4;

		[ ] -> [ ] -> [ ] -> [X] -> [ ] -> [ ] -> [ ] -> null
		fast -------------------------------> 

		[ ] -> [ ] -> [ ] -> [X] -> [ ] -> [ ] -> [ ] -> null
								           fast ---------->
	    pre------------>


		[ ] -> [ ] -> [ ] -> [X] -> [ ] -> [ ] -> [ ] -> null
					  pre
	*/
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		if (n == 0) {
			return head;
		}

		ListNode* fast = head;
		ListNode* pre = head;

		int k = n;
		while (k--) {
			fast = fast->next;
		}

		if (!fast) {
			
		}

		while (fast->next) {
			fast = fast->next;
			pre = pre->next;
		}

		// n = 1, remove the last one
		if (n == 1) {
			delete pre->next;
			pre->next = nullptr;
		}
		else {
			
		}
		return head;
	}
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *fast = head, *slow = head;
        while(n--){
            fast = fast->next;
        }
        // remove first node
        if(!fast){
            ListNode* ret = head->next;
            delete head;
            return ret;
        }

        while(fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        
        ListNode* next = slow->next;
        slow->next = slow->next->next;
        delete next;
        
        return head;
    }
};
```