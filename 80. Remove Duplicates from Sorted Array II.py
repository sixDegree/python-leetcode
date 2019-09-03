'''
有序数组去重，每个最多保留2个，返回元素length，且可遍历数组获取这些元素(不管超过length的数组元素)
eg:
    [1,1,1,2,2,3]               => 5, [1,1,2,2,3]
    [0,0,1,1,1,1,2,3,3]         => 7, [0,0,1,1,2,3,3]


Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

```
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.
```

Example 2:

```
Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
It doesn't matter what values are set beyond the returned length.
```

Clarification:

Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        k=1
        cnt=1
        for i in range(1,n):
            if nums[i]==nums[i-1] and cnt<2:
                nums[k]=nums[i]
                k+=1
                cnt+=1
            elif nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
                cnt=1
            
        return k
        

if __name__=="__main__":

    nums=[0,0,0,1,1,1,1,2,3,3]
    # nums=[1,1,1,2,2,3]
    solution=Solution()
    
    result=solution.removeDuplicates(nums)
    print(result,nums)
    
    for i in range(0,result):
        print(nums[i],end=", ")
    print()

