'''
Given an array of strings, group anagrams together.

Example:

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

Note:
    All inputs will be in lowercase.
    The order of your output does not matter.

'''

class Solution(object):

    # Time Limit Exceeded:
    def groupAnagrams(self,strs):
        n = len(strs)
        used=[False]*n
        ret=[]
        for i in range(0,n):
            if used[i]:
                continue

            record=[strs[i]]
            used[i]=True
            for j in range(i+1,n):
                if used[j]:
                    continue
                if self.isAnagram(strs[i],strs[j]):
                    record.append(strs[j])
                    used[j]=True
            ret.append(record)

        return ret

    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False

        s_map={}
        for i in range(len(s)):
            s_map[s[i]]=s_map.get(s[i],0)+1
            s_map[t[i]]=s_map.get(t[i],0)-1
        for cnt in s_map.values():
            if cnt!=0:
                return False
        return True

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_map={}
        for s in strs:
            ss = tuple(sorted(s))
            if ss in str_map:
                str_map[ss].append(s)
            else:
                str_map[ss]=[s]
        return list(str_map.values())

    def groupAngrams3(self,strs):
        str_map={}
        for s in strs:
            cnt=[0]*26
            for c in s:
                cnt[ord(c)-ord('a')]+=1
            ss=tuple(cnt)

            if ss in str_map:
                str_map[ss].append(s)
            else:
                str_map[ss]=[s]
        return list(str_map.values())

    

  
if __name__ == '__main__':

    strs=["eat", "tea", "tan", "ate", "nat", "bat", "nat"]
        
    # strs=["",""]

    solution = Solution()
    # result = solution.isAnagram("eatac","ateab")
    result = solution.groupAnagrams(strs)
    print(result)      


