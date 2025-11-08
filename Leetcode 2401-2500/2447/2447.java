// Leetcode 2447: Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/
// Solved on 8th of November, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Counts the number of subarrays in `nums` whose greatest common divisor (GCD) is equal to `k`.
     * @param nums The input array of integers.
     * @param k The target GCD value.
     * @return The number of subarrays with GCD equal to `k`.
     */
    public int subarrayGCD(int[] nums, int k) {
        int result = 0;
        Map<Integer, Integer> prev = new HashMap<>();
        for (int num : nums) {
            Map<Integer, Integer> cur = new HashMap<>();
            cur.put(num, cur.getOrDefault(num, 0) + 1);
            for (Map.Entry<Integer, Integer> e : prev.entrySet()) {
                int newG = gcd(e.getKey(), num);
                if (newG < k) {
                    continue;
                }
                cur.put(newG, cur.getOrDefault(newG, 0) + e.getValue());
            }
            result += cur.getOrDefault(k, 0);
            prev = cur;
        }
        return result;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    }
}