// Leetcode 3782: Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/
// Solved on 24th of December, 2025
class Solution {
    /**
     * Calculates the last remaining integer after alternating deletion operations.
     * @param n The initial number of integers in the list (from 1 to n).
     * @return The last remaining integer.
     */
    public long lastInteger(long n) {
        long head = 1;
        long step = 1;
        long count = n;
        boolean isLeft = true;

        while (count > 1) {
            if (!isLeft && count % 2 == 0) {
                head += step;
            }
            step *= 2;
            count -= count / 2;
            isLeft = !isLeft;
        }
        return head;
    }
}