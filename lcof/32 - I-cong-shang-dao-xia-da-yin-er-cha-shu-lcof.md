## 32 - I. 从上到下打印二叉树

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。</p>

<p>&nbsp;</p>

<p>例如:<br>
给定二叉树:&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回：</p>

<pre>[3,9,20,15,7]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>节点总数 &lt;= 1000</code></li>
</ol>


## 解法：

层次遍历，使用队列即可。

```cpp
class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
       vector<int> ret;
       if(root == nullptr) return ret;
       queue<TreeNode*> node_queue;
       node_queue.push(root);
       while(!node_queue.empty()){
          TreeNode *node = node_queue.front();
          node_queue.pop();
          ret.push_back(node->val);
          if(node->left){
             node_queue.push(node->left);
          }
          if(node->right){
             node_queue.push(node->right);
          }
       }
       return ret;
    }
};
```