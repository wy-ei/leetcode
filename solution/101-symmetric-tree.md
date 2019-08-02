## 101. Symmetric Tree

- 难度： 简单
- 通过率： 42.2%
- 题目链接：[https://leetcode.com/problems/symmetric-tree](https://leetcode.com/problems/symmetric-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，检查它是否是镜像对称的。</p>

<p>例如，二叉树&nbsp;<code>[1,2,2,3,4,4,3]</code> 是对称的。</p>

<pre>    1
   / \
  2   2
 / \ / \
3  4 4  3
</pre>

<p>但是下面这个&nbsp;<code>[1,2,2,null,3,null,3]</code> 则不是镜像对称的:</p>

<pre>    1
   / \
  2   2
   \   \
   3    3
</pre>

<p><strong>说明:</strong></p>

<p>如果你可以运用递归和迭代两种方法解决这个问题，会很加分。</p>


## 解法：

2019-8-2 21:58:16

**解法一**

第一个想到的解法是进行层次遍历，然后检查每一层是否为回文数组，这肯定是可行的。


**解法二**

对二叉树根节点的左右子树进行遍历，对左子树先访问左节点，对右子树先访问右节点，由此得到两组元素，然后比较这两组元素是否完全相同。如果对称，那么这两个数组会是相同的。

需要注意的一点是，当某个孩子为 null 的时候，需要返回一个值来进行占位。

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        all_left = self.traversal(root.left, first='left')
        all_right = self.traversal(root.right, first='right')

        for left, right in zip(all_left, all_right):
            if left != right:
                return False
                
        return True
        
    def traversal(self, node, first):
        if not node:
            return ['']

        items = [node.val]

        if first == 'left':
            items += self.traversal(node.left, first=first)
            items += self.traversal(node.right, first=first)
        else:
            items += self.traversal(node.right, first=first)
            items += self.traversal(node.left, first=first)
            
        return items
```

这个方法返回了全部元素，然后进行比较，需要占用额外的空间。另外很多时候，二叉树很早就已经不对称了，对后面的遍历都不再必要了。此方法，不够好。


**方法三**

方法二的缺点是要遍历完整二叉树，且需要花费空间。如果可以把对根节点的左右子树的遍历，写成一个迭代器。这样就可以在发现不对称后立刻停止，且不需要花费额外空间。

这里使用 Python 的生成器很方便地实现了上述想法：


```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left_iter = self.make_iter(root.left, 'left')
        right_iter = self.make_iter(root.right, 'right')

        for left, right in zip(left_iter, right_iter):
            if left != right:
                return False
                
        return True
    
    def make_iter(self, root, first):
        if not root:
            yield ''
            return
        
        yield root.val
        
        if first == 'left':
            yield from self.make_iter(root.left, first)
            yield from self.make_iter(root.right, first)
        else:
            yield from self.make_iter(root.right, first)
            yield from self.make_iter(root.left, first)

```

**方法四**


如果不使用生成器，要想对两棵树进行遍历，并在遍历中进行比较。这需要遍历过程是非递归的。这里采用层次遍历是个不错的选择：

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left_queue = [root.left]
        right_queue = [root.right]
        
        while left_queue and right_queue:
            left = left_queue.pop(0)
            right = right_queue.pop(0)
            
            if left == None and right == None:
                continue
                
            if (left == None) ^ (right == None):
                return False
            
            if left.val != right.val:
                return False
                
            left_queue.extend([left.left, left.right])
            right_queue.extend([right.right, right.left])
            
        return True
```

**方法五**

此问题还可以这样考虑，根节点的左子树的左孩子和根节点的右子树的右孩子对称，且根节点的左子树的右孩子和根节点的右子树的左孩子也对称，那么整个树就对称。

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self._is_symmetric(root.left, root.right)
    
    def _is_symmetric(self, left, right):
        if (left == None) and (right == None):
            return True
        
        if (left == None) ^ (right == None):
            return False
        
        if left.val != right.val:
            return False
        
        return self._is_symmetric(left.left, right.right) \
                and self._is_symmetric(left.right, right.left)
```