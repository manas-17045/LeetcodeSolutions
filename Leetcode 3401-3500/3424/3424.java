// Leetcode 3424: Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/
// Solved on 4th of December, 2025
class Solution {
    /**
     * Calculates the minimum cost to make two arrays identical.
     * @param arr The first array.
     * @param brr The second array.
     * @param k The cost of an operation.
     * @return The minimum cost to make the arrays identical.
     */
    public long minCost(int[] arr, int[] brr, long k) {
        long originalCost = 0;
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            originalCost += Math.abs(arr[i] - brr[i]);
        }

        if (originalCost <= k) {
            return originalCost;
        }

        Arrays.sort(arr);
        Arrays.sort(brr);

        long sortedCost = 0;
        for (int i = 0; i < n; i++) {
            sortedCost += Math.abs(arr[i] - brr[i]);
        }

        return Math.min(originalCost, sortedCost + k);
    }
}