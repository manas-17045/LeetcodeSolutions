// Leetcode 3678: Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/
// Solved on 1st of April, 2026
class Solution {
    /**
     * Finds the smallest positive integer that is not present in the array and is greater than the average.
     *
     * @param nums An array of integers.
     * @return The smallest absent positive integer greater than the average of the array.
     */
    public int smallestAbsent(int[] nums) {
        int sum = 0;
        boolean[] seen = new boolean[201];
        for (int num : nums) {
            sum += num;
            seen[num + 100] = true;
        }
        int target = (int) Math.floor((double) sum / nums.length) + 1;
        target = Math.max(1, target);
        while (target <= 100 && seen[target + 100]) {
            target++;
        }
        return target;
    }
}