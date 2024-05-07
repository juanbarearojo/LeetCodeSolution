"""
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

 
Example 1:
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

Example 2:
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
 

Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.set_int_max_str_digits(11000)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = ""
        i = head
        while i is not None:
            s += str(i.val)
            i = i.next

        
        a = str(int(s) *2)
        new_head = ListNode(int(a[0]))
        current = new_head
        d = new_head
        for k in a[1:]:
            new_node = ListNode(int(k))
            current.next = new_node
            current = new_node
        return d
