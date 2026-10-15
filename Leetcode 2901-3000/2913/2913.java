// Leetcode 2913: Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
// Solved on 15th of October, 2026
import java.util.List;

class Solution {
    /**
     * Calculates the sum of the squares of distinct element counts across all contiguous subarrays.
     *
     * @param nums the list of integers representing the input array
     * @return the total sum of squares of distinct counts for all subarrays
     */
    public int sumCounts(List<Integer> nums) {
        int numsLength = nums.size();
        int maxValue = 0;
        int[] elements = new int[numsLength];

        for (int i = 0; i < numsLength; i++) {
            elements[i] = nums.get(i);
            if (elements[i] > maxValue) {
                maxValue = elements[i];
            }
        }

        int[] lastSeen = new int[maxValue + 1];
        int totalSum = 0;

        for (int i = 0; i < numsLength; i++) {
            int distinctCount = 0;
            int marker = i + 1;

            for (int j = i; j < numsLength; j++) {
                int currentValue = elements[j];
                if (lastSeen[currentValue] != marker) {
                    lastSeen[currentValue] = marker;
                    distinctCount++;
                }
                totalSum += distinctCount * distinctCount;
            }
        }

        return totalSum;
    }
}