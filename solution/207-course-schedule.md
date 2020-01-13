## 207. Course Schedule

- 难度： 中等
- 通过率： 35.9%
- 题目链接：[https://leetcode.com/problems/course-schedule](https://leetcode.com/problems/course-schedule)


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


## 解法：

课程之间互相依赖，构成一个有向图。只要这个有向图中没有环，即不存在循环依赖，那么所有可能都能够修完。

解法一：

使用 dfs 判断图中是否有环：

```cpp
class Solution {
    enum {NOT_VISITED, VISITED};
public:
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        graph.clear();
        graph.reserve(numCourses);
        for(auto& item: prerequisites){
            add_edge(item[0], item[1]);
        }
        return !has_circle();
    }

private:
    bool has_circle(){
        unordered_map<int, int> visited;
        visited.reserve(graph.size());
        for(auto & it : graph){
            visited[it.first] = NOT_VISITED;
            if(dfs(it.first, visited)){
                return true;
            }
        }
        return false;
    }

    void add_edge(int w, int v){
        graph[w].insert(v);
    }

    bool dfs(int w, unordered_map<int, int>& visited){
        if(visited[w] == VISITED){
            return true;
        }
        visited[w] = VISITED;
        unordered_set<int> &nodes = graph[w];
        for(int k: nodes){
            if(dfs(k, visited)){
                return true;
            }
        }
        visited[w] = NOT_VISITED;
        return false;
    }

private:
    unordered_map<int, unordered_set<int>> graph;
};
```

解法二：

先把那些不需要前驱课程的课修了，然后进一步修依赖这些课的其他可能，而后继续。最后判断能够修的课程和全部课程是否相等。

不需要前驱课程，就是图中入度为 0 的点。当一个入度为 0 的点，消除后，该点指向的节点的入度就减 1，那么节点如果入度减为 0，那就可以进一步消除其他节点。

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, int> in_degrees(numCourses);
        unordered_map<int, unordered_set<int>> adj(numCourses);
        for(auto& item: prerequisites){
            in_degrees[item[1]] += 1;
            adj[item[0]].insert(item[1]);
        }

        queue<int> free_node_queue;
        for(int i=0;i<numCourses;i++){
           if(in_degrees[i] == 0){
               free_node_queue.push(i);
           }
        }

        int free_node_count = 0;
        while (!free_node_queue.empty()){
            int w = free_node_queue.front();
            free_node_queue.pop();
            free_node_count += 1;

            for(int v: adj[w]){
                in_degrees[v] -= 1;
                if (in_degrees[v] == 0){
                    free_node_queue.push(v);
                }
            }
        }

        return free_node_count == numCourses;
    }
};
```