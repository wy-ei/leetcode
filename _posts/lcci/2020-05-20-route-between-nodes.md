---
title: 节点间通路
qid: 04.01
tags: [图]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/route-between-nodes-lcci/](https://leetcode-cn.com/problems/route-between-nodes-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。</p>

<p><strong>示例1:</strong></p>

<pre><strong> 输入</strong>：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
<strong> 输出</strong>：true
</pre>

<p><strong>示例2:</strong></p>

<pre><strong> 输入</strong>：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
<strong> 输出</strong> true
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>节点数量n在[0, 1e5]范围内。</li>
	<li>节点编号大于等于 0 小于 n。</li>
	<li>图中可能存在自环和平行边。</li>
</ol>


## 解法一：深度优先搜索

采用深度优先搜索即可。我为有向图实现了一个类 `DiGraph`，`DiGraph.adj(n)` 返回图中与 n 相连的其他节点。

```c++
class Solution {
public:
    bool findWhetherExistsPath(int n, vector<vector<int>>& graph, int start, int target) {
        DiGraph directed_graph(graph);
        unordered_set<int> seen_nodes;
        return is_path_exists(graph, seen_nodes, start, target);
    }

    bool is_path_exists(const DiGraph& graph, unordered_set<int> &seen_nodes, int start, int target){
        for(int n: graph.adj(start)){
            if(n == target){
                return true;
            }
            if(seen_nodes.find(n) == seen_nodes.end()){
                seen_nodes.insert(n);
                bool ret = is_path_exists(graph, seen_nodes, n, target);
                if(ret){
                    return true;
                }
            }
        }
        return false;
    }
};
```

也可以采用广度优先搜索，使用一个队列即可。

```c++
class Solution {
public:
    bool findWhetherExistsPath(int n, vector<vector<int>>& graph, int start, int target) {
        DiGraph directed_graph(graph);
        unordered_set<int> seen_nodes;
        queue<int> nodes;
        
        nodes.push(start);
        seen_nodes.insert(start);
        
        while(!nodes.empty()){
            int len = nodes.size();
            for(int i=0;i<len;i++){
                int node = nodes.front();
                nodes.pop();
                if(node == target){
                    return true;
                }
                for(int v: directed_graph.adj(node)){
                    if(seen_nodes.find(v) == seen_nodes.end()){
                        nodes.push(v);
                        seen_nodes.insert(v);
                    }
                }
            }
        }
        return false;
    }
};
```