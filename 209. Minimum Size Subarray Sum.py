'''
找`sum >= T`的最短连续子数组，返回此子数组长度
eg:
    nums = [2,3,1,2,4,3], T = 7 => [4,3]>=7   => 2

Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 
```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
```
Explanation: 
the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''

class Solution(object):
    
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0

        i=0
        j=0
        sub_sum=0
        sub_len=0    
        min_len=n
        found=False
        while i<n:
            if sub_sum<s and j<n:
                sub_sum+=nums[j]
                sub_len+=1
                j+=1
            else:
                sub_sum-=nums[i]
                sub_len-=1
                i+=1

            if sub_sum>=s:
                found=True
                # print(min_len,sub_len,nums[i:j])
                min_len=min(min_len,sub_len)
       
        if not found:
            return 0
        else:
            return min_len
    

    def minSubArrayLen2(self, s, nums):
        n=len(nums)
        i=0
        sub_sum=0
        sub_len=0
        min_len=n+1
        
        for j in range(0,n):
            sub_sum+=nums[j]
            sub_len+=1
            while sub_sum>=s:
                min_len=min(min_len,sub_len)
                sub_sum-=nums[i]
                sub_len-=1
                i+=1

        return 0 if min_len>n else min_len
        


if __name__ == '__main__':

    # s = 7
    # nums = [2,3,1,2,4,3]
    # [2,3,1,2,4,3]
    #  2,3,1,2,j
    #    3,1,2,4,j
    #      1,2,4,j
    #        2,4,3,j
    #          4,3,j


    # s = 7
    # nums = [2]
    # nums = [8]

    # s = 4
    # nums = [1,4,4]

    # s = 3
    # nums = [1,1]

    
    solution = Solution()
    result = solution.minSubArrayLen2(s,nums)
    print(result)


