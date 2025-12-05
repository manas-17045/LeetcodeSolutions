// Leetcode 3761: Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/
// Solved on 5th of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the minimum absolute distance between mirror pairs in the given array.
     * A mirror pair is defined as two numbers `nums[i]` and `nums[j]` where `nums[i]` is the reverse of `nums[j]`.
     * @param nums The input array of integers.
     * @return The minimum absolute distance between mirror pairs, or -1 if no such pair exists.
     */
    public int minMirrorPairDistance(int[] nums) {
        int minDistance = Integer.MAX_VALUE;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                minDistance = Math.min(minDistance, i - map.get(nums[i]));
            }
            int reversed = 0;
            int current = nums[i];
            while (current > 0) {
                reversed = reversed * 10 + current % 10;
                current /= 10;
            }
            map.put(reversed, i);
        }
        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
    }
}