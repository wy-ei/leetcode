## 721. Accounts Merge

- 难度： 中等
- 通过率： 37.9%
- 题目链接：[https://leetcode.com/problems/accounts-merge](https://leetcode.com/problems/accounts-merge)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个列表 <code>accounts</code>，每个元素 <code>accounts[i]</code>&nbsp;是一个字符串列表，其中第一个元素 <code>accounts[i][0]</code>&nbsp;是&nbsp;<em>名称 (name)</em>，其余元素是 <em>emails </em>表示该帐户的邮箱地址。</p>

<p>现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。</p>

<p>合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。accounts 本身可以以任意顺序返回。</p>

<p><strong>例子 1:</strong></p>

<pre>
<strong>Input:</strong> 
accounts = [[&quot;John&quot;, &quot;johnsmith@mail.com&quot;, &quot;john00@mail.com&quot;], [&quot;John&quot;, &quot;johnnybravo@mail.com&quot;], [&quot;John&quot;, &quot;johnsmith@mail.com&quot;, &quot;john_newyork@mail.com&quot;], [&quot;Mary&quot;, &quot;mary@mail.com&quot;]]
<strong>Output:</strong> [[&quot;John&quot;, &#39;john00@mail.com&#39;, &#39;john_newyork@mail.com&#39;, &#39;johnsmith@mail.com&#39;],  [&quot;John&quot;, &quot;johnnybravo@mail.com&quot;], [&quot;Mary&quot;, &quot;mary@mail.com&quot;]]
<strong>Explanation:</strong> 
  第一个和第三个 John 是同一个人，因为他们有共同的电子邮件 &quot;johnsmith@mail.com&quot;。 
  第二个 John 和 Mary 是不同的人，因为他们的电子邮件地址没有被其他帐户使用。
  我们可以以任何顺序返回这些列表，例如答案[[&#39;Mary&#39;，&#39;mary@mail.com&#39;]，[&#39;John&#39;，&#39;johnnybravo@mail.com&#39;]，
  [&#39;John&#39;，&#39;john00@mail.com&#39;，&#39;john_newyork@mail.com&#39;，&#39;johnsmith@mail.com&#39;]]仍然会被接受。

</pre>

<p><strong>注意：</strong></p>

<ul>
	<li><code>accounts</code>的长度将在<code>[1，1000]</code>的范围内。</li>
	<li><code>accounts[i]</code>的长度将在<code>[1，10]</code>的范围内。</li>
	<li><code>accounts[i][j]</code>的长度将在<code>[1，30]</code>的范围内。</li>
</ul>


## 解法：

```cpp

template <typename T>
class Hash_UF{
public:
    explicit Hash_UF(){
        union_count = 0;
    }

    int count(){
        return union_count;
    }

    bool connected(const T& p, const T& q){
        return find(p) == find(q);
    }

    void connect(const T& p, const T& q){
        insert_if_not_exist(p);
        insert_if_not_exist(q);

        int pid = find(p);
        int qid = find(q);
        if(pid == qid) return;
        if(sz[pid] > sz[qid]){
            id[qid] = pid;
            sz[pid] += sz[qid];
        }else{
            id[pid] = qid;
            sz[qid] += sz[pid];
        }
        union_count--;
    }

    void insert_if_not_exist(const T &p){
        if(id.find(p) == id.end()){
            id[p] = p;
            union_count++;
        }
    }

    T find(T p){
        while(id[p] != p){
            id[p] = id[id[p]];
            p = id[p];
        }
        return p;
    }
private:
    unordered_map<T, T> id;
    int union_count;
    unordered_map<T, size_t> sz;
};


class Vocab{
public:
    using iterator = typename unordered_map<string, int>::iterator;

    size_t token_to_id(const string &token){
        auto it = vocab.find(token);
        if(it == vocab.end()){
            num_vocab += 1;
            vocab[token] = num_vocab;
            return num_vocab;
        }else{
            return it->second;
        }
    }

    iterator begin(){
        return vocab.begin();
    }
    iterator end(){
        return vocab.end();
    }

private:
    unordered_map<string, int> vocab;
    size_t num_vocab = 0;
};


class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        Hash_UF<int> uf;
        Vocab vocab;

        unordered_map<string, int> name_to_group;
        unordered_map<int, vector<string>> group_to_account;

        for(auto &account: accounts){
            auto it = account.begin();
            ++it; // skip name

            int id1 = vocab.token_to_id(*it);
            uf.insert_if_not_exist(id1); // insert first account
            ++it;
            for(;it != account.end();++it){
                int id2 = vocab.token_to_id(*it);
                uf.connect(id1, id2);
                id1 = id2;
            }
        }

        // add name to group
        for(auto &account: accounts){
            auto it = account.begin();
            string &name = *it;
            ++it;
            int id1 = vocab.token_to_id(*it);
            int group_id = uf.find(id1);
            if(group_to_account[group_id].empty()){
                group_to_account[group_id].push_back(name);
            }
        }

        // add account to certain group
        for(auto it=vocab.begin();it!=vocab.end();++it){
            int group_id = uf.find(it->second);
            group_to_account[group_id].push_back(it->first);
        }

        // sort every group
        vector<vector<string>> ret;
        for(auto it=group_to_account.begin();it!=group_to_account.end();++it){
            sort(it->second.begin()+1, it->second.end());
            ret.push_back(::move(it->second));
        }
        return ret;
    }
};
```