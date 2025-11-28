// Leetcode 2354: Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/
// Solved on 28th of November, 2025
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Counts the number of "excellent pairs" in an array.
     * An excellent pair (a, b) is defined such that a and b are from the input array,
     * and the sum of their bit counts (number of set bits) is greater than or equal to k.
     * @param nums The input array of integers.
     * @param k The minimum sum of bit counts required for an excellent pair.
     * @return The total number of excellent pairs.
     */
    public long countExcellentPairs(int[] nums, int k) {
        Set<Integer> uniqueNumbers = new HashSet<>();
        for (int num : nums) {
            uniqueNumbers.add(num);
        }

        long[] bitCounts = new long[32];
        for (int num : uniqueNumbers) {
            bitCounts[Integer.bitCount(num)]++;
        }

        long result = 0;
        for (int i = 0; i < 32; i++) {
            for (int j = 0; j < 32; j++) {
                if (i + j >= k) {
                    result += bitCounts[i] * bitCounts[j];
                }
            }
        }
        
        return result;
    }
}