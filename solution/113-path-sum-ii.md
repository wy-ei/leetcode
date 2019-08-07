## 113. Path Sum II

- 难度： 中等
- 通过率： 38.7%
- 题目链接：[https://leetcode.com/problems/path-sum-ii](https://leetcode.com/problems/path-sum-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。</p>

<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>

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


## 解法：

深度优先遍历，在深入的同时，传入余下的路线应有的 sum。

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        self.dfs(root, [], sum, result)
        return result
        
    def dfs(self, node, nodes, sum):
        if not node:
            return
        
        if not node.left and not node.right and sum == node.val:
            result.append(nodes + [node.val])

        if node.left:
            self.dfs(node.left, nodes + [node.val], sum - node.val, result)
        if node.right:
            self.dfs(node.right, nodes + [node.val], sum - node.val, result)
```