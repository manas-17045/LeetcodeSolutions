// Leetcode 61: Rotate List
// https://leetcode.com/problems/rotate-list/
// Solved on 5th of May, 2026
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    /**
     * Rotates the list to the right by k places.
     * 
     * @param head The head of the linked list.
     * @param k    The number of positions to rotate the list to the right.
     * @return     The head of the rotated linked list.
     */
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }
        
        int length = 1;
        ListNode tail = head;
        
        while (tail.next != null) {
            length++;
            tail = tail.next;
        }
        
        k = k % length;
        if (k == 0) {
            return head;
        }
        
        ListNode newTail = head;
        for (int i = 0; i < length - k - 1; i++) {
            newTail = newTail.next;
        }
        
        ListNode newHead = newTail.next;
        newTail.next = null;
        tail.next = head;
        
        return newHead;
    }
}