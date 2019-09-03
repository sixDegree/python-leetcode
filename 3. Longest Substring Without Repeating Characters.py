'''
找没有重复字母的最长子串
eg:
    "abcabcbb"  =>  3
    "bbbbb"     =>  1
    "pwwkew"    =>  3
    " "         =>  1

Given a string, find the length of the longest substring without repeating characters.

Example 1:

```
Input: "abcabcbb"
Output: 3 
Explanation: 
    The answer is "abc", with the length of 3. 
```

Example 2:

```
Input: "bbbbb"
Output: 1
Explanation: 
    The answer is "b", with the length of 1.
```

Example 3:

```
Input: "pwwkew"
Output: 3
Explanation: 
    The answer is "wke", with the length of 3. 
    Note that the answer must be a substring, 
    "pwke" is a subsequence and not a substring.
```
'''

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        sub_seq=set()
        sub_len=0
        max_len=0

        i=0
        for j in range(0,n):
            if s[j] not in sub_seq:
                sub_seq.add(s[j])
                sub_len+=1
                # print(max_len,sub_len,s[i:j+1])     # [i,j]
                max_len=max(max_len,sub_len)
            else:
                while s[i]!=s[j]:
                    sub_seq.remove(s[i])
                    sub_len-=1
                    i+=1
                i+=1
        return max_len
        

    def lengthOfLongestSubstring2(self, s):
        n=len(s)
        sub_seq=set()
        sub_len=0
        max_len=0

        i=0
        j=0
        while i<n and j<n:
            if s[j] not in sub_seq:
                sub_seq.add(s[j])
                sub_len+=1
                j+=1
                # print(max_len,sub_len,s[i:j+1])   # [i,j]
                max_len=max(max_len,sub_len)
            else:
                sub_seq.remove(s[i])
                sub_len-=1
                i+=1
        return max_len

    def lengthOfLongestSubstring3(self,s):
        n=len(s)
        sub_seq={}                          # dict - char:pos - record each char last pos
        max_len=0
        
        i=0
        for j in range(0,n):
            if s[j] in sub_seq:
                i=max(i,sub_seq[s[j]]+1)    # locat i directly
            # print(max_len,i,j,s[i:j+1])   # [i,j]
            max_len=max(max_len,j-i+1)
            sub_seq[s[j]]=j
        return max_len


if __name__ == '__main__':

    # s="abcabcbb"
    # s="bbbbb"
    # s="pwwkew"
    # s="au"
    # s="tmmzuxt"
    # s=" "
    # s="abba"

    solution = Solution()
    # result = solution.lengthOfLongestSubstring4(s)
    # print(result)

    cases={"abcabcbb":3,"bbbbb":1,"pwwkew":3,"au":2,"tmmzuxt":5," ":1,"abba":2}
    for s,e in cases.items():
        print("case:",s,"expect:",e)
        result = solution.lengthOfLongestSubstring3(s)
        print("result:",result)
        assert(result==e)
        print("---"*10)


