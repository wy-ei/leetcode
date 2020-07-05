## 22. Generate Parentheses

- 难度： 中等
- 通过率： 52.0%
- 题目链接：[https://leetcode.com/problems/generate-parentheses](https://leetcode.com/problems/generate-parentheses)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给出&nbsp;<em>n</em>&nbsp;代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且<strong>有效的</strong>括号组合。</p>

<p>例如，给出&nbsp;<em>n </em>=<em> </em>3，生成结果为：</p>

<pre>[
  &quot;((()))&quot;,
  &quot;(()())&quot;,
  &quot;(())()&quot;,
  &quot;()(())&quot;,
  &quot;()()()&quot;
]
</pre>



## 解法：

用一个空字符串，先尝试添加左括号，再添加右括号。

```c++
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string path;
        if (n > 0) {
            generate(n, path, result, 0, 0);
        }
        return result;
    }

    static void generate(int n, string &path, vector<string> &result, int l, int r) {
        if (l == n) {
            string s(path);
            s.append(n - r, ')');
            result.push_back(::move(s));
            return;
        }

        path.push_back('(');
        generate(n, path, result, l + 1, r);
        path.pop_back();

        if (l > r) {
            path.push_back(')');
            generate(n, path, result, l, r + 1);
            path.pop_back();
        }
    }
};
```

也可以采用迭代的方法，每次加入一个括号。在上一步的每个结果之上，如果左括号还有余下的，就可以添加左括号，如果已经添加的左括号数大于右括号数，就可以添加一个右括号。

因此，需要使用一个数组保存当前的结果，使用另外一个数组来记录左括号的数量。

```cpp
class Solution {
public:
vector<string> generateParenthesis(int n) {
        vector<string> parentheses = {"("};
        vector<int> left_counts = {1};
        vector<string> new_parentheses;
        vector<int> new_left_counts;
        
        for (int i = 1; i < n * 2; i++) {
            new_parentheses.clear();
            new_left_counts.clear();
            new_parentheses.reserve(parentheses.size() * 2);
            new_left_counts.reserve(parentheses.size() * 2);

            for (int j = 0; j < parentheses.size(); j++) {
                string &str = parentheses[j];
                int left = left_counts[j];
                int right = str.size() - left;

                if (left < n) {
                    new_parentheses.emplace_back(str + "(");
                    new_left_counts.emplace_back(left + 1);
                }

                if (left > right) {
                    new_parentheses.emplace_back(str + ")");
                    new_left_counts.emplace_back(left);
                }
            }
            parentheses.swap(new_parentheses);
            left_counts.swap(new_left_counts);
        }
        return parentheses;
    }
};
```