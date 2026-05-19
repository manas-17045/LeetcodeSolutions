// Leetcode 3920: maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/
// Solved on 19th of May, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum number of fixed points (nums[i] == i) that can be achieved
     * by deleting elements from the original array.
     * @param nums The input array of integers.
     * @return The maximum number of fixed points possible after deletions.
     */
    public int maxFixedPoints(int[] nums) {
        int arrayLength = nums.length;
        long[] validPairs = new long[arrayLength];
        int validCount = 0;
        
        for (int i = 0; i < arrayLength; i++) {
            if (nums[i] <= i) {
                long difference = i - nums[i];
                validPairs[validCount] = (difference << 32) | nums[i];
                validCount++;
            }
        }
        
        Arrays.sort(validPairs, 0, validCount);
        
        int[] longestSubsequence = new int[validCount];
        int subsequenceLength = 0;
        
        for (int i = 0; i < validCount; i++) {
            int currentValue = (int) (validPairs[i] & 0xFFFFFFFFL);
            int leftIndex = 0;
            int rightIndex = subsequenceLength;
            
            while (leftIndex < rightIndex) {
                int midIndex = leftIndex + (rightIndex - leftIndex) / 2;
                if (longestSubsequence[midIndex] < currentValue) {
                    leftIndex = midIndex + 1;
                } else {
                    rightIndex = midIndex;
                }
            }
            
            longestSubsequence[leftIndex] = currentValue;
            if (leftIndex == subsequenceLength) {
                subsequenceLength++;
            }
        }
        
        return subsequenceLength;
    }
}