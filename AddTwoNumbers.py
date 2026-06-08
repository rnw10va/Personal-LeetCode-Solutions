"""
Problem Name: 2. Add Two Numbers
Problem Link: https://leetcode.com/problems/add-two-numbers/submissions/1220441791/
Problem Description:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#My Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        returnHead = ListNode((l1.val + l2.val) % 10)
        remainder = (l1.val + l2.val) // 10
        currentNode1 = l1
        currentNode2 = l2
        currentNodeReturn = returnHead
        while currentNode1.next and currentNode2.next:
            currentNode1 = currentNode1.next
            currentNode2 = currentNode2.next
            currentNodeReturn.next = ListNode((currentNode1.val + currentNode2.val + remainder) % 10)
            remainder = (currentNode1.val + currentNode2.val + remainder) // 10
            currentNodeReturn = currentNodeReturn.next
        while currentNode1.next: 
            currentNode1 = currentNode1.next
            currentNodeReturn.next = ListNode((currentNode1.val + remainder) % 10)
            remainder = (currentNode1.val + remainder) // 10
            currentNodeReturn = currentNodeReturn.next
        while currentNode2.next:
            currentNode2 = currentNode2.next
            currentNodeReturn.next = ListNode((currentNode2.val + remainder) % 10)
            remainder = (currentNode2.val + remainder) // 10
            currentNodeReturn = currentNodeReturn.next
        if remainder == 1:
            currentNodeReturn.next = ListNode(1)
        return returnHead