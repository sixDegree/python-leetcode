'''

字符串S & P，在S中找出P的异序词（字母相同但顺序可不同的子串），数组形式返回所有找到的异序词在S中起始索引
eg:
    s: "cbaebabacd" p: "abc" => cba,bac     => [0,6]
    s: "abab"       p: "ab"  => ab,ba,ab    => [0,1,2]
    s: "abab"       p: "aba" => aba         => [0]

Given a string s and a non-empty string p, 
find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only 
and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

```
Input:      s: "cbaebabacd" p: "abc"
Output:     [0, 6]
Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
```

Example 2:
```
Input:      s: "abab" p: "ab"
Output:     [0, 1, 2]
Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
```
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n=len(s)
        if n==0:
            return []
        
        m=len(p)
        p_map={}
        sub_map={}
        # for i in range(0,26):
        #     p_map[chr(i+97)]=0
        #     sub_map[chr(i+97)]=0
        for c in p:
            p_map[c]=p_map.get(c,0)+1

        ret=[]
        i,j=0,0
        while j<n:
            sub_map[s[j]]=sub_map.get(s[j],0)+1
            while sub_map[s[j]]>p_map.get(s[j],0):
                sub_map[s[i]]-=1
                i+=1
            j+=1
            if j-i==m:
                ret.append(i)
        return ret


if __name__ == '__main__':

    s="cbaebabacd"
    p="abc"

    # s="abab"
    # p="ab"

    # s="abab"
    # p="aba"

    solution=Solution()
    result=solution.findAnagrams(s,p)
    print(result)
