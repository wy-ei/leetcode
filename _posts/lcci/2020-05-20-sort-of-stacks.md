---
title: 栈排序
qid: 03.05
tags: [设计]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/sort-of-stacks-lcci/](https://leetcode-cn.com/problems/sort-of-stacks-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：<code>push</code>、<code>pop</code>、<code>peek</code> 和 <code>isEmpty</code>。当栈为空时，<code>peek</code>&nbsp;返回 -1。</p>

<p><strong>示例1:</strong></p>

<pre><strong> 输入</strong>：
[&quot;SortedStack&quot;, &quot;push&quot;, &quot;push&quot;, &quot;peek&quot;, &quot;pop&quot;, &quot;peek&quot;]
[[], [1], [2], [], [], []]
<strong> 输出</strong>：
[null,null,null,1,null,2]
</pre>

<p><strong>示例2:</strong></p>

<pre><strong> 输入</strong>： 
[&quot;SortedStack&quot;, &quot;pop&quot;, &quot;pop&quot;, &quot;push&quot;, &quot;pop&quot;, &quot;isEmpty&quot;]
[[], [], [], [1], [], []]
<strong> 输出</strong>：
[null,null,null,null,null,true]
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>栈中的元素数目在[0, 5000]范围内。</li>
</ol>


## 解法：

如果栈顶元素小于 `val`，就把小于 `val` 的元素全部 push 到另一个栈中。然后将 `val` 入栈，再把另一个栈中的元素转移过来。

```c++
class SortedStack {
public:
    SortedStack() {
    }

    void push(int val) {
        while(!stk1.empty() && stk1.top() < val){
            stk2.push(stk1.top());
            stk1.pop();
        }
        stk1.push(val);
        while(!stk2.empty()){
            stk1.push(stk2.top());
            stk2.pop();
        }
    }

    void pop() {
        if(stk1.empty()){
            return;
        }
        stk1.pop();
    }

    int peek() {
        if(stk1.empty()){
            return -1;
        }
        return stk1.top();
    }

    bool isEmpty() {
        return stk1.empty();
    }

private:
    stack<int> stk1;
    stack<int> stk2;
};
```