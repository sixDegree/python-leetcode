'''
数组排序，只有0／1/2 3种元素值

Given an array with n objects colored red, white or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

Follow up:

```
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, 
then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
```
'''

class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        
        # 三路快排，只遍历一遍即可
        # [0,lt) = 0, [lt,gt) = 1, [gt,n) = 2
        lt=-1
        gt=n
        i=0
        while i<gt:
            if nums[i]==1:
                i+=1
            elif nums[i]<1:
                if i!=lt+1:
                    nums[lt+1],nums[i]=nums[i],nums[lt+1]
                lt+=1
                i+=1
            elif nums[i]>1:
                if i!=gt-1:
                    nums[gt-1],nums[i]=nums[i],nums[gt-1]
                gt-=1



if __name__=='__main__':
    
    nums=[2,0,2,1,0,2,1,0]

    solution = Solution()
    solution.sortColors(nums)
    print(nums)



        