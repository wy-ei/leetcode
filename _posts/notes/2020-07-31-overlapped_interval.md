---
title: 求多个区间的最大重合数量
layout: post
category: 总结
---

问题描述：

小明选了 n 门在线课程，每门课程的开始和结束时间为 `(s[i], e[i])`，小明可以一心多用，问小明最多需要同时打开多少个播放器窗口才能顺利地上完这些课程。 

这个问题的本质是：给定了 n 个区间，问重合的区间的最大数量是多少。


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

int max_overlapped_interval_count1(const vector<Interval>& intervals){
    vector<Point> points;
    
    for(const Interval& item: intervals){
        points.emplace_back(item.start, START);
        points.emplace_back(item.end, END);
    }
    
    sort(points.begin(), points.end(), [](const Point& a, const Point& b){
        return a.val < b.val;
    });

    int res = 0;
    int n = 0;
    for(int i = 0; i< points.size(); i++){
        if(points[i].type == START){
            n += 1;
        }else{
            n -= 1;
        }
        // 同一时刻有可能会存在多个区间的起点和终点，因此需要把某个点上的
        // 起点和终点都处理完成，然后再更新最大重叠数量
        if(i > 0 && points[i].val != points[i-1].val){
            res = max(res, n);
        }
    }
    res = max(res, n);
    return res;
}
```