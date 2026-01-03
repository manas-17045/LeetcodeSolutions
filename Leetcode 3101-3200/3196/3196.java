// Leetcode 3196: Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/
// Solved on 3rd of January, 2026
class Solution {
    /**
     * Calculates the maximum total cost of alternating subarrays.
     * The cost is maximized by strategically choosing to add or subtract elements.
     * @param nums An array of integers.
     * @return The maximum total cost.
     */
    public long maximumTotalCost(int[] nums) {
        long addCost = nums[0];
        long subCost = Long.MIN_VALUE;

        for (int i = 1; i < nums.length; i++) {
            long nextAddCost = Math.max(addCost, subCost) + nums[i];
            long nextSubCost = addCost - nums[i];

            addCost = nextAddCost;
            subCost = nextSubCost;
        }

        return Math.max(addCost, subCost);
    }
}