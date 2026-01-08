// Leetcode 3789: Minimum Cost to Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
// Solved on 8th of January, 2026
class Solution {
    /**
     * Calculates the minimum cost to acquire required items.
     * @param cost1 The cost of acquiring one item of type 1.
     * @param cost2 The cost of acquiring one item of type 2.
     * @param costBoth The cost of acquiring one item of type 1 and one item of type 2 together.
     * @param need1 The number of items of type 1 needed.
     * @param need2 The number of items of type 2 needed.
     * @return The minimum total cost.
     */
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long separateCost = (long) need1 * cost1 + (long) need2 * cost2;
        long combinedCost = (long) Math.max(need1, need2) * costBoth;

        int minNeed = Math.min(need1, need2);
        long mixedCost = (long) minNeed * costBoth + (long) (need1 - minNeed) * cost1 + (long) (need2 - minNeed) * cost2;

        return Math.min(separateCost, Math.min(combinedCost, mixedCost));
    }
}