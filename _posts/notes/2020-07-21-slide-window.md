---
title: 滑动窗口问题套路
layout: post
category: 总结
---

滑动窗口，通常用于寻找某个子序列，比如 {% include post_link qid="3" %}，这类问题通常都有固定的套路，使用 `lo` 和 `hi` 维护一个窗口，初始状态下，`lo = hi = 0`，窗口大小为 0，然后不断地移动窗口右边界，并更新窗口类的状态。当某些条件不满足时，向右滑动左窗口。

## 案例

{% include post_link qid="3" %}

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int lo = 0, hi = 0;
        unordered_set<char> window;
        int max_len = 0;
        while(hi < s.size()){
            char ch = s[hi];
            hi++;
            while(window.count(ch) == 1){
                window.erase(s[lo++]);
            }
            window.insert(ch);
            max_len = max(max_len, hi - lo);
        }
        return max_len;
    }
};
```

## 解题模版

滑动窗口的套路如下：

```c++
int lo = 0, hi = 0;
unordered_set<char> window;

while(hi < nums.size()){
    char n = nums[hi];
    hi++;
    while(/* 需要收缩窗口 */){
        // 缩小窗口
        // 更新窗口信息
        lo ++;
    }
    window.insert(ch);

    //根据窗口信息，更新答案
    max_len = max(max_len, hi - lo);
}
```