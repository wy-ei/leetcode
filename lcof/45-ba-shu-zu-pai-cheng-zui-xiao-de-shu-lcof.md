## 45. 把数组排成最小的数

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>[10,2]</code>
<strong>输出:</strong> &quot;<code>102&quot;</code></pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code>[3,30,34,5,9]</code>
<strong>输出:</strong> &quot;<code>3033459&quot;</code></pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
    <li><code>0 &lt; nums.length &lt;= 100</code></li>
</ul>

<p><strong>说明: </strong></p>

<ul>
    <li>输出结果可能非常大，所以你需要返回一个字符串而不是整数</li>
    <li>拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0</li>
</ul>


## 解法：

一个数的最高位越小，把它放在前面时，构成的数字也就越小。但是如果两个数字 a 和 b 的最高位相同怎么办？此时单从数字本身来确定谁前谁后，是挺麻烦的。但是可以比较 `str(a)+str(b)` 和 `str(b)+str(a)` 的大小，如果前者小，自然 `a` 应该在 `b` 的前面。

```c++
class Solution {
public:
    string minNumber(vector<int>& nums) {
        vector<string> strs;
        strs.reserve(nums.size());
        transform(nums.begin(), nums.end(), back_inserter(strs), [](int n){
            return to_string(n);
        });
        sort(strs.begin(), strs.end(), [](string &a, string &b){
            if(a[0] < b[0]){
                return true;
            }else if(a[0] > b[0]){
                return false;
            }else{
                return a + b < b + a;
            }
        });
        ostringstream os;
        copy(strs.begin(), strs.end(), ostream_iterator<string>(os));
        return os.str();
    }
};
```