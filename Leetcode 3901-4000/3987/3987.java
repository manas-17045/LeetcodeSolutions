// Leetcode 3987: Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/
// Solved on 7th of August, 2026
class Solution {
    /**
     * Calculates the minimum total cost to process all elements in an array.
     * The cost is determined by the sum of the number of operations required for each element.
     * 
     * @param nums The array of integers to process.
     * @param k The cost of a single operation.
     * @return The minimum total cost to process all elements.
     */
    public int minimumCost(int[] nums, int k) {
        long totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        if (totalSum <= k) {
            return 0;
        }
        long totalOps = (totalSum - 1) / k;
        long mod = 1000000007L;
        long opsMod = totalOps % mod;
        long result = (opsMod * ((opsMod + 1) % mod)) % mod;
        result = (result * 500000004L) % mod;
        return (int) result;
    }
}