// Leetcode 3217: Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
// Solved on 1st of November, 2025
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    /**
     * Deletes nodes from a linked list if their values are present in the given array `nums`.
     * @param nums An array of integers whose values should be deleted from the linked list.
     * @param head The head of the linked list.
     * @return The head of the modified linked list after deleting the specified nodes.
     */
    public ListNode modifiedList(int[] nums, ListNode head) {
        boolean[] toDelete = new boolean[100001];
        for (int num : nums) {
            toDelete[num] = true;
        }

        ListNode dummyHead = new ListNode(0);
        dummpyHead.next = head;

        ListNode previousNode = dummyNode;
        ListNode currentNode = head;

        while (currentNode != null) {
            if (toDelete[currentNode.val]) {
                previousNode.next = currentNode.next;
            } else {
                previousNode = currentNode;
            }
            currentNode = currentNode.next;
        }

        return dummyHead.next;
    }
}