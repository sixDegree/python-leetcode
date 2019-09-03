'''
Given an array of integers, 
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        index_map={}    # { nums[i]:i }
        target_map={}   # { nums[i]:t }

        for i in range(0,n):
            x,t = nums[i], target-nums[i]
            if x not in target_map:
                target_map[x]=t
                index_map[x]=i
            if t in target_map and i!=index_map[t]:
                return [index_map[t],i]
        return []

    def twoSum2(self,nums,target):
        n = len(nums)
        nums_map = {}   # { nums[i]:index }
        for i in range(0,n):
            x,t = nums[i],target-nums[i]
            if t in nums_map:
                return [nums_map[t],i]
            nums_map[x]=i
        return []


        
if __name__ == '__main__':

    nums = [2, 7, 11, 15]
    target = 9

    nums = [3,2,4]
    target = 6


    solution = Solution()
    result = solution.twoSum(nums,target)
    print(result)

