// Leetcode 2130: Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
// Solved on 14th of June, 2026
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    /**
     * Calculates the maximum twin sum of a linked list of even length.
     * @param head The head of the linked list.
     * @return The maximum sum of a node and its twin.
     */
    public int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null;
        ListNode curr = slow;
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }
        ListNode firstHalf = head;
        ListNode secondHalf = prev;
        int maxVal = 0;
        while (secondHalf != null) {
            maxVal = Math.max(maxVal, firstHalf.val + secondHalf.val);
            firstHalf = firstHalf.next;
            secondHalf = secondHalf.next;
        }
        return maxVal;
    }
}