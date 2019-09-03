'''
求2个数组的公共元素，以数组形式返回(不去重)
eg:
    [1,2,2,1], [2,2]        => [2,2]
    [4,9,5],   [9,4,9,8,4]  => [4,9]

Given two arrays, write a function to compute their intersection.

Example 1:
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

Example 2:

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums1)
        m=len(nums2)
        if n==0 or m==0:
            return []
        if n>m:
            nums1,nums2=nums2,nums1

        nums_map={}
        for i in range(len(nums1)):
            nums_map[nums1[i]]=nums_map.get(nums1[i],0)+1

        ret=[]
        for i in range(0,len(nums2)):
            if nums_map.get(nums2[i],0)>0:
                ret.append(nums2[i])
                nums_map[nums2[i]]-=1
        return ret
        
if __name__=='__main__':

    # nums1=[1,2,2,1]
    # nums2=[2,2]

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    solution=Solution()
    result=solution.intersect(nums1,nums2)
    print(result)