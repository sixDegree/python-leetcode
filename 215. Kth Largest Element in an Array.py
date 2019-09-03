'''
求数组中第K大的元素

Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

Example 2:

```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

Note: 

You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        return self.find(nums,0,n,k-1)

    def partition(self,nums,l,r):
        # [l,gt]    >  v
        # [gt+1,r)  <= v
        v=nums[l]
        gt=l
        for i in range(l+1,r):
            if nums[i]>v:
                nums[i],nums[gt+1]=nums[gt+1],nums[i]
                gt+=1
        # [l,gt) < v
        # [gt] = v
        # [gt,r) >=v
        nums[l],nums[gt]=nums[gt],nums[l]
        return gt

    def find(self,nums,l,r,k):
        gt=self.partition(nums,l,r)
        if gt>k:
            return self.find(nums,l,gt,k)
        elif gt<k:
            return self.find(nums,gt+1,r,k)
        else:
            return nums[gt]

    def findKthLargest2(self,nums,k):
        import heapq
        
        n=len(nums)
        pq=[]
        for i in range(0,n):
            heapq.heappush(pq,nums[i])
            if i>=k:
                heapq.heappop(pq)
            #print(pq)
        return heapq.heappop(pq)


if __name__ == '__main__':

    nums=[3,2,1,5,6,4]
    k=2

    # nums=[3,2,3,1,2,4,5,5,6]
    # k=4

    solution=Solution()
    result=solution.findKthLargest2(nums,k)
    print(result)


