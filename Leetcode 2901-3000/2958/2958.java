// Leetcode 2958: Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
// Solved on 12th of August, 2026
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Finds the length of the longest subarray where the frequency of each element is at most k.
     * @param nums The input array of integers.
     * @param k The maximum frequency allowed for each element.
     * @return The length of the longest subarray satisfying the condition.
     */
    public int maxSubarrayLength(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < nums.length; right++) {
            int currentNum = nums[right];
            frequencyMap.put(currentNum, frequencyMap.getOrDefault(currentNum, 0) + 1);

            while (frequencyMap.get(currentNum) > k) {
                int leftNum = nums[left];
                frequencyMap.put(leftNum, frequencyMap.get(leftNum) - 1);
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}