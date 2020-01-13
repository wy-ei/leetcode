## 126. Word Ladder II

- 难度： 困难
- 通过率： 16.4%
- 题目链接：[https://leetcode.com/problems/word-ladder-ii](https://leetcode.com/problems/word-ladder-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定两个单词（<em>beginWord</em> 和 <em>endWord</em>）和一个字典 <em>wordList</em>，找出所有从 <em>beginWord </em>到 <em>endWord </em>的最短转换序列。转换需遵循如下规则：</p>

<ol>
	<li>每次转换只能改变一个字母。</li>
	<li>转换过程中的中间单词必须是字典中的单词。</li>
</ol>

<p><strong>说明:</strong></p>

<ul>
	<li>如果不存在这样的转换序列，返回一个空列表。</li>
	<li>所有单词具有相同的长度。</li>
	<li>所有单词只由小写字母组成。</li>
	<li>字典中不存在重复的单词。</li>
	<li>你可以假设 <em>beginWord</em> 和 <em>endWord </em>是非空的，且二者不相同。</li>
</ul>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

<strong>输出:</strong>
[
  [&quot;hit&quot;,&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;cog&quot;],
&nbsp; [&quot;hit&quot;,&quot;hot&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]
]
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

<strong>输出: </strong>[]

<strong>解释:</strong>&nbsp;<em>endWord</em> &quot;cog&quot; 不在字典中，所以不存在符合要求的转换序列。</pre>


## 解法：

可以将所有单词视作图中的节点，两个词语之间如果相差的字符为 1，在图中这两个词之间就存在一条路径。

此问题就变成了类似寻找两个点之间最短路径的问题，不同之处在于这个最短路径可能有很多条。

在图中寻找最短路径的标准解法是广度优先搜索。在搜索过程中，从起点开始，一层一层地向外扩展，直到遇到目标节点。

在搜索过程中需要记录在路径，一般做法就是使用一个 map 来记录下当前点和其前一个点。这样在寻找到终点时，就可以不断地向前查询，直到起点。比如下面的例子从，从 'c' 向前查询，就可以得到序列 `c-->a-->b-->e`

```python
{
    'a': 'b',
    'b': 'e',
    'c': 'a',
}
```

最短路径常常不止一条，本题中要求返回所有的最短路径，因此记录路径的策略就要稍作调整。能到达当前节点的前一层节点可以有多个，因此在 `map` 的值部分可以使用一个 `set` 来记录能到当前节点的所有前一层节点。

```python
{
    'a': {'b'},
    'b': {'e'},
    'c': {'a', 'd'},
    'd': {'b'}
}
```

提前构造图时没有必要的，要想提前造图，需要对各个单词两两计算差异，但在遍历的随着余下的节点的规模减小，计算量也会慢慢下降。

对某个单词寻找差异为 1 的其他单词，直观的做法是和余下的单词一一比较。如果余下的单词的规模为 N，每个单词的长度为 M，时间复杂度为 O(NM) 。另外一种思路是对当前单词进行变换，然后在单词聚合中查询是否存在，这种方法需要查询 26*(M-1) 次散列表，当单词表很大时，这个方法比前一种方法快很多。

```python
from collections import defaultdict

class Solution:
    
    def findLadders(self, begin_word: str, end_word: str, words: List[str]) -> List[List[str]]:
        if end_word not in words:
            return []
        words = set(words + [begin_word])
        
        result = self.search(begin_word, end_word, words)
        
        return result

    def search(self, begin_word, end_word, words):
        children = {begin_word}
        marked = defaultdict(set)
        stop = False
        
        while children and not stop:
            new_children = set()
            words -= children
            
            for word in children:
                for i in range(len(word)):
                    head, tail = word[:i], word[i+1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        w = head + c + tail
                        if w not in words:
                            continue
                            
                        marked[w].add(word)
                        new_children.add(w)
                        
                        if w == end_word:
                            stop = True
                            break

            children = new_children
            
        if end_word not in marked:
            return []
        else:
            return self.decode(begin_word, end_word, marked)
        
    def decode(self, begin_word, end_word, marked):
        result = [[end_word]]
        while result[0][0] != begin_word:
            result = [[w] + req for req in result
                        for w in marked[req[0]]]
        return result
```

当目标单词距离起始点很远的时候，即距离较长时，随着遍历层次的深入，规模也会变得很大。另外一种方法是从两端，同时进行层次遍历。当前后两个层次遍历在某一层相交大的时候，就得到了解。这种方法从两端一起遍历，可以大幅地缩小规模。


```python
# 双端 BFS

from collections import defaultdict

class Solution:
    
    def findLadders(self, begin_word: str, end_word: str, words: List[str]) -> List[List[str]]:
        if end_word not in words:
            return []
        words = set(words + [begin_word])
        
        result = self.search(begin_word, end_word, words)
        
        return result

    def search(self, begin_word, end_word, words):
        forward = {begin_word}
        backward = {end_word}
        is_forward = True
        
        marked = defaultdict(set)
        
        while forward or backward:
            new_children = set()
            if is_forward:
                children = forward
            else:
                children = backward
            
            words -= children
            
            for word in children:
                for i in range(len(word)):
                    head, tail = word[:i], word[i+1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        w = head + c + tail
                        if w not in words:
                            continue
                        
                        if is_forward:
                            marked[w].add(word)
                        else:
                            marked[word].add(w)

                        new_children.add(w)
            
            if is_forward:
                forward = new_children
            else:
                backward = new_children
            
            if forward & backward:
                break

            is_forward = not is_forward

        if end_word not in marked:
            return []
        else:
            return self.decode(begin_word, end_word, marked)
        
    def decode(self, begin_word, end_word, marked):
        result = [[end_word]]
        while result[0][0] != begin_word:
            result = [[w] + req for req in result
                        for w in marked[req[0]]]
        return result
```