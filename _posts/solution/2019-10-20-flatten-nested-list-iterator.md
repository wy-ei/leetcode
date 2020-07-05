---
title: 扁平化嵌套列表迭代器
qid: 341
tags: [栈,设计]
---


- 难度： 中等
- 通过率： 45.9%
- 题目链接：[https://leetcode.com/problems/flatten-nested-list-iterator](https://leetcode.com/problems/flatten-nested-list-iterator)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。</p>

<p>列表中的项或者为一个整数，或者是另一个列表。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>[[1,1],2,[1,1]]
<strong>输出: </strong>[1,1,2,1,1]
<strong>解释: </strong>通过重复调用&nbsp;<em>next </em>直到&nbsp;<em>hasNex</em>t 返回false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,1,2,1,1]</code>。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>[1,[4,[6]]]
<strong>输出: </strong>[1,4,6]
<strong>解释: </strong>通过重复调用&nbsp;<em>next&nbsp;</em>直到&nbsp;<em>hasNex</em>t 返回false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,4,6]</code>。
</pre>


## 解法：

```c++
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        push_nested_list_into_stack(nestedList);
        flatten_top();
    }
    
    int next() {
        int n = stk.top()->getInteger();
        stk.pop();
        return n;
    }
    
    bool hasNext() {
        flatten_top();
        return !stk.empty();
    }
private:
    void push_nested_list_into_stack(const vector<NestedInteger> & nestedList){
        for(int i=nestedList.size()-1;i>=0;i--){
            stk.push(&nestedList[i]);
        }
    }
    void flatten_top(){
        while(!stk.empty() && !stk.top()->isInteger()){
            const auto & nestedList = stk.top()->getList();
            stk.pop();
            push_nested_list_into_stack(nestedList);
        }
    }
    stack<const NestedInteger*> stk;
};
```