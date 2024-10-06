# Problem Name: 21. Merge Two Sorted Lists
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            combinedList = ListNode(val='')
        elif list1 is None:
            combinedList = ListNode(val=list2.val)
            list2 = list2.next
        elif list2 is None:
            combinedList = ListNode(val=list1.val)
            list1 = list1.next
        elif list1.val < list2.val:
            combinedList = ListNode(val=list1.val)
            list1 = list1.next
        else:
            combinedList = ListNode(val=list2.val)
            list2 = list2.next
        head = combinedList
        while list1 is not None or list2 is not None:
            if list1 is None:
                currentList = ListNode(val=list2.val)
                list2 = list2.next
            elif list2 is None:
                currentList = ListNode(val=list1.val)
                list1 = list1.next
            elif list1.val < list2.val:
                currentList = ListNode(val=list1.val)
                list1 = list1.next
            else:
                currentList = ListNode(val=list2.val)
                list2 = list2.next
            head.next = currentList
            head = head.next
        return combinedList
