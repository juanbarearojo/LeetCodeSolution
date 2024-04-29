"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r =""
        c = True
        min_l = min(len(s) for s in strs)
        for i in range(min_l):
            if c == False:
                break
            cha = strs[0][i]
            for s in strs:
                if s[i] != cha:
                    c = False
                    break
            if c == True:
                r +=cha
        return r