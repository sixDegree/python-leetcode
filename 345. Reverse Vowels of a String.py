'''
翻转一个字符串中的元音字母

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

```
Input: "hello"
Output: "holle"
```

Example 2:

```
Input: "leetcode"
Output: "leotcede"
```

Note:

The vowels does not include the letter "y".
'''
class Solution(object):

    def __init__(self):
        # a e i o u
        self.volwelSet={'a','e','i','o','u','A','E','I','O','U'}

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n==0 or n==1:
            return s

        i=0
        j=n-1
        retS=list(s) # 'str' object does not support item assignment
        while i<j:
            si=retS[i] in self.volwelSet
            sj=retS[j] in self.volwelSet
            if not si:
                i+=1
            elif not sj:
                j-=1
            else:
                retS[i],retS[j]=retS[j],retS[i]
                i+=1
                j-=1
        return "".join(retS)


        
if __name__ == '__main__':

    # s = "hello"
    s = "leetcode"
    
    solution=Solution()
    result=solution.reverseVowels(s)
    print(result)
