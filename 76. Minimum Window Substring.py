'''
字符串S & T，在S中找到包含T中所有字母的最短子串
eg:
    s="ADOBECODEBANC",      t="ABC"     => "BANC"
    s="cabwefgewcwaefgcf",  t="cae"     => "cwae"
    s="abab",               t="aba"     => "aba"
    s="aa",                 t="a"       => ""
    s="a",                  t="a"       => "a"


Given a string S and a string T, 
find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

Note:
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        n=len(s)
        m=len(t)
        if m>n:
            return ""

        t_map={}
        for c in t:
            t_map[c]=t_map.get(c,0)+1

        sub_map={}
        min_len=n+1
        min_str=""
        min_map={n+1:1}   # {min_len: occur_cnt}

        match_len=0
        i,j=0,0
        while i<n and j<n:
            sub_map[s[j]]=sub_map.get(s[j],0)+1
            if sub_map[s[j]]<=t_map.get(s[j],0):
                match_len+=1
            j+=1
            while match_len==m:
                if sub_map[s[i]]==t_map.get(s[i],0):
                    # print(min_len,j-i,s[i:j],min_map)
                    if min_len>=j-i:
                        min_len=j-i
                        min_str=s[i:j]
                        min_map[min_len]=min_map.get(min_len,0)+1
                    match_len-=1
                sub_map[s[i]]-=1
                i+=1

        # print("min_map:",min_map,"min_len:",min_len,"min_str:",min_str)
        return min_str if min_map[min_len]==1 else ""
            


# ADOBECODEBANC : ABC => BANC
# ADOBEC
#  DOBEC
#  DOBECODEBA
#       ODEBA
#       ODEBANC
#          BANC

# ADOBEC
# 111111
# 100101
 

if __name__ == '__main__':

    s="ADOBECODEBANC"
    t="ABC"

    s="cabwefgewcwaefgcf"
    t="cae"

    # s="abab"
    # t="aba"

    # s="aa"
    # t="a"

    # s="a"
    # t="a"

    solution=Solution()
    result=solution.minWindow(s,t)
    print(result)

