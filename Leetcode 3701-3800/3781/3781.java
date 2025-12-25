// Leetcode 3781: Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/
// Solved on 25th of December, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the maximum score after performing binary swaps.
     * @param nums An array of integers representing the values.
     * @param s A string representing the binary configuration.
     * @return A long representing the maximum possible score.
     */
    public long maximumScore(int[] nums, String s) {
        long score = 0;
        int capacity = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = nums.length - 1; i >= 0; i--) {
            pq.offer(nums[i]);
            score += nums[i];

            if (s.charAt(i) == '1') {
                capacity++;
            }

            if (pq.size() > capacity) {
                score -= pq.poll();
            }
        }

        return score;
    }
}