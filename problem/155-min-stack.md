## 155. Min Stack

- 难度： 简单
- 通过率： 34.7%
- 题目链接：[https://leetcode.com/problems/min-stack](https://leetcode.com/problems/min-stack)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。</p>

<ul>
	<li>push(x)&nbsp;-- 将元素 x 推入栈中。</li>
	<li>pop()&nbsp;-- 删除栈顶的元素。</li>
	<li>top()&nbsp;-- 获取栈顶元素。</li>
	<li>getMin() -- 检索栈中的最小元素。</li>
</ul>

<p><strong>示例:</strong></p>

<pre>MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --&gt; 返回 -3.
minStack.pop();
minStack.top();      --&gt; 返回 0.
minStack.getMin();   --&gt; 返回 -2.
</pre>


## 解法：

使用另外一个`min_stack`，保存当前元素之前最小的元素。比如插入序列为 `2 3 4 1 5`，在压入 `2 3 4` 的时候，在 `min_stack` 里压入最小值 `2`，当压入 `1 5` 的时候，再压入最小值 `1`。当 `1` 最后被弹出的时候，也把 `min_stack` 的栈顶的 `1` 弹出。此时 `min_stack` 栈顶元素就是 `2`，为目前最小值。

```cpp
class MinStack {
public:
    MinStack() {}

    void push(int x) {
        if(min_stack_.size() == 0 || min_stack_.top() >= x){
            min_stack_.push(x);
        }
        data_stack_.push(x);
    }

    void pop() {
        if(data_stack_.top() == min_stack_.top()){
            min_stack_.pop();
        }
        data_stack_.pop();
    }

    int top() {
        return data_stack_.top();
    }

    int getMin() {
        return min_stack_.top();
    }

private:
    stack<int> data_stack_;
    stack<int> min_stack_;
};
```
