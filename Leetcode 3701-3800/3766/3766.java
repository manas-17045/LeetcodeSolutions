// Leetcode 3766: Minimum Operations to make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/
// Solved on 26th of December, 2025
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    /**
     * Calculates the minimum operations to make each number in the input array a binary palindrome.
     *
     * @param nums The input array of integers.
     * @return An array where each element `result[i]` is the minimum difference between `nums[i]` and the nearest binary palindrome.
     */
    public int[] minOperations(int[] nums) {
        List<Integer> binaryPalindromes = new ArrayList<>();
        for (int length = 1; length <= 14; length++) {
            int halfLength = (length + 1) / 2;
            int start = 1 << (halfLength - 1);
            int end = (1 << halfLength) - 1;
            for (int i = start; i <= end; i++) {
                int palindrome = i;
                int temp = i;
                if (length % 2 != 0) {
                    temp >>= 1;
                }
                while (temp > 0) {
                    palindrome = (palindrome << 1) | (temp & 1);
                    temp >>= 1;
                }
                binaryPalindromes.add(palindrome);
            }
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int target = nums[i];
            int index = Collections.binarySearch(binaryPalindromes, target);
            if (index >= 0) {
                result[i] = 0;
            } else {
                int insertionPoint = -index - 1;
                int minDiff = Integer.MAX_VALUE;
                if (insertionPoint < binaryPalindromes.size()) {
                    minDiff = Math.min(minDiff, binaryPalindromes.get(insertionPoint) - target);
                }
                if (insertionPoint > 0) {
                    minDiff = Math.min(minDiff, target - binaryPalindromes.get(insertionPoint - 1));
                }
                result[i] = minDiff;
            }
        }
        return result;
    }
}