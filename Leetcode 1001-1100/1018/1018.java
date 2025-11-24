// Leetcode 1018: Binary Prefix Divisible by 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/
// Solved on 24th of November, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number.
     * Return a list of booleans where result[i] is true if N_i is divisible by 5.
     * @param nums An array of 0s and 1s.
     * @return A list of booleans indicating if the prefix binary numbers are divisible by 5.
     */
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> result = new ArrayList<>(nums.length);
        int remainder = 0;
        for (int num : nums) {
            remainder = (remainder * 2 + num) % 5;
            result.add(remainder == 0);
        }
        return result;
    }
}