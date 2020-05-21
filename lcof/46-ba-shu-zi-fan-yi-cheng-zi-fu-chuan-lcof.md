## 46. 把数字翻译成字符串

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 &ldquo;a&rdquo; ，1 翻译成 &ldquo;b&rdquo;，&hellip;&hellip;，11 翻译成 &ldquo;l&rdquo;，&hellip;&hellip;，25 翻译成 &ldquo;z&rdquo;。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 12258
<strong>输出:</strong> <code>5
</code><strong>解释:</strong> 12258有5种不同的翻译，分别是&quot;bccfi&quot;, &quot;bwfi&quot;, &quot;bczi&quot;, &quot;mcfi&quot;和&quot;mzi&quot;</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num &lt; 2<sup>31</sup></code></li>
</ul>


## 思路：

先把数字 num 转换为字符串 s，设 `f(i)` 为 `s[i:]` 可以构成的翻译结果数量。那么：

`s[i]` 可以翻译成一个字母，它与 `s[i]` 后面的字符串翻译的结果组合起来，并没有带来多样性。但如果 `s[i:i+2]` 构成的数字 `10~25` 之间，它们就可以合并起来构成一个字母。此时：`f(i) = f(i+1) + f(i+2)`，否则 `f(i) = f(i+1)`。


## 解法一：带记忆的递归

```c++
class Solution {
public:
    int translateNum(int num) {
		unordered_map<int, int> cache;
        string s = to_string(num);
        return translateNum(s, 0, cache);
    }
private:
    int translateNum(string s, int i, unordered_map<int, int>& cache){
        if(cache.find(i) != cache.end()){
            return cache[i];
        }
        if(s.size() == i){
            return 1;
        }
        int num = translateNum(s, i+1, cache);
        if(i + 1 < s.size()){
            int n = (s[i] - '0') * 10 + (s[i+1] - '0');
            if(n <= 25 && n >= 10){
                num += translateNum(s, i+2, cache);
            }
        }
        cache[i] = num;
        return num;
    }
};
```


## 解法二：自底向上，非递归解法

基本上每个动态规划问题都可以用记忆化递归来解决，递归自顶向下计算，为了避免对子问题重复计算，可以保存下已经计算过的结果。如果先把子问题计算出来，然后在用子问题的结果来结果更大的子问题，这样就可以使用迭代的方法。

本题中依赖的子问题的解只有两个，即 `f(i+1)` 和 `f(i+2)`，因此可以使用两个变量保存这两个解。产生新的解以后，再更新这两个变量。

```c++
class Solution {
public:
    int translateNum(int num) {
        string s = to_string(num);
        int first = 1, second = 1;
        int n1 = num % 10, n2 = 0;
        num /= 10;

        while(num){
            n2 = n1;
            n1 = num % 10;
            n2 += n1 * 10;
            num /= 10;

            int old_first = first;
            if(n2 <= 25 && n2 >= 10){
                first += second; 
            }
            second = old_first;
        }   
        return first;
    }
};
```