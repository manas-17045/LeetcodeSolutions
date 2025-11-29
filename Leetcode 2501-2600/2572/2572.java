// Leetcode 2572: Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/
// Solved on 29th of November, 2025
class Solution {
    /**
     * Counts the number of square-free subsets that can be formed from the given array of integers.
     * A subset is square-free if the product of its elements is square-free.
     * @param nums The input array of integers.
     * @return The number of square-free subsets modulo 10^9 + 7.
     */
    public int squareFreeSubsets(int[] nums) {
        int mod = 1000000007;
        int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        int[] count = new int[31];
        for (int num : nums) {
            count[num]++;
        }

        long[] dp = new long[1024];
        dp[0] = 1;

        for (int i = 2; i <= 30; i++) {
            if (count[i] == 0) {
                continue;
            }

            int mask = 0;
            boolean isSquareFree = true;
            for (int j = 0; j < 10; j++) {
                if (i % primes[j] == 0) {
                    if (i % (primes[j] * primes[j]) == 0) {
                        isSquareFree = false;
                        break;
                    }
                    mask |= (1 << j);
                }
            }

            if (!isSquareFree) {
                continue;
            }

            for (int state = 1023; state >= 0; state--) {
                if ((state & mask) == 0) {
                    dp[state | mask] = (dp[state | mask] + dp[state] * count[i]) % mod;
                }
            }
        }

        long result = 0;
        for (long val : dp) {
            result = (result + val) % mod;
        }

        long powerOfTwo = 1;
        for (int i = 0; i < count[1]; i++) {
            powerOfTwo = (powerOfTwo * 2) % mod;
        }

        result = (result * powerOfTwo) % mod;
        return (int) ((result - 1 + mod) % mod);
    }
}