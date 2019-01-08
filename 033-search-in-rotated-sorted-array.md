## 33. Search in Rotated Sorted Array

- 难度： 中等
- 通过率： 32.5%
- 题目链接：[https://leetcode.com/problems/search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>假设按照升序排序的数组在预先未知的某个点上进行了旋转。</p>

<p>( 例如，数组&nbsp;<code>[0,1,2,4,5,6,7]</code>&nbsp;可能变为&nbsp;<code>[4,5,6,7,0,1,2]</code>&nbsp;)。</p>

<p>搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>你可以假设数组中不存在重复的元素。</p>

<p>你的算法时间复杂度必须是&nbsp;<em>O</em>(log&nbsp;<em>n</em>) 级别。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 0
<strong>输出:</strong> 4
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 3
<strong>输出:</strong> -1</pre>


### 解法 1

在 leetcode 上看到这个[解答](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple)，非常简洁，深深被折服。

数组可以分为两段，其中前一段大于后一段，先确定需要查询的数它在那一段。如果在前半段，就让后半段的值为无穷大。如果在后半段，那就让前半段为无穷小。这样以来整个数组依然可以做是有序数组，可以进行二分查找。

具体的做法就是在取 `nums[mid]` 的值时，分三种情况：

1. 如果 `nums[mid]` 和 target 处于同一段，那就取实际值 `nums[mid]`
2. target 处于前一段，而 `nums[mid]` 处于后一段，那么取 inf
3. target 处于后一段，而 `nums[mid]` 处于前一段，那么取 -inf

```python
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    inf = float('inf')

    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        # nums[mid] and target on the same side
        if (target < nums[0]) == (nums[mid] < nums[0]):
            num = nums[mid]
        else:
            if target < nums[0]:
                num = -inf
            else:
                num = inf

        if num < target:
            lo = mid + 1
        elif num > target:
            hi = mid - 1
        else:
            return mid

    return -1
                    
```

### 解法 2

target 和 `nums[mid]` 的位置有以下几种情况：

当 target 和`nums[mid]` 在同一侧时：

- 当 `nums[mid]` > target 时，需要调小 hi，即 hi = mid
- 当 `nums[mid]` < target 时，需要增大 lo，即 lo = mid + 1
- 当 `nums[mid]` == target 时，就得到了结果  
    
当 target 和`nums[mid]` 不在同一侧时：

- target 在左，`nums[mid]` 在右，需要调小 hi，即 hi = mid
- target 在右，`nums[mid]` 在左，需要调大 lo，即 lo = mid + 1

```python
def search(nums, target):
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) // 2

        # nums[mid] and target on the same side
        if (nums[mid] < nums[0]) == (target < nums[0]):
            if (nums[mid] < target):
                lo = mid + 1
            elif (nums[mid] > target):
                hi = mid
            else:
                return mid
        elif target < nums[0]:
            lo = mid + 1
        else:
            hi = mid

    return -1
```

### 关于二分查找

在二分查找中 `lo` 初始化为 0，对 `hi` 的初始化有两种方案，不同的方案 while 条件写法也不同


当 hi 为 `len(nums)` 时，`hi` 是当前有效范围的上边界，这个时候 while 循环有效条件是 `lo < hi`

```python
lo = 0
hi = len(nums)

while lo < hi:
    pass
```

当 hi 为 `len(nums) - 1` 时，`hi` 是当前有效范围中最后一个元素的下标，这个时候 while 循环的有效条件是 `lo <= hi`

```python
lo = 0
hi = len(nums)

while lo <= hi:
    pass
```

另外在求 mid 值得时候，常见的有下面这量种方法：

```python
mid = lo + (hi - lo) // 2

mid = (lo + hi) // 2
```

其实在 python 中往往显示不出区别来，但是在 C/C++ 中，第二种写法中的 `lo + hi` 可能会导致整数溢出，因此推荐使用第一种写法。