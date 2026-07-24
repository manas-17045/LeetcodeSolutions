// Leetcode 3514: Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique0xor-triplets-ii/
// Solved on 24th of July, 2026
class Solution {
    /**
     * Counts the number of unique XOR triplets.
     * @param nums Array of integers.
     * @return Number of unique XOR triplets.
     */
    public int uniqueXorTriplets(int[] nums) {
        int n = nums.length;
        boolean[] haspair = new boolean[2048];
        boolean[] seenTriplet = new boolean[2048];
        int[] pairList = new int[2048];
        int pairCount = 0;

        for (int i = n - 1; i >= 0; i--) {
            for (int k = i; k < n; k++) {
                int pairXor = nums[i] ^ nums[k];
                if (!hasPair[pairXor]) {
                    hasPair[pairXor] = true;
                    pairList[pairCount++] = pairXor;
                }
            }
            for (int j = 0; j < pairCount; j++) {
                seenTriplet[nums[i] ^ pairList[j]] = true;
            }
        }

        int count = 0;
        for (boolean seen : seenTriplet) {
            if (seen) {
                count++;
            }
        }

        return count;
    }
}