// Leetcode 3984: Divisible Game
// https://leetcode.com/problems/divisible-game/
// Solved on 2nd of August, 2026
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Finds the value of k that maximizes the expression (maxScoreDiff * k) % 1000000007,
     * where maxScoreDiff is the maximum subarray sum of the array obtained by
     * replacing each element in nums with either the element itself if it is
     * divisible by k or the negative of the element if it is not divisible by k.
     *
     * @param nums The input array of integers.
     * @return The value of k that maximizes the expression (maxScoreDiff * k) % 1000000007.
     */
    public int divisibleGame(int[] nums) {
        Set<Integer> candidates = new HashSet<>();
        candidates.add(2);
        for (int num : nums) {
            int temp = num;
            for (int d = 2; d * d <= temp; d++) {
                if (temp % d == 0) {
                    candidates.add(d);
                    while (temp % d == 0) {
                        temp /= d;
                    }
                }
            }
            if (temp > 1) {
                candidates.add(temp);
            }
        }
        long maxDiff = Long.MIN_VALUE;
        int bestK = Integer.MAX_VALUE;
        for (int k : candidates) {
            long currentSum = 0;
            long maxSubarray = Long.MIN_VALUE;
            for (int num : nums) {
                long val = (num % k == 0) ? num : -num;
                currentSum += val;
                if (currentSum > maxSubarray) {
                    maxSubarray = currentSum;
                }
                if (currentSum < 0) {
                    currentSum = 0;
                }
            }
            if (maxSubarray > maxDiff) {
                maxDiff = maxSubarray;
                bestK = k;
            } else if (maxSubarray == maxDiff && k < bestK) {
                bestK = k;
            }
        }
        long mod = 1000000007L;
        long product = (maxDiff % mod) * (bestK % mod) % mod;
        long result = (product + mod) % mod;
        return (int) result;
    }
}