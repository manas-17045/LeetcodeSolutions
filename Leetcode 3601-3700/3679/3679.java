// Leetcode 3679: Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/
// Solved on 28th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of items to discard to balance the inventory.
     * @param arrivals An array representing the arrival of items, where arrivals[i] is the type of the i-th item.
     * @param w The window size, representing the number of most recent items to consider.
     * @param m The maximum allowed count for any single item type within the window.
     * @return The minimum number of items that must be discarded.
     */
    public int minArrivalsToDiscard(int[] arrivals, int w, int m) {
        int n = arrivals.length;
        int discards = 0;
        int[] counts = new int[100001];
        boolean[] kept = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (i >= w) {
                int removeIndex = i - w;
                if (kept[removeIndex]) {
                    counts[arrivals[removeIndex]]--;
                }
            }

            int val = arrivals[i];
            if (counts[val] < m) {
                counts[val]++;
                kept[i] = true;
            } else {
                discards++;
            }
        }
        
        return discards;
    }
}