'''
是否存在i & j => nums[i]==nums[j]  && |i-j|<=k

Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
```
Input: nums = [1,2,3,1], k = 3
Output: true
```

Example 2:
```
Input: nums = [1,0,1,1], k = 1
Output: true
```

Example 3:
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        
        n_set=set()
        i=0
        j=0
        while i<n and j<n:
            if nums[j] not in n_set:
                n_set.add(nums[j])
                j+=1
            else:
                t = j-i
                if t<=k:
                    return True
                else:
                    n_set.remove(nums[i])
                    i+=1
        return False

        
if __name__ == '__main__':

    # nums=[1,2,3,1]
    # k=3

    # nums = [1,0,1,1]
    # k = 1

    # nums = [1,2,3,1,2,3]
    # k = 2

    nums = [2,2]
    k = 3

    solution = Solution()
    result = solution.containsNearbyDuplicate(nums,k)
    print(result)


