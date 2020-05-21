## 34. 二叉树中和为某一值的路径

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong><br>
给定如下二叉树，以及目标和&nbsp;<code>sum = 22</code>，</p>

<pre>              <strong>5</strong>
             / \
            <strong>4</strong>   <strong>8</strong>
           /   / \
          <strong>11</strong>  13  <strong>4</strong>
         /  \    / \
        7    <strong>2</strong>  <strong>5</strong>   1
</pre>

<p>返回:</p>

<pre>[
   [5,4,11,2],
   [5,8,4,5]
]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>节点总数 &lt;= 10000</code></li>
</ol>

<p>注意：本题与主站 113&nbsp;题相同：<a href="https://leetcode-cn.com/problems/path-sum-ii/">https://leetcode-cn.com/problems/path-sum-ii/</a></p>


## 解法：深度优先遍历

在遍历过程中记录下当前走过的路径，如果路径之和等于目标值，且当前节点为叶子节点，那么将当前路径插入结果中。

深度优先遍历采用递归的写法，可以使用单个容器记录下当前的路径。进入节点时，在路径中插入节点，退出节点时，删除节点。

```cpp
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> ret;
        vector<int> path;
        
        dfs(root, path, sum, ret);
        return ret;
    }

    void dfs(TreeNode* node, vector<int>& path, int target, vector<vector<int>>& ret){
        if(node == nullptr) return;

        path.push_back(node->val);

        bool leaf = (node->left == nullptr) && (node->right == nullptr);
        if(node->val == target && leaf){
            ret.push_back(path);
            path.pop_back();
            return;
        }
        target -= node->val;

        dfs(node->left, path, target, ret);
        dfs(node->right, path, target, ret);
        
        path.pop_back();
    }
};
```
