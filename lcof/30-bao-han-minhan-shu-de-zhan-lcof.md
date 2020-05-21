## 30. 包含min函数的栈

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre>MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --&gt; 返回 -3.
minStack.pop();
minStack.top();      --&gt; 返回 0.
minStack.min();   --&gt; 返回 -2.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>各函数的调用总次数不超过 20000 次</li>
</ol>

<p>&nbsp;</p>

<p>注意：本题与主站 155 题相同：<a href="https://leetcode-cn.com/problems/min-stack/">https://leetcode-cn.com/problems/min-stack/</a></p>


## 解法：

```c++
class MinStack {
public:
    MinStack() {}
    void push(int val) {
        stack1.push(val);
        
        if(stack2.empty() || stack2.top() >= val){
            stack2.push(val);
        }
    }
    void pop() {
        if(stack2.top() == stack1.top()){
            stack2.pop();
        }
        stack1.pop();
    }
    int top() {
        return stack1.top();
    }
    
    int min() {
        return stack2.top();
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};
```