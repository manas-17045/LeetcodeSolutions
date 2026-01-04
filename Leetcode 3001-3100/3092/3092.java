// Leetcode 3092: Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/
// Solved on 4th of January, 2026
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the most frequent ID after each operation.
     * @param nums An array of IDs.
     * @param freq An array of frequencies, where `freq[i]` is added to `nums[i]`'s count.
     * @return An array `ans` where `ans[i]` is the count of the most frequent ID after the i-th operation.
     */
    public long[] mostFrequentIDs(int[] nums, int[] freq) {
        int n = nums.length;
        long[] ans = new long[n];
        long[] counts = new long[100001];
        PriorityQueue<long[]> priorityQueue = new PriorityQueue<>((a, b) -> Long.compare(b[0], a[0]));

        for (int i = 0; i < n; i++) {
            int id = nums[i];
            counts[id] += freq[i];
            priorityQueue.offer(new long[]{counts[id], id});

            while (priorityQueue.peek()[0] != counts[(int) priorityQueue.peek()[1]]) {
                priorityQueue.poll();
            }

            ans[i] = priorityQueue.peek()[0];
        }

        return ans;
    }
}