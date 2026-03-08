// Leetcode 3861: Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/
// Solved on 8th of March, 2026
class Solution {
    /**
     * Finds the index of the box with the minimum capacity that can fit the item.
     * @param capacity An array representing the capacities of available boxes.
     * @param itemSize The size of the item to be placed in a box.
     * @return The index of the box with the smallest capacity >= itemSize, or -1 if none fit.
     */
    public int minimumIndex(int[] capacity, int itemSize) {
        int bestIndex = -1;
        int minCapacity = Integer.MAX_VALUE;
        for (int i = 0; i < capacity.length; i++) {
            if (capacity[i] >= itemSize && capacity[i] < minCapacity) {
                minCapacity = capacity[i];
                bestIndex = i;
            }
        }
        return bestIndex;
    }
}