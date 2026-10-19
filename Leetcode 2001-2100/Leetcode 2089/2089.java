// Leetcode 2089: Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/
// Solved on 19th of October, 2026
import java,util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Finds and returns all indices of the target value after sorting
     * the given array in non-decreasing order.
     *
     * @param nums the array of integers to evaluate
     * @param target the integer value whose sorted indices are to be found
     * @return a list of indices where target appears in the sorted array
     */
    public List<Integer> targetIndices(int[] nums, int target) {
        int countLessThan = 0;
        int countTarget = 0;

        for (int num : nums) {
            if (num < target) {
                countLessThan++;
            } else if (num == target) {
                countTarget++;
            }
        }
        
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < countTarget; i++) {
            result.add(countLessThan + i);
        }
        
        return result;
    }
}