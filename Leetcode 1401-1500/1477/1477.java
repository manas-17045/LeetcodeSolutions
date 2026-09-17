// Leetcode 1477: Find Two Non-overlapping Sub-arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
// Solved on 17th of September, 2026
class Solution {
    /**
     * Finds the minimum sum of lengths of two non-overlapping sub-arrays
     * that each have a sum equal to the specified target.
     *
     * @param arr the array of positive integers
     * @param target the target sum for each sub-array
     * @return the minimum total length of the two sub-arrays, or -1 if two such sub-arrays do not exist
     */
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int[] minLens = new int[n];
        int left = 0;
        int currentSum = 0;
        int minTotalLength = Integer.MAX_VALUE;

        for (int right = 0; right < n; right++) {
            currentSum += arr[right];

            while (currentSum > target) {
                currentSum -= arr[left];
                left++;
            }

            int bestPrevious = (right > 0) ? minLens[right - 1] : Integer.MAX_VALUE;

            if (currentSum == target) {
                int currentLen = right - left + 1;
                if (left > 0 && minLens[left - 1] != Integer.MAX_VALUE) {
                    minTotalLength = Math.min(minTotalLength, currentLen + minLens[left - 1]);
                }
                minLens[right] = Math.min(bestPrevious, currentLen);
            } else {
                minLens[right] = bestPrevious;
            }
        }

        return minTotalLength == Integer.MAX_VALUE ? -1 : minTotalLength;
    }
}