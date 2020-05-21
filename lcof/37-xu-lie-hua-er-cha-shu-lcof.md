## 37. 序列化二叉树

- 难度：Hard
- 题目链接：[https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>请实现两个函数，分别用来序列化和反序列化二叉树。</p>

<p><strong>示例:&nbsp;</strong></p>

<pre>你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 <code>&quot;[1,2,3,null,null,4,5]&quot;</code></pre>

<p>注意：本题与主站 297 题相同：<a href="https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/">https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/</a></p>


## 解法：


示例中是按层进行序列化的，我按照这个思路实现，结果超时了。因为按层进行序列化非常浪费内存。假设有一个高度为 10 的树，它只有 10 个节点，即每个节点只有一个孩子。如果以逗号分隔各个节点，按层存储需要约 `2^10` 个节点。这是相当不划算的。

这里采用了先序遍历，对每个节点进行序列化。在反序列化的时候，同样进行先序遍历即可恢复二叉树。


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