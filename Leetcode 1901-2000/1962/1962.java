// Leetcode 1962: Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/
// Solved on 30th of November, 2025
import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    /**
     * Minimizes the total number of stones by performing a specific operation `k` times.
     * In each operation, a pile is chosen, and `floor(stones_in_pile / 2)` stones are removed from it.
     * @param piles An array of integers representing the number of stones in each pile.
     * @param k The number of operations to perform.
     * @return The minimum total number of stones after `k` operations.
     */
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(piles.length, Collections.reverseOrder());
        int sum = 0;
        for (int pile : piles) {
            queue.add(pile);
            sum += pile;
        }

        while (k > 0) {
            int curr = queue.poll();
            int remove = curr / 2;
            if (remove == 0) {
                break;
            }
            sum -= remove;
            queue.add(curr - remove);
            k--;
        }

        return sum;
    }
}