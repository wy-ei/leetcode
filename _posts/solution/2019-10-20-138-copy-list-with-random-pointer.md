---
title: 复制带随机指针的链表
qid: 138
tag: [哈希表, 链表]
---

- 难度： 中等
- 通过率： 25.6%
- 题目链接：[https://leetcode-cn.com/problems/copy-list-with-random-pointer](https://leetcode-cn.com/problems/copy-list-with-random-pointer)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。</p>

<p>要求返回这个链表的深度拷贝。&nbsp;</p>



## 解法一：哈希表

使用原节点的地址作为 `key` 用拷贝的节点作为 `value`。先把所有节点拷贝一份，然后再把拷贝的节点串起来。


```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> mp;
		for(Node* p=head;p != nullptr;p = p->next){
			mp[p] = new Node(p->val);
		}
		for(Node* p=head;p != nullptr;p = p->next){
			mp[p].next = mp[p->next];
			mp[p].random = mp[p->random];
		}
		return mp[head];
    }
};
```

## 解法二：

复制链表中的每个节点，把该节点插入到原节点的后面。

```
1-->2-->3

1-->1-->2-->2-->3-->3
```

复制完了之后，修改指针的指向 `next == next->next`，`random = random->next`。

```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head) return nullptr;
        
		Node *p = head;
		while(p != nullptr){
			Node *node = new Node(p->val);
			node->next = p->next;
			node->random = p->random;
			p->next = node;
			p = node->next;
		}
		p = head;
		while(p != nullptr){
            if(p->next->random){
    			p->next->random = p->next->random->next;
            }
			p = p->next->next;
		}

		p = head;
		head = p->next;
		while(p != nullptr){
			Node *copy = p->next;
			p->next = copy->next;
			p = p->next;
			if(copy->next){
				copy->next = p->next;
			}
		}

		return head;
    }
};
```


这个方法真巧秒啊。