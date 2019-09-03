'''
求2个数组的公共元素，以数组形式返回(去重)
eg:
    [1,2,2,1], [2,2]        => [2]
    [4,9,5],   [9,4,9,8,4]  => [4,9]
    

Given two arrays, write a function to compute their intersection.

Example 1:

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

Example 2:

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

Note:
    Each element in the result must be unique.
    The result can be in any order.
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1=set(nums1)
        s2=set(nums2)
        return list(s1&s2)
        

if __name__=='__main__':

    # nums1=[1,2,2,1]
    # nums2=[2,2]

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    solution=Solution()
    result=solution.intersection(nums1,nums2)
    print(result)



