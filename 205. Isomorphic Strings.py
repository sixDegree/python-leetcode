'''
两个字符串 s 和 t，判断它们是否是同构

eg:
    s = "egg", t = "add"        => True
    s = "foo", t = "bar"        => False
    s = "paper", t = "title"    => True
    s = "ab", t = "ab"          => True
    s = "ab", t = "aa"          => False
    s = "ba", t = "aa"          => False
     

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character 
while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:
```
Input: s = "egg", t = "add"
Output: true
```

Example 2:
```
Input: s = "foo", t = "bar"
Output: false
```

Example 3:
```
Input: s = "paper", t = "title"
Output: true
```

Note:
    You may assume both s and t have the same length.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len=len(s)
        t_len=len(t)
        
        if s_len!=t_len:
            return False
        if s_len<=1:
            return True

        s_map={}
        t_map={}
        for i in range(0,s_len):
            if s[i] not in s_map:
                s_map[s[i]]=t[i]
            if t[i] not in t_map:
                t_map[t[i]]=s[i]
            # print(s[i],t[i],s_map,t_map)
            if s_map[s[i]]!=t[i] or t_map[t[i]]!=s[i]:
                return False
        return True


if __name__ == '__main__':

    # s = "egg"
    # t = "add"

    # s = "foo"
    # t = "bar"

    # s = "paper"
    # t = "title"
    # s_map = p:t,a:i,e:l,r:e
    # t_map = t:p,i:a,l:e,e:r

    # s = "ab"
    # t = "aa"
    # s_map = a:a,b:a
    # t_map = a:a.a:b

    # s = "ba"
    # t = "aa"

    # s = "ab"
    # t = "ab"
    

    solution = Solution()
    result = solution.isIsomorphic(s,t)
    print(result)








