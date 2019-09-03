'''

在数组中找三个数和为0，返回无重复三元祖列表(注意去重)
eg: 
    nums = [-1, 0, 1, 2, -1, -4] ＝> [[-1, 0, 1],[-1, -1, 2]]

--- 

Given an array nums of n integers, 
are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
    The solution set must not contain duplicate triplets.

Example:
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

'''

class Solution(object):

    # 无法去重：
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     print(nums)
    #     n = len(nums)
    #     ret=[]

    #     for i in range(0,n):
    #         x = nums[i]
    #         result=[ [x,r[0],r[1]] for r in self.twoSum(nums,-x,i,n)]
    #         # print(i-1,":",x,result)
    #         ret.extend(result)
    #     return ret

    # def twoSum(self,nums,target,s,n):
    #     target_map = {}
    #     e=nums[s]
    #     for i in range(s+1,n):
    #         x,t = nums[i],target-nums[i]
    #         if t in target_map:
    #             yield t,x
    #         target_map[x]=t

    def threeSum(self,nums):
        # 排序＋对撞指针
        nums.sort()
        # print(nums)
        n = len(nums)

        ret=[]
        for k in range(0,n):
            x = nums[k]
            if x>0:
                break
            if k>0 and x==nums[k-1]: # 去重
                continue
            i=k+1
            j=n-1
            t=-x
            while i<j:
                if nums[i]+nums[j] < t:
                    i+=1
                elif nums[i]+nums[j] > t:
                    j-=1
                else:
                    ret.append([x,nums[i],nums[j]])
                    # print(x,nums[i],nums[j])
                    i+=1
                    j-=1
                    # 去重
                    while i<n and nums[i]==nums[i-1]:
                        i+=1
                    while j>0 and nums[j]==nums[j+1]:
                        j-=1
        return ret



if __name__ == '__main__':

    nums = [-1, 0, 1, 2, -1, -4]

    # [-4,-1,-1,0,1,2]

    nums = [0,0,0,0]

    # [-4, -1, -1, 0, 1, 2]

    solution = Solution()
    result = solution.threeSum(nums)
    print(result)


