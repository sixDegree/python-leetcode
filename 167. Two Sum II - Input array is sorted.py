'''
有序数组，找2个数sum为T

Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers 
such that they add up to the target, 
where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            if numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                break;
        return [i+1,j+1]

        

if __name__=="__main__":

    numbers = [2,7,11,15]
    target = 9

    solution = Solution()
    result=solution.twoSum(numbers,target)
    print(result)
    print(numbers[result[0]-1],numbers[result[1]-1])


