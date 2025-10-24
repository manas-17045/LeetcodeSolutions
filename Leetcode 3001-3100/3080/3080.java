// Leetcode 3080: Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/
// Solved on 24th of October, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the sum of unmarked elements after performing a series of queries.
     * Each query involves marking a specific element and then marking the `k` smallest unmarked elements.
     *
     * @param nums An array of integers representing the initial elements.
     * @param queries A 2D array where each inner array `[index, k]` represents a query.
     * @return An array of long integers, where each element is the sum of unmarked elements after the corresponding query.
     */
    public long[] unmarkedSumArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int m = queries.length;

        boolean[] marked = new boolean[n];
        long[] answer = new long[m];
        long sum = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });

        for (int i = 0; i < n; i++) {
            sum += nums[i];
            pq.add(new int[]{nums[i], i});
        }

        for (int i = 0; i < m; i++) {
            int index = queries[i][0];
            int k = queries[i][1];

            if (!marked[index]) {
                marked[index] = true;
                sum -= nums[index];
            }

            int count = 0;
            while (count < k && !pq.isEmpty()) {
                int[] smallest = pq.poll();
                int val = smallest[0];
                int idx = smallest[1];

                if (!marked[idx]) {
                    marked[idx] = true;
                    sum -= val;
                    count++;
                }
            }
            answer[i] = sum;
        }

        return answer;
    }
}