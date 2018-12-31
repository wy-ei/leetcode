## 27. Remove Element


- 难度： 简单
- 通过率： 42.8%
- 题目链接：[https://leetcode.com/problems/remove-element](https://leetcode.com/problems/remove-element)



### 解法 1：

简单，但缺点是容易出现没必要的赋值。

```python
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    for num in nums:
        if num != val:
            nums[i] = num
            i += 1
    return i
```

### 解法 2：

看看别人写的代码，真是自愧不如。遇到 val 就把数组最后一个元素换过来，然后缩短数组长度。

```python
def removeElement(self, nums, val):
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return n
```