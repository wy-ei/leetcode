---
title: 基本计算器II
qid: 227
layout: post
tag: [字符串]
---


- 难度： 中等
- 通过率： 32.1%
- 题目链接：[https://leetcode-cn.com/problems/basic-calculator-ii](https://leetcode-cn.com/problems/basic-calculator-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>实现一个基本的计算器来计算一个简单的字符串表达式的值。</p>

<p>字符串表达式仅包含非负整数，<code>+</code>， <code>-</code> ，<code>*</code>，<code>/</code> 四种运算符和空格&nbsp;<code>&nbsp;</code>。 整数除法仅保留整数部分。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong>&quot;3+2*2&quot;
<strong>输出:</strong> 7
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> &quot; 3/2 &quot;
<strong>输出:</strong> 1</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> &quot; 3+5 / 2 &quot;
<strong>输出:</strong> 5
</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>你可以假设所给定的表达式都是有效的。</li>
	<li>请<strong>不要</strong>使用内置的库函数 <code>eval</code>。</li>
</ul>


## 解法一：基于后缀表达式

如下这种正常的这种表达式，很不利于计算机直接求值，人在计算它的结果时，首先会看一下优先级，先计算括号里面的，先计算乘除法，然后加减法。我们人其实是对整个表达式经过了多次扫描，然后不断计算其中的某个部分，最终把整个表达式计算完成。但这种方法，对计算机而言不够高效，我们期望它能一遍扫描就计算完成。

```
1 + 4 * 5 + 2 * (3 + 1)
```

我们把整个表达式转化为后缀表达式：

```
1 4 5 * + 2 3 1 + * +
```

后文会提到如何得到后缀表达式，这里先看看后缀表达式的求值。遍历每个 token，遇到符号之后，就对该符号前面的两个数进行运算得到一个结果，这就可以消除两个数字和一个符号。如此持续运算，最终会得到运算结果。上面的表达式计算过程如下：

```python
1 4 5 * + 2 3 1 + * +
1 20 + 2 3 1 + * +      # 对 4 5 * 求值得到 20
21 2 3 1 + * +          # 对 1 20 + 求值得到 21
21 2 4 * +              # 对 3 1 + 求值得到 4
21 8 +                  # 对 2 4 * 求值得到 8
29                      # 对 21 8 + 求值得到 29
```

计算过程就是使用一个栈，遇到数字就入栈，遇到符号就出栈两个数，然后将计算结果再次入栈。这种基于后缀表达式的方法，计算步骤非常简单，但前提是要把原表达式转化为后缀表达式。

![](https://wangyu-name.oss-cn-hangzhou.aliyuncs.com/superbed/2020/07/27/5f1e63f514195aa594a1edf1.jpg)

整个表达式可以看作是一个二叉树，其中叶子节点是数字，内部节点是运算符号。常规的表达式是二此二叉树的中序遍历，而后缀表达式就是此二叉树的后序遍历。但是我们不能通过中序遍历的序列得到后序遍历序列。其实上面的表达式可以表示成多种不同的树，上面的这个树只是其中一种而已。

好在我们能够得到一个不改变原表达式值的后缀表达式，它的过程是这样的：

使用 seq 表示后缀表达式序列，使用一个栈保存操作符。

1. 遍历原序列，记每个 token 为 t
2. 如果 t 是数字，就把它加入 seq
3. 如果 t 是操作符
	- 如果栈非空，就把栈中优先级比 t 更高的运算符 pop 出来并加入 seq 中，然后把 t 入栈。
	- 如果栈为空，就把 t 入栈
4. 如果 t 是左括号，就入栈。如果 t 是右括号，就不断出栈直到遇到左括号（抛弃左括号）
5. 遍历完原序列后，把栈中余下的内容加入到 seq 中

下面是完整的实现代码，支持加减乘除和括号。


```cpp
// 输入的是字符串，其中包含数字和操作符号，这里把每个数字和操作符号转为一个 Token
// kind 表示符号类型，可取值为 '+', '-', '*', '/', '(', ')' 和 0，其中 0 表示这个 Token 是数字
// 如果支持浮点数，只需要修改 Token 中 value 的数据类型，并且修改 tokenize 方法即可
struct Token{
    char kind;
    int value;
};

class Solution {
public:
    int calculate(string s) {
        vector<Token> tokens = tokenize(s);

        vector<Token> postOrderTokens = inOrderToPostOrder(tokens);

        int res = evalPostOrder(postOrderTokens);

        return res;
    }

private:
    // 对后缀表达式序列求值
    static int evalPostOrder(const vector<Token>& postOrderTokens){
        stack<int> values;
        for(const Token& t: postOrderTokens){
            if(t.kind == 0){
                values.push(t.value);
            }else{
                int b = values.top();
                values.pop();
                int a = values.top();
                values.pop();
                switch (t.kind) {
                    case '+':
                        values.push(a + b);
                        break;
                    case '-':
                        values.push(a - b);
                        break;
                    case '*':
                        values.push(a * b);
                        break;
                    case '/':
                        values.push(a / b);
                    default:
                        break;
                }
            }
        }
        return values.top();
    }

    // 转化中序序列为后序序列
    static vector<Token> inOrderToPostOrder(const vector<Token>& tokens){
        vector<Token> res;
        stack<Token> stk;

        for(const Token& t: tokens){
            switch (t.kind) {
                case 0: // kind == 0 表示数字
                    res.push_back(t);
                    break;
                case '(':
                    stk.push(t);
                    break;
                case ')':
                    while (stk.top().kind !=  '('){
                        res.push_back(stk.top());
                        stk.pop();
                    }
                    stk.pop(); // pop '('
                    break;
                case '+':
                case '-':
                case '*':
                case '/':
                    while(!stk.empty() && stk.top().kind != '(' &&
                        compare_priority(stk.top().kind, t.kind) >= 0){

                        res.push_back(stk.top());
                        stk.pop();
                    }
                    stk.push(t);
                default:
                    break;
            }
        }
        while(!stk.empty()){
            res.push_back(stk.top());
            stk.pop();
        }
        return res;
    }

    // 比较两个运算符的优先级:
    // a < b   -> -1
    // a == b  -> 0
    // a > b   -> 1
    static int compare_priority(char a, char b){
        if (a == '+' || a == '-'){
            if(b == '+' || b == '-'){
                return 0;
            }else{
                return -1;
            }
        }
        if(a == '*' || a == '/'){
            if(b == '*' || b == '/'){
                return 0;
            }else{
                return 1;
            }
        }
        return 0;
    }

    // 把输入字符串转化为 Token 序列
    static vector<Token> tokenize(const string& s){
        vector<Token> tokens;
        int i = 0;
        while(i < s.size()){
            if(s[i] == ' '){
                i++;
                continue;
            }
            if(!isdigit(s[i])){
                tokens.push_back(Token{.kind = s[i], .value = 0});
                i++;
                continue;
            }
            int n = 0;
            while(isdigit(s[i])){
                n = n * 10 + (s[i] - '0');
                i++;
            }
            tokens.push_back(Token{.kind = 0, .value = n});
        }
        return tokens;
    }
};
```

## 解法二：递归下降

![](https://wangyu-name.oss-cn-hangzhou.aliyuncs.com/superbed/2020/07/27/5f1e63f514195aa594a1edf1.jpg)

观察上面这个表达式树，如果先左右孩子均为数值的子树求值，消除一个子树，继续以上过程，整个表达式的值就能求出来了。

使用递归下降来对表达式求值，其本质还是对表达式树进行求值，基于递归的思想，先计算最最基本的子树（左右孩子均为数值），然后一步步第求出整个表达式的结果。这个解法比较复杂，需要大致了解一下编译原理。这里我不打算写了。

首先写出四则运算表达式的文法：

```
expression := term
            | expression + term
            | expression - term

term := primary
      | term * primary
      | term / primary

primary := number
        | ( expression )
        | - primary
        | + primary
```

基于文法使用递归下降对表达式进行求值：


```cpp
struct Token{
    char kind;
    int value;
};

class Solution{
public:
    int calculate(const string& exp){
        this->tokens_ = tokenize(exp);
        return expression();
    }

private:
    int expression(){
        int lhs = term();
        Token t = lookahead(0);
        while(true){
            switch (t.kind) {
                case '+':
                    consume(t.kind);
                    lhs += term();
                    t = lookahead(0);
                    break;
                case '-':
                    consume(t.kind);
                    lhs -= term();
                    t = lookahead(0);
                    break;
                default:
                    return lhs;
            }
        }
    }

    int term(){
        int lhs = primary();
        Token t = lookahead(0);
        while (true){
            switch (t.kind) {
                case '*':
                    consume(t.kind);
                    lhs *= primary();
                    t = lookahead(0);
                    break;
                case '/':
                    consume(t.kind);
                    lhs /= primary();
                    t = lookahead(0);
                    break;
                default:
                    return lhs;
            }
        }
    }

    int primary(){
        Token t = lookahead(0);
        consume(t.kind);
        switch (t.kind) {
            case '(': {
                int d = expression();
                consume(')');
                return d;
            }
            case '0':
                return t.value;
            case '-':
                return -primary();
            case '+':
                return primary();
            default:
                throw logic_error("invalid expression");
        }
    }

    Token lookahead(int i){
        if(index_ + i < tokens_.size()){
            return tokens_[index_ + i];
        }else{
            return Token{.kind = -1, .value = 0};
        }
    }

    void consume(int kind){
        if(index_ < tokens_.size()){
            if(tokens_[index_].kind == kind){
                index_++;
            }else{
                throw logic_error("invalid expression");
            }
        }else{
            logic_error("invalid expression");
        }
    }
    
    static vector<Token> tokenize(const string& s){
        vector<Token> tokens;
        int i = 0;
        while(i < s.size()){
            if(s[i] == ' '){
                i++;
                continue;
            }
            if(!isdigit(s[i])){
                tokens.push_back(Token{.kind = s[i], .value = 0});
                i++;
                continue;
            }
            int n = 0;
            while(isdigit(s[i])){
                n = n * 10 + (s[i] - '0');
                i++;
            }
            tokens.push_back(Token{.kind = 0, .value = n});
        }
        return tokens;
    }
private:
    vector<Token> tokens_;
    int index_ = 0;
};
```