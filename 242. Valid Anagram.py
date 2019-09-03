'''
字符串s & t ，判断 t 是否是 s 的字母异位词
eg:
    s = "anagram", t = "nagaram"    => true
    s = "rat", t = "car"            => false

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

Note:
    You may assume the string contains only lowercase alphabets.

Follow up:
    What if the inputs contain unicode characters? 
    How would you adapt your solution to such case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len=len(s)
        t_len=len(t)
        if s_len!=t_len:
            return False

        s_map={}
        for i in range(0,s_len):
            s_map[s[i]]=s_map.get(s[i],0)+1

        for j in range(0,t_len):
            if s_map.get(t[j],0)!=0:
                s_map[t[j]]-=1
            else:
                return False
        return True

    def isAnagram2(self,s,t):
        s_len=len(s)
        t_len=len(t)
        if s_len!=t_len:
            return False

        s_map={}
        for i in range(0,s_len):
            s_map[s[i]]=s_map.get(s[i],0)+1
            s_map[t[i]]=s_map.get(t[i],0)-1

        for counter in s_map.values():
            if counter<0:
                return False
        return True


if __name__ == '__main__':

    s = "anagram"
    t = "nagaram"

    # s = "rat"
    # t = "car" 

    # s = "abbac"
    # t = "cbaba"

    # s = "abbac"
    # t = "cbaac"

    solution = Solution()
    result=solution.isAnagram2(s,t)
    print(result)








