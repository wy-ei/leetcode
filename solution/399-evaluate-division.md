## 399. Evaluate Division

- 难度： 中等
- 通过率： 45.5%
- 题目链接：[https://leetcode.com/problems/evaluate-division](https://leetcode.com/problems/evaluate-division)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给出方程式&nbsp;<code>A / B = k</code>, 其中&nbsp;<code>A</code> 和&nbsp;<code>B</code> 均为代表字符串的变量，&nbsp;<code>k</code> 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回&nbsp;<code>-1.0</code>。</p>

<p><strong>示例 :</strong><br />
给定&nbsp;<code>a / b = 2.0, b / c = 3.0</code><br />
问题: <code> a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?&nbsp;</code><br />
返回&nbsp;<code>[6.0, 0.5, -1.0, 1.0, -1.0 ]</code></p>

<p>输入为: <code> vector&lt;pair&lt;string, string&gt;&gt; equations, vector&lt;double&gt;&amp; values, vector&lt;pair&lt;string, string&gt;&gt; queries</code>(方程式，方程式结果，问题方程式)，&nbsp;其中&nbsp;<code>equations.size() == values.size()</code>，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。&nbsp;返回<code>vector&lt;double&gt;</code>类型。</p>

<p>基于上述例子，输入如下：</p>

<pre>
equations(方程式) = [ [&quot;a&quot;, &quot;b&quot;], [&quot;b&quot;, &quot;c&quot;] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ [&quot;a&quot;, &quot;c&quot;], [&quot;b&quot;, &quot;a&quot;], [&quot;a&quot;, &quot;e&quot;], [&quot;a&quot;, &quot;a&quot;], [&quot;x&quot;, &quot;x&quot;] ]. 
</pre>

<p>输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。</p>


## 解法：

使用并查集，计算出分子分母到 root 的商，然后两者做除法即可得到结果。如果分子分母都不在一个集合中，那就无解。

```cpp
class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        for(size_t i=0;i<equations.size();++i){
            auto equation = equations[i];
            string& v1 = equation[0];
            string& v2 = equation[1];
            double value = values[i];

            int id1 = token_to_id(v1);
            int id2 = token_to_id(v2);

            connect(id1, id2, value);
        }

        return eval(queries);
    }

    int token_to_id(const string &token){
        if(vocab.find(token) == vocab.end()){
            num_vocab += 1;
            vocab[token] = num_vocab;
        }
        return num_vocab;
    }

    vector<double> eval(vector<vector<string>> &queries){
        vector<double> ret;
        for(auto equation : queries){
            string& v1 = equation[0];
            string& v2 = equation[1];

            if(vocab.find(v1) == vocab.end() || vocab.find(v2) == vocab.end()){
                ret.push_back(-1);
                continue;
            }

            int id1 = vocab[v1];
            int id2 = vocab[v2];

            double root_div_id1, root_div_id2;
            int root_id1, root_id2;

            std::tie(root_id1, root_div_id1) = find(id1);
            std::tie(root_id2, root_div_id2) = find(id2);

            if(root_id1 != root_id2){
                ret.push_back(-1);
            } else{
                ret.push_back(root_div_id2 / root_div_id1);
            }
        }
        return ret;
    }

    void connect(int id1, int id2, double value){
        if(mp.find(id1) == mp.end()){
            mp[id1] = make_pair(id1, 1);
        }
        if(mp.find(id2) == mp.end()){
            mp[id2] = make_pair(id2, 1);
        }

        double root_div_id1, root_div_id2;
        int root_id1, root_id2;

        std::tie(root_id1, root_div_id1) = find(id1);
        std::tie(root_id2, root_div_id2) = find(id2);

        if(root_id1 == root_id2){
            return;
        }

        mp[root_id2].first = root_id1;
        mp[root_id2].second = root_div_id1 / root_div_id2 * value;
    }

    tuple<int, double> find(int id){
        int root_id = id;
        double root_div_id = 1;
        while(root_id != mp[root_id].first){
            root_div_id *= mp[root_id].second;
            root_id = mp[root_id].first;
        }
        mp[id].first = root_id;
        mp[id].second = root_div_id;
        return make_tuple(root_id, root_div_id);
    }

private:
    // id1  ->  <id2, id1/id2>
    unordered_map<int, pair<int, double>> mp;
    unordered_map<string, int> vocab;
    size_t num_vocab = 0;
};
```