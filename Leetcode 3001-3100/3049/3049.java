// Leetcode 3049: Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/
// Solved on 19th of November, 2025
import java.util.*;

class Solution {
    /**
     * Finds the earliest second at which all indices can be marked.
     *
     * @param nums An array of integers representing the values at each index.
     * @param changeIndices An array of integers representing the index that becomes available at each second.
     * @return The earliest second to mark all indices, or -1 if it's not possible.
     */
    public int earliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        int n = nums.length;
        int m = changeIndices.length;
        if (n > m) {
            return -1;
        }

        int[] firstOccurrence = new int[n + 1];
        for (int i = 0; i < m; i++) {
            int index = changeIndices[i];
            if (firstOccurrence[index] == 0) {
                firstOccurrence[index] = i + 1;
            }
        }

        long totalNums = 0;
        for (int num : nums) {
            totalNums += num;
        }

        int low = n;
        int high = m;
        int ans = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canMarkIndices(nums, changeIndices, firstOccurrence, mid, totalNums)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private boolean canMarkIndices(int[] nums, int[] changeIndices, int[] firstOccurrence, int limit, long totalNums) {
        PriorityQueue<Integer> savingsQueue = new PriorityQueue<>();
        int freeSlots = 0;
        long savedOperations = 0;

        for (int s = limit; s >= 1; s--) {
            int index = changeIndices[s - 1];
            if (firstOccurrence[index] == s) {
                int val = nums[index - 1];
                if (val > 1) {
                    if (freeSlots > 0) {
                        freeSlots--;
                        savingsQueue.offer(val);
                        savedOperations += (val - 1);
                    } else {
                        freeSlots++;
                        if (!savingsQueue.isEmpty() && val > savingsQueue.peek()) {
                            int minVal = savingsQueue.poll();
                            savedOperations -= (minVal - 1);
                            savingsQueue.offer(val);
                            savedOperations += (val - 1);
                        }
                    }
                } else {
                    freeSlots++;
                }
            } else {
                freeSlots++;
            }
        }

        long neededOperations = nums.length + totalNums - savedOperations;
        return neededOperations <= limit;
    }
}