// Leetcode 3757: Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/
// Solved on 22nd of December, 2025
class Solution {
    /**
     * Calculates the number of effective subsequences.
     * An effective subsequence is a non-empty subsequence where the bitwise OR of its elements is equal to the bitwise OR of all elements in the original array.
     * @param nums The input array of integers.
     * @return The number of effective subsequences modulo 10^9 + 7.
     */
    public int countEffective(int[] nums){
        int n = nums.length;
        int mod = 1000000007;

        int totalOr = 0;
        for (int num : nums) {
            totalOr |= num;
        }

        if (totalOr == 0) {
            return 0;
        }

        int[] bitMapping = new int[20];
        int k = 0;
        for (int i = 0; i < 20; i++) {
            if ((totalOr & (1 << i)) != 0) {
                bitMapping[k++] = i;
            }
        }

        int compressedMax = 1 << k;
        int[] count = new int[compressedMax];

        for (int num : nums) {
            int compressedNum = 0;
            for (int i = 0; i < k; i++) {
                if ((num & (1 << bitMapping[i])) != 0) {
                    compressedNum |= (1 << i);
                }
            }
            count[compressedNum]++;
        }

        for (int i = 0; i < k; i++) {
            for (int mask = 0; mask < compressedMax; mask++) {
                if ((mask & (1 << i)) != 0) {
                    count[mask] += count[mask ^ (1 << i)];
                }
            }
        }

        int[] pow2 = new int[n + 1];
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow2[i] = (int)((pow2[i - 1] * 2L) % mod);
        }

        long countSameOr = 0;
        int maxMask = compressedMax - 1;
        int currentMask = maxMask;

        while (true) {
            int subsetCount = count[currentMask];
            long ways = pow2[subsetCount];

            int diffBits = k - Integer.bitCount(currentMask);

            if ((diffBits & 1) == 1) {
                countSameOr = (countSameOr - ways + mod) % mod;
            } else {
                countSameOr = (countSameOr + ways) % mod;
            }

            if (currentMask == 0) break;
            currentMask = (currentMask - 1) & maxMask;
        }

        return (int)((pow2[n] - countSameOr + mod) % mod);
    }
}