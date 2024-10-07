# Problem Name: 2. Add Two Numbers
# Problem Link: https://leetcode.com/problems/add-two-numbers/submissions/1220441791/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
