// Leetcode 2470: Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/
// Solved on 8th of November, 2025
class Solution {
    /**
     * Counts the number of subarrays in `nums` whose least common multiple (LCM) is equal to `k`.
     * @param nums The input array of integers.
     * @param k The target LCM value.
     * @return The number of subarrays with LCM equal to `k`.
     */
    public int subarrayLCM(int[] nums, int k) {
        int n = nums.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            long curr = 1;
            for (int j = i; j < n; j++) {
                int v = nums[j];
                if (k % v != 0) break;
                curr = lcm(curr, v);
                if (curr == k) count++;
                if (curr > k) break;
            }
        }
        return count;
    }

    private long lcm(long a, long b) {
        return a / gcd(a, b) * b;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}