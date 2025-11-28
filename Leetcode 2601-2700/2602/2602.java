// Leetcode 2602: Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/
// Solved on 28th of November, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Calculates the minimum number of operations to make all array elements equal to a given query value.
     * @param nums The input array of integers.
     * @param queries The array of query values.
     * @return A list of long integers, where each element is the minimum operations for the corresponding query.
     */
    public List<Long> minOperations(int[] nums, int[] queries) {
        Arrays.sort(nums);
        int n = nums.length;
        long[] prefixSum = new long[n + 1];

        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        List<Long> result = new ArrayList<>();

        for (int query : queries) {
            int left = 0;
            int right = n;

            while (left < right) {
                int mid = left + (right - left) / 2;
                if (nums[mid] < query) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            int index = left;
            long leftSum = prefixSum[index];
            long rightSum = prefixSum[n] - leftSum;
            long leftCount = index;
            long rightCount = n - index;

            long operations = (leftCount * query - leftSum) + (rightSum - rightCount * query);
            result.add(operations);
        }

        return result;
    }
}