// Leetcode 3729: Count Distinct Subarrays Divisible by K in Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/
// Solved on 2nd of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Counts the number of distinct subarrays whose sum is divisible by k.
     * @param nums The input array of integers.
     * @param k The divisor.
     * @return The number of distinct subarrays whose sum is divisible by k.
     */
    public long numGoodSubarrays(int[] nums, int k) {
        long totalCount = 0;
        long currentSum = 0;
        Map<Integer, Integer> modMap = new HashMap<>();
        modMap.put(0, 1);

        for (int num : nums) {
            currentSum += num;
            int mod = (int) (currentSum % k);
            int count = modMap.getOrDefault(mod, 0);
            totalCount += count;
            modMap.put(mod, count + 1);
        }

        long duplicates = 0;
        long distinct = 0;
        int n = nums.length;
        int i = 0;

        while (i < n) {
            int j = i;
            while (j < n && nums[j] == nums[i]) {
                j++;
            }

            long length = j - i;
            long value = nums[i];
            long gcdVal = gcd(value, k);
            long kPrime = k / gcdVal;
            long validCount = length / kPrime;

            if (validCount > 0) {
                distinct += validCount;
                long term1 = validCount * (length + 1);
                long term2 = kPrime * validCount * (validCount + 1) / 2;
                duplicates += (term1 - term2);
            }
            i = j;
        }

        return totalCount - duplicates + distinct;
    }

    private long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}