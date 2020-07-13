---
title: 二叉树的序列化与反序列化
qid: 297
tag: [树, 设计]
---

- 难度： 困难
- 通过率： 38.3%
- 题目链接：[https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。</p>

<p>请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。</p>

<p><strong>示例:&nbsp;</strong></p>

<pre>你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 <code>&quot;[1,2,3,null,null,4,5]&quot;</code></pre>

<p><strong>提示:&nbsp;</strong>这与 LeetCode 目前使用的方式一致，详情请参阅&nbsp;<a href="/faq/#binary-tree">LeetCode 序列化二叉树的格式</a>。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。</p>

<p><strong>说明:&nbsp;</strong>不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。</p>


## 解法：


示例中是按层进行序列化的，我按照这个思路实现，结果超时了。因为按层进行序列化非常浪费内存。假设有一个高度为 10 的树，它只有 10 个节点，即每个节点只有一个孩子。如果以逗号分隔各个节点，按层存储需要约 `2^10` 个节点。这是相当不划算的。

这里采用了先序遍历，对每个节点进行序列化，在序列化的时候，叶子节点的左右孩子需要序列化为 `null`，以标识子树的终结。在反序列化的时候，同样进行先序遍历即可恢复二叉树，每次从序列中取一个节点，如果不为 `null` 就按照正常先序遍历进行，如果是 `null` 就退出递归。


```c++
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream os;
        serialize(root, os);
        return os.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<TreeNode*> nodes = parse(data);
        if(nodes.empty()){
            return nullptr;
        }

        int index = 0;
        TreeNode *root = deserialize(nodes, index);

        return root;
    }

private:
    void serialize(TreeNode* node, ostringstream& os) {
        if(node == nullptr){
            os << "null,";
            return;
        }
        os << node->val << ',';
        serialize(node->left, os);
        serialize(node->right, os);
    }

    TreeNode* deserialize(vector<TreeNode*>& nodes, int& index){
        TreeNode *node = nodes[index];
        index += 1;
        if(node == nullptr){
            return nullptr;
        }
        
        node->left = deserialize(nodes, index);
        node->right = deserialize(nodes, index);
        return node;
    }

    static vector<TreeNode*> parse(const string& s){
        vector<TreeNode*> nodes;
        if(s.empty()) return nodes;

        vector<string> items = split(s, ',');
        for(auto& item: items){
            if(item[0] == 'n'){
                nodes.push_back(nullptr);
            }else{
                auto *node = new TreeNode(stoi(item));
                nodes.push_back(node);
            }
        }
        return nodes;
    }

    static vector<string> split(string s, char sep){
        vector<string> items;
        auto first = s.begin();
        auto last = s.end();

        auto start = first;
        for(auto it = first;it != last;++it){
            if(*it == sep){
                items.emplace_back(start, it);
                start = it + 1;
            }
        }
        if(start < last){
            items.emplace_back(start, last);
        }

        return items;
    }
};
```