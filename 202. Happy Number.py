'''
起始一个给定的正整数，循环计算结果整数的每个数字的平方和，直到变为1，则为一个快乐数，返回true

eg:
    19
    =>
        1*1 + 9*9 = 82
        8*8 + 2*2 = 68
        6*6 + 8*8 = 100
        1*1 + 0*0 + 0*0 = 1
    => True

    29 => 85, 89, 145, 42, 20, 4, 16, 37, 58, 89 => False
    
    7 => 49, 97, 130, 10, 1 => True


slow = 19 ; fast = 82
slow = 82 ; fast = 68, fast = 100
slow = 68 ; fast = 1, fast = 1

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True

        s_map={}
        for i in range(0,10):
            s_map[str(i)]=i*i

        s_set=set()
        s_set.add(n)
        s = str(n)
        while True:
            target = sum(s_map[i] for i in s)
            # print(target)
            if target == 1:
                return True
            if target in s_set:
                return False
            s_set.add(target)
            s = str(target)


if __name__ == '__main__':

    # n = 19

    n = 29

    # n = 7

    solution = Solution()
    result = solution.isHappy(n)
    print(result)

    






