// Leetcode 3985: Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/
// Solved on 2nd of August, 2026
class Solution {
    /**
     * Calculates the maximum sum of a palindromic subarray using Manacher's algorithm.
     * 
     * @param nums The input array.
     * @return The maximum palindromic subarray sum.
     */
    public long getSum(int[] nums) {
        int arrayLength = nums.length;
        int modifiedLength = 2 * arrayLength + 1;
        int[] modified = new int[modifiedLength];
        
        for (int i = 0; i < arrayLength; i++) {
            modified[2 * i] = -1;
            modified[2 * i + 1] = nums[i];
        }
        modified[modifiedLength - 1] = -1;
        
        int[] palindromeRadii = new int[modifiedLength];
        int center = 0;
        int rightEdge = 0;
        
        for (int i = 0; i < modifiedLength; i++) {
            int mirrorCenter = 2 * center - i;
            if (i < rightEdge) {
                palindromeRadii[i] = Math.min(rightEdge - i, palindromeRadii[mirrorCenter]);
            }
            
            int rightBound = i + 1 + palindromeRadii[i];
            int leftBound = i - 1 - palindromeRadii[i];
            
            while (rightBound < modifiedLength && leftBound >= 0 && modified[rightBound] == modified[leftBound]) {
                palindromeRadii[i]++;
                rightBound++;
                leftBound--;
            }
            
            if (i + palindromeRadii[i] > rightEdge) {
                center = i;
                rightEdge = i + palindromeRadii[i];
            }
        }
        
        long[] prefixSums = new long[arrayLength + 1];
        for (int i = 0; i < arrayLength; i++) {
            prefixSums[i + 1] = prefixSums[i] + nums[i];
        }
        
        long maximumSum = 0;
        for (int i = 0; i < modifiedLength; i++) {
            int startIndex = (i - palindromeRadii[i]) / 2;
            int endIndex = (i + palindromeRadii[i]) / 2 - 1;
            
            if (startIndex <= endIndex) {
                long currentPalindromeSum = prefixSums[endIndex + 1] - prefixSums[startIndex];
                if (currentPalindromeSum > maximumSum) {
                    maximumSum = currentPalindromeSum;
                }
            }
        }
        
        return maximumSum;
    }
}