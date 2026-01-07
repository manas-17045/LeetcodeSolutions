// Leetcode 2816: Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
// Solved on 7th of January, 2027
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    /**
     * Doubles the number represented by a linked list.
     * @param head The head of the linked list representing the number.
     * @return The head of the linked list representing the doubled number.
     */
    public ListNode doubleIt(ListNode head) {
        if (head.val > 4) {
            ListNode newHead = new ListNode(0);
            newHead.next = head;
            head = newHead;
        }
        
        ListNode current = head;
        while (current != null) {
            current.val = (current.val * 2) % 10;
            if (current.next != null && current.next.val > 4) {
                current.val++;
            }
            current = current.next;
        }
        
        return head;
    }
}