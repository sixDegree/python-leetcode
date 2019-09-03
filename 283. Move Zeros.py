'''
所有0挪到数组末尾，其他非0元素相对位置保持不变
eg: [0,1,0,3,12] => [1,3,12,0,0,0]

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:

- Input: [0,1,0,3,12]
- Output:[1,3,12,0,0]

Note:

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.
'''


class Solution:

    # 挑出所有非0元素放到[0,...,k)，余下的[k,...n)都置0
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=0
        for i in range(0,n):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,n):
            nums[i]=0

    # 遍历数组，i,k 交换，将非0元素置换到［0,k)
    def moveZeroes2(self,nums): # quicker - recommend
        n=len(nums)
        k=0
        for i in range(0,n):
            if nums[i]!=0:
                if i!=k:
                    nums[k],nums[i]=nums[i],nums[k]
                k+=1


    def moveZeroes3(self,nums): # not maintain the relative order !
        l,r=0,len(nums)-1
        while l<r:
            while nums[l]!=0 and l<r:
                l+=1
            while nums[r]==0 and l<r:
                r-=1
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1



if __name__ == '__main__':

    nums=[7,0,1,0,3,0,12,0,5,0]
    solution = Solution()
    solution.moveZeroes3(nums)
    print(nums)





        