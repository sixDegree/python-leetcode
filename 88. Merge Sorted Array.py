'''

2个有序数组，有序地归并到第一个数组中

Given two sorted integer arrays nums1 and nums2, 
merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        k=(m+n)-1

        while k>=0 and i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
            k-=1
            
        if j<0:
            nums1[:k+1]=nums1[:i+1]
        elif i<0:
            nums1[:k+1]=nums2[:j+1]


if __name__ == '__main__':
     nums1=[1,2,3,8,10,0,0,0,0]
     nums2=[2,5,6,7]
     m=5
     n=4

     # nums1=[1]
     # nums2=[]
     # m=1
     # n=0

     # nums1=[0]
     # nums2=[1]
     # m=0
     # n=1

     solution = Solution()
     solution.merge(nums1,m,nums2,n)
     print(nums1)

        