// Leetcode 2841: Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/
// Solved on 1st of November, 2025
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    /**
     * Calculates the maximum sum of an "almost unique" subarray of length k.
     * An "almost unique" subarray is defined as a subarray that has at least `m` distinct elements.
     * @param nums The input list of integers.
     * @param m The minimum number of distinct elements required for a subarray to be considered "almost unique".
     * @param k The fixed length of the subarrays to consider.
     * @return The maximum sum found among all "almost unique" subarrays of length `k`.
     */
    public long maxSum(List<Integer> nums, int m, int k) {
        int n = nums.size();
        long maxSum = 0;
        long windowSum = 0;
        Map<Integer, Integer> counts = new HashMap<>();

        for (int i = 0; i < k; i++) {
            int num = nums.get(i);
            windowSum += num;
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        if (counts.size() >= m) {
            maxSum = windowSum;
        }

        for (int i = k; i < n; i++) {
            int rightNum = nums.get(i);
            int leftNum = nums.get(i - k);

            windowSum += rightNum;
            counts.put(rightNum, counts.getOrDefault(rightNum, 0) + 1);

            windowSum -= leftNum;
            int leftCount = counts.get(leftNum);
            if (leftCount == 1) {
                counts.remove(leftNum);
            } else {
                counts.put(leftNum, leftCount - 1);
            }

            if (counts.size() >= m) {
                maxSum = Math.max(maxSum, windowSum);
            }
        }

        return maxSum;
    }
}