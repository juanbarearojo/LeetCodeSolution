"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        sm = 0
        a = 0
        while a < len(s):
            cond = a < len(s) - 1
            if s[a] == 'I' and cond:
                if s[a + 1] == 'V':
                    sm += 4
                    a += 2
                elif s[a + 1] == 'X':
                    sm += 9
                    a += 2
                else:
                    sm += 1
                    a += 1
            elif s[a] == 'I':
                sm += 1
                a += 1
            elif s[a] == 'V':
                sm += 5
                a += 1
            # Añadir los demás casos
            elif s[a] == 'X':
                if cond and s[a + 1] == 'L':
                    sm += 40
                    a += 2
                elif cond and s[a + 1] == 'C':
                    sm += 90
                    a += 2
                else:
                    sm += 10
                    a += 1
            elif s[a] == 'L':
                sm += 50
                a += 1
            elif s[a] == 'C':
                if cond and s[a + 1] == 'D':
                    sm += 400
                    a += 2
                elif cond and s[a + 1] == 'M':
                    sm += 900
                    a += 2
                else:
                    sm += 100
                    a += 1
            elif s[a] == 'D':
                sm += 500
                a += 1
            elif s[a] == 'M':
                sm += 1000
                a += 1
        return sm
