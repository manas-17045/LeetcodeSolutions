// Leetcode 2054: Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/
// Solved on 2nd of November, 2025
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the maximum sum of values from at most two non-overlapping events.
     *
     * @param events A 2D array where each inner array represents an event [start_time, end_time, value].
     * @return The maximum total value achievable from selecting at most two non-overlapping events.
     */
    public int maxTwoEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> Integer.compare(a[0], b[0]));

        int maxTotalSum = 0;
        int maxPrecedingValue = 0;
        
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

        for (int[] event : events) {
            int start = event[0];
            int end = event[1];
            int value = event[2];

            while (!minHeap.isEmpty() && minHeap.peek()[0] < start) {
                int[] finishedEvent = minHeap.poll();
                int finishedValue = finishedEvent[1];
                maxPrecedingValue = Math.max(maxPrecedingValue, finishedValue);
            }

            maxTotalSum = Math.max(maxTotalSum, maxPrecedingValue + value);

            minHeap.offer(new int[]{end, value});
        }

        return maxTotalSum;
    }
}