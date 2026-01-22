// Leetcode 3811: Number of Alternating XOR Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/
// Solved on 22nd of January, 2026
class Solution {
    /**
     * Calculates the number of ways to partition the array into subarrays such that
     * the XOR sum of the subarrays alternates between target1 and target2, starting
     * with target1.
     * @param nums An array of integers.
     * @param target1 The XOR sum required for the 1st, 3rd, etc., subarrays.
     * @param target2 The XOR sum required for the 2nd, 4th, etc., subarrays.
     * @return The number of valid partitions modulo 10^9 + 7.
     */
    public int alternatingXOR(int[] nums, int target1, int target2) {
        int mod = 1000000007;
        int[] countTarget1 = new int[200000];
        int[] countTarget2 = new int[200000];
        
        countTarget2[0] = 1;
        
        int prefixXor = 0;
        int result = 0;
        
        for (int num : nums) {
            prefixXor ^= num;
            
            int waysEndingTarget1 = countTarget2[prefixXor ^ target1];
            int waysEndingTarget2 = countTarget1[prefixXor ^ target2];
            
            countTarget1[prefixXor] = (countTarget1[prefixXor] + waysEndingTarget1) % mod;
            countTarget2[prefixXor] = (countTarget2[prefixXor] + waysEndingTarget2) % mod;
            
            result = (waysEndingTarget1 + waysEndingTarget2) % mod;
        }
        
        return result;
    }
}