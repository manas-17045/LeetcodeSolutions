// Leetcode 3755: Find Maximum Balanced XOR Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/
// Solved on 26th of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Finds the maximum length of a "balanced XOR subarray".
     * A subarray is balanced if the count of odd numbers equals the count of even numbers,
     * and the XOR sum of its elements is 0.
     * @param nums The input array of integers.
     * @return The maximum length of a balanced XOR subarray.
     */
    public int maxBalancedSubarray(int[] nums) {
        Map<Long, Integer> map = new HashMap<>();
        int n = nums.length;
        int xor = 0;
        int diff = 0;
        int maxLen = 0;
        int offset = n + 1;

        long initialKey = ((long) 0 << 32) | (0 + offset);
        map.put(initialKey, -1);

        for (int i = 0; i < n; i++) {
            xor ^= nums[i];
            
            if (nums[i] % 2 != 0) {
                diff++;
            } else {
                diff--;
            }

            long key = ((long) xor << 32) | (diff + offset);

            if (map.containsKey(key)) {
                maxLen = Math.max(maxLen, i - map.get(key));
            } else {
                map.put(key, i);
            }
        }
        return maxLen;
    }
}