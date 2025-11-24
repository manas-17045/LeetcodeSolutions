// Leetcode 3224: Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/
// Solved on 24th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of changes required to make the differences between symmetric pairs equal.
     *
     * @param nums The input array of integers.
     * @param k The maximum possible value for an element in the array.
     * @return The minimum number of changes.
     */
    public int minChanges(int[] nums, int k) {
        int n = nums.length;
        int[] differenceArray = new int[k + 2];
        int halfN = n / 2;

        for (int i = 0; i < halfN; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            
            int diff = Math.abs(a - b);
            
            int maxDiff = Math.max(a, k - a);
            maxDiff = Math.max(maxDiff, Math.max(b, k - b));

            differenceArray[diff] -= 1;
            differenceArray[diff + 1] += 1;
            differenceArray[maxDiff + 1] += 1;
        }

        int minOperations = halfN;
        int currentOperations = halfN;

        for (int x = 0; x <= k; x++) {
            currentOperations += differenceArray[x];
            if (currentOperations < minOperations) {
                minOperations = currentOperations;
            }
        }

        return minOperations;
    }
}