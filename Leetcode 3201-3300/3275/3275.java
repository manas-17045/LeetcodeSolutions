// Leetcode 3275: K-th Nearst Obstacle qUERIES
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/
// Solved on 8th of December, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Finds the k-th nearest obstacle for a series of queries.
     * @param queries A 2D array where each inner array represents a query [x, y] for an obstacle's coordinates.
     * @param k The k-th nearest obstacle to find.
     * @return An array of integers where each element is the Manhattan distance to the k-th nearest obstacle for the corresponding query, or -1 if fewer than k obstacles are encountered so far.
     */
    public int[] resultsArray(int[][] queries, int k) {
        int[] results = new int[queries.length];
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < queries.length; i++) {
            int distance = Math.abs(queries[i][0]) + Math.abs(queries[i][1]);

            if (maxHeap.size() < k) {
                maxHeap.offer(distance);
            } else if (distance < maxHeap.peek()) {
                maxHeap.poll();
                maxHeap.offer(distance);
            }

            if (maxHeap.size() < k) {
                results[i] = -1;
            } else {
                results[i] = maxHeap.peek();
            }
        }
        return results;
    }
}