// Leetcode 1356: Sort Integers by The Number of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
// Solved on 25th of February, 2026
import java.util.Arrays;

class Solution {
    /**
     * Sorts an array of integers in ascending order based on the number of 1 bits 
     * in their binary representation. If two integers have the same number of 1 bits, 
     * they are sorted in ascending order of their actual values.
     * 
     * @param arr The input array of integers to be sorted.
     * @return The sorted array of integers.
     */
    public int[] sortByBits(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] |= Integer.bitCount(arr[i]) << 16;
        }

        Arrays.sort(arr);

        for (int i = 0; i < arr.length; i++) {
            arr[i] &= 0xFFFF;
        }
        return arr;
    }
}