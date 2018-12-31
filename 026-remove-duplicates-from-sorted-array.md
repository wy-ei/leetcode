## 26. Remove Duplicates from Sorted Array


- 难度： 简单
- 通过率： 38.8%
- 题目链接：[https://leetcode.com/problems/remove-duplicates-from-sorted-array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)



### 解法 1

使用一个下标 j 指向数组第一个元素，然后从第二个元素开始和 nums[j] 比较，如果发现不同，那么就要把这个元素放到 j+1 的位置上。这样 j 始终指向数组中个元素 考虑到数组可能无重复，这么做会引起不必要的赋值，所以加一个判断。

```python
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            if j < i:
                nums[j] = nums[i]
    return j + 1
```

### 解法 2：

在[这里](https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11782/Share-my-clean-C%2B%2B-code)看到如下解法，稍作改进如下：

思路是使用一个变量记录下重复的元素个数，这样下标 `i-count` 就是当前未重复的元素的位置了。结果用总长度减去重复元素个数就好了。这个解法真是太厉害了。

```python
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        elif count > 0:
            nums[i - count] = nums[i]

    return len(nums) - count
```