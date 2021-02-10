'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
----------------------------------------------------------------------------------------------
Example:

>>> Input: l1 = [2,4,3], l2 = [5,6,4]
>>> Output: [7,0,8]

Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize a ListNode and mark it as the current node as well as the start node
        curr_node = ListNode()
        start = curr_node
        curr_digit = 0
        carry_digit = 0
        end = False
 
        
        if l1 == None and l2 == None:
            return None
        
        while end == False:
            if l1 == None and l2 == None:
                curr_digit = carry_digit
            elif l1 == None:
                curr_digit = l2.val + carry_digit
                l2 = l2.next
            elif l2 == None:
                curr_digit = l1.val + carry_digit
                l1 = l1.next
            else:
                curr_digit = l1.val + l2.val + carry_digit
                l1 = l1.next
                l2 = l2.next
            
            carry_digit = curr_digit//10
            curr_digit = curr_digit%10
            
            curr_node.val = curr_digit
            if l1 == None and l2 == None and carry_digit == 0:
                end = True
            else:
                curr_node.next = ListNode()
                curr_node = curr_node.next
        
        return start
        
