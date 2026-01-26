// Leetcode 3819: Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/
// Solved on 26th of January, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Rotates the non-negative elements in the array by k positions.
     *
     * @param nums The input array of integers.
     * @param k The number of positions to rotate.
     * @return The modified array with non-negative elements rotated.
     */
    public int[] rotateElements(int[] nums, int k) {
        List<Integer> nonNegatives = new ArrayList<>();
        for (int num : nums) {
            if (num >= 0) {
                nonNegatives.add(num);
            }
        }

        if (nonNegatives.isEmpty()) {
            return nums;
        }

        int count = nonNegatives.size();
        k = k % count;

        int listIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= 0) {
                nums[i] = nonNegatives.get((listIndex + k) % count);
                listIndex++;
            }
        }

        return nums;
    }
}