## Partition

荷兰旗问题，三向切分，把数组分为三部分，`[< pivot, = pivot, > pivot]`


```cpp
void partition(vector<int>& nums){
    if (nums.size() <= 1){
        return;
    }

    int pivot = nums[0];
    int small = 0, equal = 0, large = nums.size();
    while(equal < large){
        if(nums[equal] < pivot){
            swap(nums[equal++], nums[small++]);            
        }
        else if(nums[equal] == pivot){
            equal ++;
        }
        else{
            swap(nums[equal], nums[--large]);
        }
    }
}
```
