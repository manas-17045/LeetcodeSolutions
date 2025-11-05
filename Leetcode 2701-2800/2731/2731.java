// Leetcode 2731: Movement of Robots
// https://leetcode.com/problems/movement-of-robots/
// Solved on 5th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the sum of distances between all pairs of robots after `d` seconds.
     * @param nums An array of integers representing the initial positions of the robots.
     * @param s A string representing the initial directions of the robots ('R' for right, 'L' for left).
     * @param d An integer representing the time in seconds.
     * @return The sum of distances between all pairs of robots, modulo 10^9 + 7.
     */
    public int sumDistance(int[] nums, String s, int d) {
        int n = nums.length;
        long MOD = 1000000007L;
        long[] pos = new long[n];
        for (int i = 0; i < n; i++) {
            pos[i] = nums[i] + (s.charAt(i) == 'R' ? (long) d : -(long) d);
        }
        
        Arrays.sort(pos);
        long res = 0;
        long prefix = 0;
        for (int i = 0; i < n; i++) {
            long cur = pos[i] * i - prefix;
            cur %= MOD;
            res += cur;
            res %= MOD;
            prefix += pos[i];
        }
        if (res < 0) {
            res += MOD;
        }
        return (int) res;
    }
}