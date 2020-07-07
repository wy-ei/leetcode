---
title: 克隆图
qid: 133
tags: [深度优先搜索,广度优先搜索,图]
---


- 难度： 中等
- 通过率： 25.1%
- 题目链接：[https://leetcode-cn.com/problems/clone-graph](https://leetcode-cn.com/problems/clone-graph)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>克隆一张无向图，图中的每个节点包含一个&nbsp;<code>val</code>&nbsp;和一个&nbsp;<code>neighbors</code>&nbsp;（邻接点）列表 。</p>




## 解法：

使用一个 map 来记录原节点和新节点的映射，然后使用 dfs 来进行 clone。遇到一个节点的时候，如果未克隆过，就克隆该节点并记录在 map 中，如果此节点已经 clone 过了，那么直接从 map 中得到克隆的节点。

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new = self.clone(node, {})
        return new
            
    def clone(self, node, mp):
        new = Node(node.val, [])
        mp[node] = new
        
        for neighbor in node.neighbors:
            if neighbor not in mp:
                neighbor = self.clone(neighbor, mp)
            else:
                neighbor = mp[neighbor]
                
            new.neighbors.append(neighbor)
        return new
```

也可以使用 bfs 来搞定。

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new = Node(node.val, [])
        mp = {node: new}        
        queue = [node]
        
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor not in mp:
                    mp[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                mp[node].neighbors.append(mp[neighbor])

        return new
```