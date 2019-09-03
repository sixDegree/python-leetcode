'''
判断数组在k间距内是否存在两个差值小于t的元素
( if exist i & j => |nums[i]-nums[j]|<=t  && |i-j|<=k)

Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

Example 2:
```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

Example 3:
```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```
'''

class Solution:
    # Time Limit Exceeded
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        n = len(nums)
        if n<=1 or k==0:
            return False

        # [10,15,18,24]
        for i in range(0,n):
            for j in range(i+1,n):
                if j-i>k:
                    break
                if nums[j]>=(nums[i]-t) and nums[j]<=(nums[i]+t): 
                    return True
        return False

    # 定义桶的大小是t+1
    # nums[i]//(t+1)决定放入几号桶,这样在一个桶里面的任意两个的绝对值差值都<=t
    def containsNearbyAlmostDuplicate2(self,nums,k,t):
        n = len(nums)
        if n<=1 or k==0 or t<0:
            return False

        bucket = {}
        for i in range(0,n):
            b = nums[i]//(t+1)  # 放入哪个桶
            if b in bucket:     # 桶中已经有其他元素,若放nums[i]进去满足差值<=t,直接返回True（如此，前后桶的元素最多也只能有一个）
                return True
            if (b-1) in bucket and abs(nums[i]-bucket[b-1])<=t:
                return True
            if (b+1) in bucket and abs(nums[i]-bucket[b+1])<=t:
                return True
            
            bucket[b]=nums[i]
            if i>=k:
                bucket.pop(nums[i-k]//(t+1))
        return False


    # def containsNearbyAlmostDuplicate3(self,nums,k,t):
    #     n = len(nums)
    #     if n<=1 or k==0 or t<0:
    #         return False

    #     from binarySearchTree import BinarySearchTree 

    #     bst = BinarySearchTree()
    #     for i in range(0,n):
    #         v = bst.floor(nums[i])
    #         if v is not None and nums[i]-v.key<=t:
    #             return True
    #         v = bst.ceil(nums[i])
    #         if v is not None and v.key-nums[i]<=t:
    #             return True
    #         bst.insert(nums[i])
    #         if i>=k:
    #             bst.remove(nums[i-k])
    #     return False
            

if __name__ == '__main__':

    # nums = [1,0,1,1]
    # k = 1
    # t = 2

    # nums = [1,5,9,1,5,9]
    # k = 2
    # t = 3

    # nums = [1,2]
    # k = 0
    # t = 1

    # nums = [7,1,3]
    # k = 2
    # t = 3

    nums = [10,15,18,24]
    k = 3
    t = 3


    solution =  Solution()
    result = solution.containsNearbyAlmostDuplicate3(nums,k,t)
    print(result)


