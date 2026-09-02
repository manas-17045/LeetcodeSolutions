// Leetcode 4010: Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/
// Solved on 2nd of September, 2026
import java.util.Arrays;

class Solution {
    /**
     * Computes the maximum pair strength over all possible distinct index pairs in the array.
     *
     * @param nums the input array of positive integers
     * @return the maximum strength among all distinct index pairs
     */
    public long maxPairStrength(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        long maxStrength = 0;

        for (int i = n - 1; i >= 1; i--) {
            if ((long) nums[i] * nums[i] <= maxStrength) {
                break;
            }
            for (int j = i - 1; j >= 0; j--) {
                if ((long) nums[i] * nums[j] <= maxStrength) {
                    break;
                }
                int commonDivisor = gcd(nums[i], nums[j]);
                long strength = ((long) nums[i] / commonDivisor) * (nums[j] / commonDivisor);
                if (strength > maxStrength) {
                    maxStrength = strength;
                }
            }
        }

        return maxStrength;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }
}