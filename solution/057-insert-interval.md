## 57. Insert Interval

- 难度： 困难
- 通过率： 30.4%
- 题目链接：[https://leetcode.com/problems/insert-interval](https://leetcode.com/problems/insert-interval)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给出一个<em>无重叠的 ，</em>按照区间起始端点排序的区间列表。</p>

<p>在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>输出:</strong> [[1,5],[6,9]]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> intervals = <code>[[1,2],[3,5],[6,7],[8,10],[12,16]]</code>, newInterval = <code>[4,8]</code>
<strong>输出:</strong> [[1,2],[3,10],[12,16]]
<strong>解释:</strong> 这是因为新的区间 <code>[4,8]</code> 与 <code>[3,5],[6,7],[8,10]</code>&nbsp;重叠。
</pre>


## 解法：

这道题的难度被定为 hard，我开始不以为然，然后自己上手编了一下，提交了 5 次才成功，而且代码修修补补写的很烂。主要问题在于没有看透此问题的本质，因此用了一些笨办法。


下面是 LeetCode 上 StefanPochmann 的解法：[7+ lines, 3 easy solutions](https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions)，这段代码实在是太帅了。


```python
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, new_interval):
        left = []
        right = []
        start, end = new_interval.start, new_interval.end
        for interval in intervals:
            if interval.end < start:
                left.append(interval)
            elif interval.start > end:
                right.append(interval)
            else:
                start = min(interval.start, start)
                end = max(interval.end, end)
                

        return left + [Interval(start, end)] + right
```

下面的解法会直观一点，先处理相交区间之前的子区间，然后合并区间，最后处理相交区间后面的子区间。

```python
class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        ret = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i][1] < new_interval[0]:
            ret.append(intervals[i])
            i += 1
            
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(intervals[i][0], new_interval[0])
            new_interval[1] = max(intervals[i][1], new_interval[1])
            i += 1
        ret.append(new_interval)
        
        while i < n:
            ret.append(intervals[i])
            i += 1
        
        return ret
```


### 启发：

某些解法需判断两个区间是否重叠，下面这段代码用来做这件事，相当优雅。

```python
if max(start_1, start_2) <= min(end_1, end_2):
    return True
else:
    return False
```

```
----  -----
```

观察不相交的区间的特征，`max_left > min_right`，根据这个特征就可以很容易地判断两个区间是否相交。