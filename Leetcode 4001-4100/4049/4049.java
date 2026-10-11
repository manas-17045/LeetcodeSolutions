// Leetcode 4049: Count Values With Equally Spaced Occurrences II
// https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-ii/
// Solved on 11th of October, 2026
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Counts the number of distinct integers in the array that appear at least
     * three times and have all occurrences spaced at equal index intervals.
     *
     * @param nums the input array of integers
     * @return the number of distinct special integers
     */
    public int countSpecialIntegers(int[] nums) {
        Map<Integer, int[]> tracker = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int[] state = tracker.get(num);
            if (state == null) {
                tracker.put(num, new int[]{1, i, 0});
            } else if (state[2] != -1) {
                if (state[0] == 1) {
                    state[2] = i - state[1];
                    state[0] = 2;
                    state[1] = i;
                } else if (i - state[1] == state[2]) {
                    state[0]++;
                    state[1] = i;
                } else {
                    state[2] = -1;
                }
            }
        }
        int specialCount = 0;
        for (int[] state : tracker.values()) {
            if (state[0] >= 3 && state[2] != -1) {
                specialCount++;
            }
        }
        return specialCount;
    }
}