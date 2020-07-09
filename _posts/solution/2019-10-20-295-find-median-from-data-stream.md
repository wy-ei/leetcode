---
title: 数据流的中位数
qid: 295
tag: [堆, 设计]
---

- 难度： 困难
- 通过率： 33.6%
- 题目链接：[https://leetcode-cn.com/problems/find-median-from-data-stream](https://leetcode-cn.com/problems/find-median-from-data-stream)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。</p>

<p>例如，</p>

<p>[2,3,4]&nbsp;的中位数是 3</p>

<p>[2,3] 的中位数是 (2 + 3) / 2 = 2.5</p>

<p>设计一个支持以下两种操作的数据结构：</p>

<ul>
	<li>void addNum(int num) - 从数据流中添加一个整数到数据结构中。</li>
	<li>double findMedian() - 返回目前所有元素的中位数。</li>
</ul>

<p><strong>示例：</strong></p>

<pre>addNum(1)
addNum(2)
findMedian() -&gt; 1.5
addNum(3) 
findMedian() -&gt; 2</pre>

<p><strong>进阶:</strong></p>

<ol>
	<li>如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？</li>
	<li>如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？</li>
</ol>


## 思路：

在一个输入流中，实时地计算已经输出的数字的中位数。如果维护一个有序的序列，那么获取中位数很简单，但是插入就相当费时间。

换种想法，如果能够把所有数分为两部分 A 和 B，保证 `A <= B`，且 `A.size() == B.size()` 或 `A.size() == B.size() + 1`。那么利用 A 中的最大值和 B 中的最小值，就能计算出中位数了。

大顶堆和小顶堆，就能够完成此任务。对于流中的数，我们分别把它们插入到 A 和 B 两个堆中，保证满足上面提到的堆大小的要求。

对于输出 `num`，如果要向 `A` 中加入元素的时候，为了保证 `A <= B`，先把 `num` 插入到 `B` 中，然后把 `B` 中的最小值插入 `A` 中。当需要向 `B` 中加入值时，就先把 `num` 加入 `A` 中，然后把 `A` 中的最大值插入 `B` 中。采用这种方法，把每个输入都加入到堆中。

获取中位数就相当简单了，如果总数是奇数，那就返回 `A` 中的最大值。否则返回 `A` 中最大值和 `B` 中最小值的均值。也就是两个堆的堆顶元素的均值。

## 解法

```c++
class MedianFinder {
public:
    MedianFinder(){}

    void addNum(int num) {
        if(max_pq.size() == min_pq.size()){
            min_pq.push(num);
            max_pq.push(min_pq.top());
            min_pq.pop();
        }else{
            max_pq.push(num);
            min_pq.push(max_pq.top());
            max_pq.pop();
        }
    }

    double findMedian() {
        if(max_pq.size() == min_pq.size()){
            return (max_pq.top() + min_pq.top()) / 2.0;
        }else{
            return max_pq.top();
        }
    }

private:
    priority_queue<int> max_pq;
    priority_queue<int, vector<int>, greater<>> min_pq;
};
```