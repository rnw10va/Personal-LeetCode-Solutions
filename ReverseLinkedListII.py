# Problem Name: 92. Reverse Linked List II
# Problem Link: https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        arrayToMatch = []
        current = head
        while count <= right:
            if left <= count <= right:
                arrayToMatch.append(current)
            elif count == left - 1:
                leftOfLeftVal = current
            current = current.next
            count+=1
        last = current
        current = arrayToMatch.pop()
        if left != 1:
            leftOfLeftVal.next = current
        else:
            head = current
        
        for count in range(len(arrayToMatch)-1,-1,-1):
            nextVal = arrayToMatch.pop()
            current.next = nextVal
            current = nextVal
        current.next = last
        return head
