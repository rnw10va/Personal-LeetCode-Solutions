# Problem Name: 141. Linked List Cycle
# Problem Link: https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        headSlow = head
        while head is not None and head.next is not None:
            if headSlow == head.next:
                return True
            if i % 2 == 1:
                headSlow = headSlow.next
            head = head.next
            i += 1
        return False
