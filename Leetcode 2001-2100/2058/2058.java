// Leetcode 2058: Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
// Solved on 31st of August, 2026
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    /**
     * Calculates the minimum and maximum distance between any two critical points in a linked list.
     *
     * @param head the head node of the singly-linked list
     * @return an integer array containing [minDistance, maxDistance], or [-1, -1] if fewer than two critical points exist
     */
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) {
            return new int[]{-1, -1};
        }

        ListNode prev = head;
        ListNode curr = head.next;
        int currentIndex = 1;
        int firstIndex = -1;
        int lastIndex = -1;
        int minDistance = Integer.MAX_VALUE;

        while (curr.next != null) {
            boolean isLocalMaxima = curr.val > prev.val && curr.val > curr.next.val;
            boolean isLocalMinima = curr.val < prev.val && curr.val < curr.next.val;

            if (isLocalMaxima || isLocalMinima) {
                if (firstIndex != -1) {
                    minDistance = Math.min(minDistance, currentIndex - lastIndex);
                } else {
                    firstIndex = currentIndex;
                }
                lastIndex = currentIndex;
            }

            prev = curr;
            curr = curr.next;
            currentIndex++;
        }

        if (firstIndex == -1 || firstIndex == lastIndex) {
            return new int[]{-1, -1};
        }

        return new int[]{minDistance, lastIndex - firstIndex};
    }
}