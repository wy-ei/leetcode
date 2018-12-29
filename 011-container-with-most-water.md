## 11. Container With Most Water


- 难度： 中等
- 通过率： 41.0%
- 题目链接：[https://leetcode.com/problems/container-with-most-water](https://leetcode.com/problems/container-with-most-water)



### 解法：

```python
class Solution:
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(heights) - 1
        max_area = 0

        while lo < hi:
            width = hi - lo
            min_height = min(heights[lo], heights[hi])
            area = width * min_height

            if area > max_area:
                max_area = area

            if heights[lo] > heights[hi]:
                hi -= 1
            else:
                lo += 1

        return max_area
```