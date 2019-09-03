'''

判断数组中是否存在相同元素

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

class Solution:
    def containsDuplicate(self, nums):
        n = len(nums)

        n_set=set()
        for i in range(0,n):
            if nums[i] in n_set:
                return True
            else:
                n_set.add(nums[i])
        return False


if __name__ == '__main__':

    nums = [1,2,3,1]
    nums = [1,2,3,4]
    nums = [1,1,1,3,3,4,3,2,4,2]

    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)


