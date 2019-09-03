'''
规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律
eg:
    pattern = "abba", str = "dog cat cat dog"   => True
    pattern = "aaaa", str = "dog cat cat dog"   => False

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, 
such that there is a bijection between a letter in pattern 
and a non-empty word in str.

Example 1:
```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

Example 2:
```
Input: pattern = "abba", str = "dog cat cat fish"
Output: false
```

Example 3:
```
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```

Example 4:
```
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```

Notes:
    You may assume pattern contains only lowercase letters, 
    and str contains lowercase letters that may be separated by a single space.

'''

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        p_len=len(pattern)
        s_list=s.split()
        s_len=len(s_list)

        if p_len!=s_len:
            return False
        if p_len == 0:
            return True

        p_map={}
        s_map={}
        for i in range(0,p_len):
            if pattern[i] not in p_map:
                p_map[pattern[i]]=s_list[i]
            if s_list[i] not in s_map:
                s_map[s_list[i]]=pattern[i]
            if p_map[pattern[i]]!=s_list[i] or s_map[s_list[i]]!=pattern[i]:
                return False
        return True

if __name__ == '__main__':

    pattern = "abba"
    s = "dog cat cat dog"

    pattern = "abba"
    s = "dog cat cat fish"

    pattern = "aaaa"
    s = "dog cat cat dog"

    pattern = "abba"
    s = "dog dog dog dog"

    solution = Solution()
    result = solution.wordPattern(pattern,s)
    print(result)

