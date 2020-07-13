---
title: 课程表
qid: 207
tags: [深度优先搜索,广度优先搜索,图,拓扑排序]
---


- 难度： 中等
- 通过率： 35.9%
- 题目链接：[https://leetcode-cn.com/problems/course-schedule](https://leetcode-cn.com/problems/course-schedule)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>现在你总共有 <em>n</em> 门课需要选，记为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>。</p>

<p>在选修某些课程之前需要一些先修课程。&nbsp;例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: <code>[0,1]</code></p>

<p>给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 2, [[1,0]] 
<strong>输出: </strong>true
<strong>解释:</strong>&nbsp;总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> 2, [[1,0],[0,1]]
<strong>输出: </strong>false
<strong>解释:</strong>&nbsp;总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>输入的先决条件是由<strong>边缘列表</strong>表示的图形，而不是邻接矩阵。详情请参见<a href="http://blog.csdn.net/woaidapaopao/article/details/51732947" target="_blank">图的表示法</a>。</li>
	<li>你可以假定输入的先决条件中没有重复的边。</li>
</ol>

<p><strong>提示:</strong></p>

<ol>
	<li>这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。</li>
	<li><a href="https://www.coursera.org/specializations/algorithms" target="_blank">通过 DFS 进行拓扑排序</a> - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。</li>
	<li>
	<p>拓扑排序也可以通过&nbsp;<a href="https://baike.baidu.com/item/%E5%AE%BD%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2/5224802?fr=aladdin&amp;fromid=2148012&amp;fromtitle=%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2" target="_blank">BFS</a>&nbsp;完成。</p>
	</li>
</ol>


## 解法一：

课程之间互相依赖，构成一个有向图。只要这个有向图中没有环，即不存在循环依赖，那么所有课程都能够修完。

遍历图，并记录下图中节点是否访问过，当一个节点被两次访问到的时候，说明存在环。遍历使用 DFS 或者 BFS 均可。这里我使用了两个标记 `visited` 和 `onstack`，其中 `visited[i] = true` 表示节点 i 在某次遍历中访问过了，而 `onstack[i] = true` 表示节点 i 在本次深度优先遍历中访问过了。

因为深度优先遍历要从所有的顶点都进行一次，只有在其中一次深度优先遍历中发现某个点被访问多次，才证明存在环。另外，其中一个点可能会指向另外一个子图，之前这个子图可能已经遍历过了，如果不使用 `visited` 来标记，就会重复遍历。

```cpp
class Solution {
private:
    bool has_cycle = false;
    unordered_map<int, unordered_set<int>> graph;
    vector<bool> visited;
    vector<bool> onstack;
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        graph.clear();
        graph.reserve(numCourses);
        visited.resize(numCourses);
        onstack.resize(numCourses);

        for(auto& edge: prerequisites){
            int w = edge[0];
            int v = edge[1];
            graph[v].insert(w);
        }

        for(auto & item : graph){
            int v = item.first;
            if(!visited[v]){
                dfs(v);
            }
        }
        return !has_cycle;
    }

private:
    void dfs(int v){
        visited[v] = true;
        onstack[v] = true;
        unordered_set<int> &nodes = graph[v];
        for(int w: nodes){
            if(has_cycle){
                return;
            }
            if(!visited[w]){
                dfs(w);
            }else if(onstack[w]){
                has_cycle = true;
            }
        }
        onstack[v] = false;
    }
};
```

## 解法二：

先把那些不需要前驱课程的课修了，然后进一步修依赖这些课的其他课程，而后继续。最后判断能够修的课程和全部课程是否相等。

不需要前驱课程，就是图中入度为 0 的点。当一个入度为 0 的点，消除后，该点指向的节点的入度就减 1，那么节点如果入度减为 0，那就可以进一步消除其他节点。

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, int> in_degrees(numCourses);
        unordered_map<int, unordered_set<int>> graph(numCourses);
        for(auto& item: prerequisites){
            graph[item[1]].insert(item[0]);
            in_degrees[item[0]] += 1;
        }

        queue<int> zero_dep_queue;
        for(int i=0;i<numCourses;i++){
            if(in_degrees[i] == 0){
                zero_dep_queue.push(i);
            }
        }

        int count = 0;
        while (!zero_dep_queue.empty()){
            int w = zero_dep_queue.front();
            zero_dep_queue.pop();
            count += 1;

            for(int v: graph[w]){
                in_degrees[v] -= 1;
                if (in_degrees[v] == 0){
                    zero_dep_queue.push(v);
                }
            }
        }

        return count == numCourses;
    }
};
```