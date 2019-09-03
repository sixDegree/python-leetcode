'''
find three integers in nums such that the sum is closest to target. 
eg:
    nums = [-1, 2, 1, -4], target = 1 => 3 numbers: -1+2+1=2 => 2

---- 

Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:

```
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
'''

import math

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if n<3:
            return 

        min_diff=math.inf
        closet_t=0

        for k in range(0,n-2):
            x = nums[k]
            i = k+1
            j = n-1
            while i < j:
                t = x+nums[i]+nums[j]
                diff = t-target
                if diff < 0:
                    i+=1
                elif diff > 0:
                    j-=1
                else:
                    return target
                if abs(diff)<min_diff:
                    min_diff=abs(diff)
                    closet_t=t
        return closet_t



if __name__ == '__main__':

    nums = [-1, 2, 1, -4]
    target=1
    target=0
    target=2

    solution = Solution()
    result = solution.threeSumClosest(nums,target)
    print(result)


        