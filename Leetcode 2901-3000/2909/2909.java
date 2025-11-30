// Leetcode 2909: Minimum Sum of mountain Troplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/
// Solved on 30th of November, 2025
class Solution {
    /**
     * Finds the minimum sum of a "mountain triplet" in the given array.
     * A triplet (i, j, k) is a mountain triplet if i < j < k and nums[i] < nums[j] and nums[k] < nums[j].
     *
     * @param nums The input array of integers.
     * @return The minimum sum of a mountain triplet, or -1 if no such triplet exists.
     */
    public int minimumSum(int[] nums) {
        int n = nums.length;
        int[] rightMin = new int[n];
        rightMin[n - 1] = nums[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            rightMin[i] = Math.min(nums[i], rightMin[i + 1]);
        }

        int minSum = Integer.MAX_VALUE;
        int leftMin = nums[0];

        for (int i = 1; i < n - 1; i++) {
            if (leftMin < nums[i] && rightMin[i + 1] < nums[i]) {
                minSum = Math.min(minSum, leftMin + nums[i] + rightMin[i + 1]);
            }
            leftMin = Math.min(leftMin, nums[i]);
        }

        return minSum == Integer.MAX_VALUE ? -1 : minSum;
    }
}