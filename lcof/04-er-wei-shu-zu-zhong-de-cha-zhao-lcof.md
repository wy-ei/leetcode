## 04. 二维数组中的查找

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<p>现有矩阵 matrix 如下：</p>

<pre>[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
</pre>

<p>给定 target&nbsp;=&nbsp;<code>5</code>，返回&nbsp;<code>true</code>。</p>

<p>给定&nbsp;target&nbsp;=&nbsp;<code>20</code>，返回&nbsp;<code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= n &lt;= 1000</code></p>

<p><code>0 &lt;= m &lt;= 1000</code></p>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 240 题相同：<a href="https://leetcode-cn.com/problems/search-a-2d-matrix-ii/">https://leetcode-cn.com/problems/search-a-2d-matrix-ii/</a></p>



## 解法一：线性查找

观察前面例子中的矩阵，如果从左上角开始搜索，如果目标值大于左上角的数，那么后续查询方向就有两个，左边或者下边。同理，如果从右下角开始查，移动的方向也有两个。但是从另外两个角查起，就完全不同了。假设我们从右上角开始寻找，要找的目标是 9，因为 15 > 9，那么唯一的选择就是向左移动，因为 15 下面的可能大于 9，所以最右边的那一列都被排除了。11 同理，11 所在的列也完全被排除了，因为这一列肯定都大于 9。往左移动到 7，由于 7 < 9，因此只能向下寻找，而且 7 所在行可以完全排除掉了。向下寻找，很快就找到了。

查找过程就是根据情况向下或者向左寻找，一旦触及左边或者下边的边界，而且要突破边界，那就说明没有找到。同样的道理，也可以从左下角找起，道理相同，不在叙述。这个算法的时间复杂度就是 O(m+n)。

```c++
class Solution {
public:
    bool Find(const vector<vector<int>>& array, int target) {
      if(array.empty() || array[0].empty()){
        return false;
      }
      int row = array.size(), col = array[0].size();
      int x = 0, y = col-1;
    
      while(x < row && y >= 0){
        if(array[x][y] < target){
          x += 1;
        }else if(array[x][y] > target){
          y -= 1;
        }else{
          return true;
        }
      }

      return false;
    }
};
```

## 解法二：二分查找

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

再次观察这个例子，还假设我们寻找的是 9。可以轻易地发现，最后两列是可以排除的，因为这两列中最小的元素都已经大于了 9。我们还可以发现最后两行也可以排除，因为这两行最小的元素也都大于 9。因此余下的内容就是下面这些：


```
[
  [1,   4,  7],
  [2,   5,  8],
  [3,   6,  9]
]
```

不难发现，前两列可以排除掉，因为这两列中最大的元素都小于 9。同样的，由于前两行中最大的元素都小于 9，于是前两行也可以排除。

通过上面的分析，可以总结出规律：通过观察每一列开头元素，可以排除掉大于目标值的列。通过观察每一列的结尾，可以排除小于目标值的列。相同地，观察行的开头和结尾也可以排除掉不可能存在目标值的行。


如下例子中，如果查询的数是 9，由于数组中可能存在多个待查找的值，使用前面的方法缩小范围，永远也不可能把范围缩小到 1，因为去掉了最后一行之后，就再也没法排除了。而此时其实待查找的值就落在余下范围的角上，因此在缩小范围的过程中，要不断地检查副对角线上的两个角的值。

```
[
  [5, 6, 9],
  [9, 10,11],
  [11,14,18]
]
```

基于以上分析，可以给行和列维护一个范围，交替从不同方向缩小范围，并不断检查左下角和右上角的值。这里涉及到的查找，可以使用二分查找法。在行上查找一次的时间复杂度是 O(logM)，需要在行上查找多少次呢，因为待查找的行平均每次缩小一半，因此 logN 次，列就缩减完了。因此行上的查找会进行，logN 次，由此推算时间复杂度是 O(logN * logM)。


```python
import numpy as np

def upper_bound(nums, x):
    """
    find the first element great than x in a sorted list
    return the index of this element
    """
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def lower_bound(nums, x):
    """
    find the first element that is not less than x (i.e. greater or equal to)
    """
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def Find(self, matrix, x):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
            
        row_lo, row_hi = 0, len(matrix)
        col_lo, col_hi = 0, len(matrix[0])

        matrix = np.array(matrix)
        while (row_lo < row_hi) and (col_lo < col_hi):
            if matrix[row_hi-1][col_lo] == x or matrix[row_lo][col_hi-1] == x:
                return True

            row_hi = upper_bound(matrix[:, col_lo], x)
            col_hi = upper_bound(matrix[row_lo], x)

            row_lo = lower_bound(matrix[:, col_hi-1], x)
            col_lo = lower_bound(matrix[row_hi-1], x)

        return False
```

以上代码需要说明一下，`lower_bound` 和 `upper_bound` 的作用是在一个排序数组中，寻找某个范围的上下界。比如 `nums = [1,3,5,5,5,7]`，这里 5 出现了 3 次，构成了一个范围。`lower_bound(nums, 5)` 会返回第一个 5 的下标，这是范围的起始下标。而 `upper_bound(nums, 5)` 会返回 7 的下标，这是范围的终止下标，这里采用的是左闭右开的区间表示法。

因此在代码中，寻找下界的时候，要使用 `lower_bound`，寻找上界的时候会使用 `upper_bound`。当待查找的值不在数组中时，两者返回的结果相同，即第一个大于查询值的数的下标。