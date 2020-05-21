## 68 - II. 二叉树的最近公共祖先

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。</p>

<p><a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：&ldquo;对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（<strong>一个节点也可以是它自己的祖先</strong>）。&rdquo;</p>

<p>例如，给定如下二叉树:&nbsp; root =&nbsp;[3,5,1,6,2,0,8,null,null,7,4]</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/binarytree.png"></p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>输出:</strong> 3
<strong>解释: </strong>节点 <code>5 </code>和节点 <code>1 </code>的最近公共祖先是节点 <code>3。</code>
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>输出:</strong> 5
<strong>解释: </strong>节点 <code>5 </code>和节点 <code>4 </code>的最近公共祖先是节点 <code>5。</code>因为根据定义最近公共祖先节点可以为节点本身。
</pre>

<p>&nbsp;</p>

<p><strong>说明:</strong></p>

<ul>
	<li>所有节点的值都是唯一的。</li>
	<li>p、q 为不同节点且均存在于给定的二叉树中。</li>
</ul>

<p>注意：本题与主站 236 题相同：<a href="https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/">https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/</a></p>


## 解法：

深度优先遍历得到从根节点到待查找节点的路径，然后在路径中查找公共节点。

```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> path1 = find_path(root, p);
        vector<TreeNode*> path2 = find_path(root, q);
        auto it = find_first_of(path1.rbegin(), path1.rend(), path2.rbegin(), path2.rend());
        return *it;
    }

private:
    static vector<TreeNode*> find_path(TreeNode* root, TreeNode* node){
        vector<TreeNode*> path;
        find_path(root, node, path);
        return path;
    }
    
    static bool find_path(TreeNode* root, TreeNode* node, vector<TreeNode*>& path){
        if(root == nullptr){
            return false;
        }
        path.push_back(root);
        
        if(root == node){
            return true;
        }
        
        bool found = find_path(root->left, node, path);
        if(found){
            return found;
        }
        
        found = find_path(root->right, node, path);
        if(found){
            return found;
        }
        
        path.pop_back();
        return false;
    }
};
```

## 解法二：

使用深度优先搜索在左子树和右子树中寻找两个待查找节点，如果左右子树中都能找到其中的一个，说明当前节点就是两者的最近公共节点。因为是深度优先搜索，因此在递归调用的某个节点上，一定能发现 `p` 和 `q` 位于不同的子树上。

```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr){
            return nullptr;
        }
        // 找到了其中一个节点，停止深入
        if(root == p || root == q){
            return root;
        }

        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        // 递归开始退出...

        // 在左右子树中都找到了 p 或者 q，当前节点就是待寻找的节点
        if(left != nullptr && right != nullptr){
            return root;
        }

        // 如果 left 不为空，说明 left 就是深层递归找到的公共祖先节点
        // 返回即可
        if(left != nullptr){
            return left;
        }

        if(right != nullptr){
            return right;
        }

        // 在左右都没有找到，说明待寻找的节点不在此子树上
        return nullptr;
    }
};
```