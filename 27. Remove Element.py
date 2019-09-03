'''

将数组中所有等于v的元素删除，返回不重复元素length，且可遍历数组获取不重复元素(不管超过length的数组元素)
eg: 
    nums=[3,2,2,3], val = 3                 => 2, nums=[2,2,...]
    nums = [0,1,2,2,3,0,4,2], val = 2       => 5, nums=[0,1,3,0,4,....]

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

```
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
```

Example 2:

```
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
```

Clarification:

Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```
'''

class Solution(object):
    
    # [0,k) 存储非val元素，[k,n) 存储val元素
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        k=0
        for i in range(0,n):
            if nums[i]!=val:
                # if i!=k:
                #     nums[i],nums[k]=nums[k],nums[i]
                nums[k]=nums[i]
                k+=1
        return k

    def removeElement2(self,nums,val):
        n=len(nums)
        for i in range(n-1,-1,-1):
            if nums[i]


if __name__=="__main__":
    nums=[0,1,2,2,3,0,4,2]
    solution=Solution()
    
    result=solution.removeElement(nums,2)
    print(result,nums)

    for i in range(0,result):
        print(nums[i],end=", ")
    print()



        