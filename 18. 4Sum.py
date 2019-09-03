'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ret=[]

        for l in range(0,n-3):
            if l>0 and nums[l]==nums[l-1]:
                continue
            for k in range(l+1,n-2):
                if k>l+1 and nums[k]==nums[k-1]:
                    continue
                x = nums[l]+nums[k]
                i=k+1
                j=n-1
                t = target-x
                while i<j:
                    if nums[i]+nums[j] < t:
                        i+=1
                    elif nums[i]+nums[j] > t:
                        j-=1
                    else:
                        ret.append([nums[l],nums[k],nums[i],nums[j]])
                        #print(nums[l],nums[k],nums[i],nums[j])
                        i+=1
                        j-=1
                        # 去重
                        while i<n and nums[i]==nums[i-1]:
                            i+=1
                        while j>0 and nums[j]==nums[j+1]:
                            j-=1
        return ret



if __name__ == '__main__':

    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    # [[-1,  0, 0, 1],[-2, -1, 1, 2],[-2,  0, 0, 2]]
    
    nums = [0, 0, 0, 0]
    target = 0
    # [[0,0,0,0]]

    nums = [-1,0,1,2,-1,-4]
    target = -1
    # [[-4,0,1,2],[-1,-1,0,1]]
    # -4,-1,-1,0,1,2

    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11


    solution = Solution()
    result = solution.fourSum(nums,target)
    print(result)


