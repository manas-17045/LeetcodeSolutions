// Leetcode 3731: Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/
// Solved on 4th of August, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Finds the missing elements in an array of integers.
     * 
     * @param nums The array of integers.
     * @return A list of missing integers.
     */
    public List<Integer> findMissingElements(int[] nums) {
        int minVal = nums[0];
        int maxVal = nums[0];
        for (int num : nums) {
            if (num < minVal) {
                minVal = num;
            }
            if (num > maxVal) {
                maxVal = num;
            }
        }
        boolean[] present = new boolean[maxVal + 1];
        for (int num : nums) {
            present[num] = true;
        }
        List<Integer> result = new ArrayList<>();
        for (int i = minVal; i <= maxVal; i++) {
            if (!present[i]) {
                result.add(i);
            }
        }
        return result;
    }
}