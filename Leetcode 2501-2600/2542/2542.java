// Leetcode 2542: Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/
// Solved on 19th of November, 2025
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the maximum possible score by selecting a subsequence of length k.
     * The score is defined as the sum of the selected nums1 elements multiplied by the minimum of the selected nums2 elements.
     * @param nums1 An array of integers.
     * @param nums2 An array of integers.
     * @param k The length of the subsequence to select.
     * @return The maximum possible score.
     */
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = nums1[i];
            pairs[i][1] = nums2[i];
        }

        Arrays.sort(pairs, (a, b) -> b[1] - a[1]);

        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);
        long sum = 0;
        long maxScore = 0;

        for (int[] pair : pairs) {
            minHeap.add(pair[0]);
            sum += pair[0];

            if (minHeap.size() > k) {
                sum -= minHeap.poll();
            }

            if (minHeap.size() == k) {
                maxScore = Math.max(maxScore, sum * pair[1]);
            }
        }

        return maxScore;
    }
}