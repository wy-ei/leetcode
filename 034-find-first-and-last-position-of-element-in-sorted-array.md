## 34. Find First and Last Position of Element in Sorted Array

- 难度： 中等
- 通过率： 32.6%
- 题目链接：[https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个按照升序排列的整数数组 <code>nums</code>，和一个目标值 <code>target</code>。找出给定目标值在数组中的开始位置和结束位置。</p>

<p>你的算法时间复杂度必须是&nbsp;<em>O</em>(log <em>n</em>) 级别。</p>

<p>如果数组中不存在目标值，返回&nbsp;<code>[-1, -1]</code>。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 8
<strong>输出:</strong> [3,4]</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 6
<strong>输出:</strong> [-1,-1]</pre>


### 解法：

使用二分查找来寻找上界和下界。和二分查找不同之处在于找到 target 之后，需要判断 mid 是不是上下界，如果不是就继续更新 lo 或者 hi。

```python
class Solution:
    
    def lower_bound(self, nums, target):
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid
            else:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    hi = mid

        return -1
    
    def upper_bound(self, nums, target):
        lo = 0
        hi = len(nums)
        length = len(nums)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid
            else:
                if mid + 1 == length or nums[mid + 1] > target:
                    return mid + 1
                else:
                    lo = mid + 1

        return -1
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        lower_bound = self.lower_bound(nums, target)
        
        if lower_bound == -1:
            return [-1, -1]
        
        upper_bound = self.upper_bound(nums, target)

        return [lower_bound, upper_bound - 1]
```

### 寻找上下界

在 C++ 算法模块中存在 `lowe_bound` 和 `upper_bound` 这两个函数，它们都位于二分查找类别下。在[这里](http://www.cplusplus.com/reference/algorithm/lower_bound/)看到了 `lower_bound` 的一种写法：

```c++
template <class ForwardIterator, class T>
ForwardIterator lower_bound (ForwardIterator first, ForwardIterator last, const T& val){
    ForwardIterator it;
    iterator_traits<ForwardIterator>::difference_type count, step;
    count = distance(first,last);
    while (count>0){
        it = first;
        step=count/2;
        advance (it,step);
        
        if (*it<val) {                 // or: if (comp(*it,val)), for version (2)
            first=++it;
            count-=step+1;
        }
        else{
            count=step;
        }
    }
    return first;
}
```

感觉这段代码写的更好一些，我把它改写成 python 如下： 

```python
def lower_bound(nums, target):
    count = len(nums)
    lo = 0
    while count > 0:
        step = count // 2
        mid = lo + step
        
        if nums[mid] < target:
            lo = mid + 1
            count -= step + 1
        else:
            count = step
    return lo
```

它采用的策略是使用不同的步长，拿数组中间位置元素和 target 比较，如果小于 target，那么更新 `lo=mid+1`，并减小搜索区间长度。如果不小于 target，就将步长减半。直到最后最后区间长度为 0，这个时候 lo 指向的就是 `lower_bound`。

