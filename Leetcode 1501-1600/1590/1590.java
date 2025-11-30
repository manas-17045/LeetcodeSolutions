// Leetcode 1590: Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/
// Solved on 30th of November, 2025
import java.util.HashMap;

class Solution {
    /**
     * Finds the minimum length of a subarray that needs to be removed such that the sum of the remaining elements
     * is divisible by p.
     * @param nums The input array of integers.
     * @param p The divisor.
     * @return The minimum length of the subarray to remove, or -1 if it's impossible.
     */
    public int minSubarray(int[] nums, int p) {
        int n = nums.length;
        long totalSum = 0;
        for (int num : nums) {
            totalSum = (totalSum + num) % p;
        }

        int remainder = (int) totalSum;
        if (remainder == 0) {
            return 0;
        }

        HashMap<Integer, Integer> modMap = new HashMap<>();
        modMap.put(0, -1);

        long currentSum = 0;
        int minLength = n;

        for (int i = 0; i < n; ++i) {
            currentSum = (currentSum + nums[i]) % p;
            int target = (int) ((currentSum - remainder + p) % p);

            if (modMap.containsKey(target)) {
                minLength = Math.min(minLength, i - modMap.get(target));
            }

            modMap.put((int) currentSum, i);
        }

        return minLength == n ? -1 : minLength;
    }
}