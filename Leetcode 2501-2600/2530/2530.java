// Leetcode 2530: Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/
// Solved on 30th of November, 2025
import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    /**
     * Calculates the maximum score achievable by applying operations on an array of numbers.
     * In each operation, the largest number is chosen, its value is added to the score,
     * and then it's replaced by ceil(value / 3). This is repeated `k` times.
     * @param nums An array of integers.
     * @param k The number of operations to perform.
     * @return The maximum score achievable.
     */
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : nums) {
            pq.add(num);
        }

        long score = 0;
        while (k > 0) {
            int val = pq.poll();
            score += val;
            pq.add((val + 2) / 3);
            k--;
        }

        return score;
    }
}