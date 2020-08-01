---
title: 求多个区间的最大重合数量
layout: post
category: 总结
qid: note_00731
---

这一题不是 leetcode 上的，是我在笔试中遇到的一个问题，在此总结一下。

问题描述：

小明选了 n 门在线课程，课程 `i` 开始和结束时间分别为 `s[i]` 和 `e[i]`。小明可以一心多用，可以同时打开多少个播放器窗口来上课，问小明在上完这些课程的过程中，最多需要打开多少个窗口。 

这个问题的本质是：给定了 n 个区间，问重合区间的数量最大是多少。

## 思路一

每门课开始的时候，我打开一个窗口，每门课结束的时候我关闭一个窗口。如果能够记录下每个时刻窗口的增量（可正可负），然后以时间顺序累加此增量，就可以得到每个时刻的窗口数量了。

如果时间范围比较小，而且比较稠密，可以使用数组以时间为下标来存储增量。否则，可以使用 tree map 来存储（因为后面要按照时间顺序遍历）。

```c++
struct Interval{
    int start;
    int end;
};

int max_overlapped_interval_count(const vector<Interval>& intervals){
    map<int, int> mp;
    for(const Interval& item: intervals){
        mp[item.start] += 1;
        mp[item.end] -= 1;
    }

    int res = 0;
    int n = 0;
    for(auto & item : mp){
        n += item.second; // 增量
        res = max(res, n);
    }
    return res;
}
```

## 思路二

如果把起点和终点都放到数轴上来观察，从数轴的最左边向右边遍历，遇到一个起点，我就需要打开一个播放器窗口，遇到一个终点我就关闭一个窗口。可见，在遍历数轴上所有点的过程中，可以得到最多需要打开的窗口数量。

```c++
enum POINT_TYPE{
    START, END
};

struct Point{
    Point(int v, POINT_TYPE t): val(v), type(t){}
    int val;
    POINT_TYPE type;
};

int max_overlapped_interval_count(const vector<Interval>& intervals){
    vector<Point> points;

    for(const Interval& item: intervals){
        points.emplace_back(item.start, START);
        points.emplace_back(item.end, END);
    }

    sort(points.begin(), points.end(), [](const Point& a, const Point& b){
        if(a.val < b.val){
            return true;
        }else if(a.val > b.val){
            return false;
        }else{
            return a.type == END && b.type == START; // 让终点排在前面
        }
    });

    int res = 0;
    int n = 0;
    for(auto & point : points){
        if(point.type == START){
            n += 1;
        }else{
            n -= 1;
        }
        res = max(res, n);
    }
    return res;
}
```

这里如果在同一个点上存在区间起点和终点，那么先处理终点，然后处理起点。也就是先关闭播放器窗口，在打开窗口，然后再更新打开窗口的最大数量。

另外 leetcode 上原题 {% include post_link qid="16.1" %} 和本题其实是一样的，可以使用上面的思路去解答。不过这一题中在 sort 的时候，需要把起点放在前面。