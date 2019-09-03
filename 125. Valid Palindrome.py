'''
判断一个字符串是否为回文串（忽略大小写，且只看数字，字母字符）

Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

```
Input: "A man, a plan, a canal: Panama"
Output: true
```

Example 2:

```
Input: "race a car"
Output: false
```
'''
class Solution(object):

    def __init__(self):
        self.charMap={}
        # chr(ord('a')+2) => 'c'
        for i in range(0,10):
            self.charMap[chr(ord('0')+i)]=i
        for i in range(0,26):
            self.charMap[chr(ord('a')+i)]=10+i
            self.charMap[chr(ord('A')+i)]=10+i
        # print(self.charMap)

    def isPalindrome(self,s):
        n=len(s)
        if n==0 or n==1:
            return True

        i=0
        j=n-1
        while i<j:
            si=self.charMap.get(s[i])
            sj=self.charMap.get(s[j])
            # print("s[%d]=%s,s[%d]=%s,%s==%s:%s" % (i,s[i],j,s[j],si,sj,si==sj))
            if si is None:
                i+=1
            elif sj is None:
                j-=1
            elif si==sj:
                i+=1
                j-=1
            else:
                return False
        return True


    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        if n==0 or n==1:
            return True

        i=0
        j=n-1
        while i<j:
            # print("s[%d]=%s,s[%d]=%s,%s" % (i,s[i],j,s[j],s[i]==s[j]))
            if not self.isAlphanumeric(s[i]):
                i+=1
            elif not self.isAlphanumeric(s[j]):
                j-=1
            elif s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True

    def isPalindrome3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        if n==0 or n==1:
            return True

        i=0
        j=n-1
        while i<j:
            while not self.isAlphanumeric(s[i]) and i<j:
                i+=1
            while not self.isAlphanumeric(s[j]) and i<j:
                j-=1

            # print("s[%d]=%s,s[%d]=%s,%s" % (i,s[i],j,s[j],s[i]==s[j]))
            if i==j:
                return True
            elif s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True

    def isAlphanumeric(self, c):
        '''
        ord('A'),ord('a'),ord('0')
        65,97,48
        alpha   => c.lower()-97: [0,26)
        numeric => c.lower()-48: [0,9]
        '''
        c=ord(c.lower())
        if (c-97>=0 and c-97<26) or (c-48>=0 and c-48<=9):
            return True
        else:
            return False



        
if __name__=="__main__" :

    s="A man, a plan, a canal: Panama"
    # s="race a car"
    # s=".,"
    # s=""
    # s="aa"

    solution = Solution()
    result=solution.isPalindrome(s)
    print(result)

