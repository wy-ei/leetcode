---
title: 布尔运算
qid: 08.14
tags: [栈,字符串]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/boolean-evaluation-lcci/](https://leetcode-cn.com/problems/boolean-evaluation-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 <code>0</code> (false)、<code>1</code> (true)、<code>&amp;</code> (AND)、 <code>|</code> (OR) 和 <code>^</code> (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>s = &quot;1^0|0|1&quot;, result = 0

<strong>输出: </strong>2
<strong>解释:</strong>&nbsp;两种可能的括号方法是
1^(0|(0|1))
1^((0|0)|1)
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>s = &quot;0&amp;0&amp;0&amp;1^1|0&quot;, result = 1

<strong>输出: </strong>10</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>运算符的数量不超过 19 个</li>
</ul>


## 解法：

把算式断开 a op b，分别计算 a 和 b 中 0 和 1 的个数，然后根据 op 计算出整个算式中 0 和 1 的个数。这里 a 和 b 可以再做类型的拆分，知道只有单个数字为止。很容易看出，这是一个递归过程，递归的参数是需要计算的算式的范围。

为了不必要的运算，可以使用范围作为键，把运算结果保存下来，之后同样的范围时，可以直接返回结果。

```c++
class Solution {
public:
    int countEval(string s, int result) {
        vector<char> nums;
        vector<char> ops;
        for(char ch: s){
            if(ch == '0' || ch == '1'){
                nums.push_back(ch - '0');
            }else{
                ops.push_back(ch);
            }
        }
        vector<vector<int>> cache_0(nums.size(), vector<int>(nums.size(), -1));
        vector<vector<int>> cache_1(nums.size(), vector<int>(nums.size(), -1));
        int n = nums.size();
        eval(nums, ops, 0, n-1, cache_0, cache_1);

        if(result == 0){
            return cache_0[0][n-1];
        }else{
            return cache_1[0][n-1];
        }
    }
    void eval(vector<char> nums, vector<char> ops, int lo, int hi, vector<vector<int>>& cache_0, vector<vector<int>>& cache_1){
        if(cache_0[lo][hi] != -1) return;
        if(lo == hi){
            if(nums[lo] == 0){
                cache_0[lo][hi] = 1;
                cache_1[lo][hi] = 0; 
            }else{
                cache_0[lo][hi] = 0;
                cache_1[lo][hi] = 1; 
            }
            return;
        }
        
        int n_0 = 0, n_1 = 0;
        for(int i = lo+1;i<=hi;i++){
            eval(nums, ops, lo, i-1, cache_0, cache_1);
            eval(nums, ops, i, hi, cache_0, cache_1);
            char op = ops[i-1];
            int left_0 = cache_0[lo][i-1];
            int left_1 = cache_1[lo][i-1];
            int right_0 = cache_0[i][hi];
            int right_1 = cache_1[i][hi];

            if(op == '&'){
                n_0 += left_0 * (right_0 + right_1) + right_0 * left_1;
                n_1 += left_1 * right_1;
            }else if(op == '|'){
                n_0 += left_0 * right_0;
                n_1 += left_1 * (right_0 + right_1) + right_1 * left_0;
            }else if(op == '^'){
                n_0 += left_0 * right_0 + left_1 * right_1;
                n_1 += left_0 * right_1 + left_1 * right_0;
            }
        }
        cache_0[lo][hi] = n_0;
        cache_1[lo][hi] = n_1;
    }
};
```