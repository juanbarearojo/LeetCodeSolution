"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

"""
# Intuition
The problem at hand is about computing the n-th number in the Tribonacci sequence, which is a variation of the Fibonacci sequence. In the Tribonacci sequence, each number is the sum of the preceding three numbers, starting with 0, 1, and 1.

# Approach
To solve this problem, we will use a dynamic programming approach similar to how Fibonacci numbers are often computed. We start by initializing an array with the first three numbers of the sequence: [0, 1, 1]. We then iterate from the third index up to `n`, at each step computing the next number as the sum of the previous three numbers in the array. This ensures that each Tribonacci number is computed based on the values of the three preceding numbers.

For special cases:
- If `n` is 0, we return 0.
- If `n` is 1 or 2, we return 1, since these are the values of the first few Tribonacci numbers.

# Complexity
- Time complexity: O(n). The algorithm involves a single loop from 3 to `n`, where each iteration involves a constant amount of work.
- Space complexity: O(n). The space complexity is linear due to the use of an array to store the Tribonacci numbers up to `n`.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        a = [0,1,1]
        i = 2
        while i < n:

            nn = a[i] + a[i-1] + a[i-2]
            i+=1
            a.append(nn)
        return nn
        