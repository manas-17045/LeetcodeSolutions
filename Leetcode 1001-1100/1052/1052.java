// Leetcode 1052: Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/
// Solved on 5th of March, 2026
class Solution {
    /**
     * Calculates the maximum number of satisfied customers given a grumpy owner.
     * 
     * @param customers An array where customers[i] is the number of customers at minute i.
     * @param grumpy An array where grumpy[i] is 1 if the owner is grumpy, 0 otherwise.
     * @param minutes The number of consecutive minutes the owner can use a technique to not be grumpy.
     * @return The maximum number of satisfied customers throughout the day.
     */
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int baseSatisfied = 0;
        int currentWindow = 0;
        int maxWindow = 0

        for (int i = 0; i < customers.length; i++) {
            if (grumpy[i] == 0) {
                baseSatisfied += customers[i];
            } else {
                currentWindow += customers[i];
            }

            if (i >= minutes) {
                if (grumpy[i - minutes] == 1) {
                    currentWindow -= customers[i - minutes];
                }
            }

            maxWindow = Math.max(maxWindow, currentWindow);
        }

        return baseSatisfied + maxWindow;
    }
}