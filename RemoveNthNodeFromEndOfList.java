// Problem Name: 19. Remove Nth Node From End of List
// Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode currentNode=head;
        ListNode nAwayNode=head;
        for(int i=0;i<n;i++){
            nAwayNode=nAwayNode.next;
        }
        if(nAwayNode==null) return head.next;
        while(nAwayNode.next!=null){
            currentNode=currentNode.next;
            nAwayNode=nAwayNode.next;
        }
        currentNode.next=currentNode.next.next;
        return head;
    }
}
