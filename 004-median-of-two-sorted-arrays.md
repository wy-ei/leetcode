## 4. Median of Two Sorted Arrays


- 难度： 困难
- 通过率： 24.8%
- 题目链接：[https://leetcode.com/problems/median-of-two-sorted-arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)



### 解法 1

最直接的方法，将两个数组 merge 然后返回中位数。时间复杂度为 `O(m+n)`，需要额外空间存储合并后的数组，空间复杂度为 `O(m+n)`。


```python
class Solution:
    def merge(self, nums1, nums2):
        index_1 = 0
        index_2 = 0
        len_1 = len(nums1)
        len_2 = len(nums2)
        nums = []

        while index_1 < len_1 and index_2 < len_2:
            if nums1[index_1] < nums2[index_2]:
                nums.append(nums1[index_1])
                index_1 += 1
            else:
                nums.append(nums2[index_2])
                index_2 += 1

        while index_1 < len_1:
            nums.append(nums1[index_1])
            index_1 += 1

        while index_2 < len_2:
            nums.append(nums2[index_2])
            index_2 += 1

        return nums

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = self.merge(nums1, nums2)
        nums_len = len(nums)
        if len(nums) % 2 == 0:
            return (nums[nums_len // 2] + nums[nums_len // 2 - 1]) / 2
        else:
            return nums[nums_len // 2]
```


### 解法 2

不合并，直接找到中位数的下标位置，然后返回中位数。

基本思路如下：

1. 根据数组的总长度和长度的奇偶性，得出中位数在合并的数组中的下标。
2. 在一个 while 循环中依次得到有小到大的各个数，在迭代的过程中记录的迭代次数，当迭代次数等于中位数的下标时，记录下中位数。

如果使用这样的循环：

```python
while nums1_index < nums1_len and nums2_index < nums2_len
```

可以保证在循环中两个数组的下标都不会越界，但是在这个循环之后又要使用一个循环，还需要判断哪一个数组还有剩余，代码写的很啰嗦。

如果使用这样的循环：

```python
while nums1_index < nums1_len or nums2_index < nums2_len
```

那么需要在循环中处理某个数组的下标已经超出范围的情况，同样很麻烦。这里使用两个变量 `n1` 和 `n2` 来记录两个数组当前下标指向的元素的值，如果某个下标已经超出范围，那么可以将其设为无穷大，这样以来在之后更新数组下标的步骤就很方便了，因为越界的数组得到的值是无穷大，它的下标就不会被更新。


```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        median_index_1 = 0
        median_index_2 = -1
        median_1 = 0
        median_2 = 0

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        total_len = nums1_len + nums2_len

        if total_len % 2 == 0:
            median_index_1 = total_len // 2 - 1
            median_index_2 = total_len // 2
        else:
            median_index_1 = total_len // 2

        i = 0
        nums1_index = 0
        nums2_index = 0
        while nums1_index < nums1_len or nums2_index < nums2_len:
            n1 = nums1[nums1_index] if nums1_index < nums1_len else float('inf')
            n2 = nums2[nums2_index] if nums2_index < nums2_len else float('inf')

            if n1 < n2:
                num = n1
                nums1_index += 1
            else:
                num = n2
                nums2_index += 1

            if i == median_index_1:
                median_1 = num
                if total_len % 2 == 1:
                    return median_1

            if i == median_index_2:
                median_2 = num
                return (median_1 + median_2) / 2

            i += 1
```


### 解法 3

这个解法的思路来自于<a href="https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation">这里</a>，这个方法可谓精妙。

其思想是找到一个 i 和 j 将数组 A 和 B 分为左右两部分，A 和 B 的左半部分的总长度等于 A 和 B 的右半部分的总长度的时候，中位数就一定存在于 `max(left_part)` 和 `min(right_part)` 中。

```python
      left_A             |        right_A
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]


      left_B             |        right_B
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
```

另外通过 i 和 j 切分后的左右两部分满足以下条件（为了便于理解，暂不考虑数组总长度的奇偶性问题）：

```python
A[i-1] <= B[j]
B[j-1] <= A[i]
i + j == half_length
```

当数组总长度是奇数时，切分后的左右两部分的总长度会相差 1，为了能够从 `max(left_part)` 中取得中位数，需要保证前半部分的长度稍长。因此让 `half_length = (m + n + 1) // 2`，对于总长度为偶数的情况，也能得到正确的结果。

因此 `j = half_length - i`，为了保证 `j` 大于零，需要让 `i < half_length`，为此只需要让 `i` 作为稍短的数组的下标即可。

在 `[0, m]` 范围内确定一个 `i`，会存在下面三种情况：

1. `B[j-1] > A[i]`: 说明 i 还不够大，且合适的 i 一定存在于 `(i, m]` 范围内
2. `A[i-1] > B[j]`: 说明 i 过大，且合适的 i 存在于 `[0, i)` 范围内
2. `B[j-1] <= A[i] and A[i-1] <= B[j]`：以上两个条件都不满足，自然满足这一条了。这个时候就已经找到了合适的 i 和 j 了。

因此可以给 i 初始化一个范围 `i_min = 0` 和 `i_max = m` 然后使用二分法，在每次迭代中更新 `i_min` 或者 `i_max`。


```python
class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(A) > len(B):
            A, B = B, A

        m = len(A)
        n = len(B)
        half_len = (m + n + 1) // 2

        i_min = 0
        i_max = m

        while True:
            i = i_min + (i_max - i_min) // 2
            j = half_len - i
            if i < m and A[i] < B[j - 1]:
                i_min = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                i_max = i - 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2
```