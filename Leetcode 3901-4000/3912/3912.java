// Leetcode 3912: Valid Elements in an Array
// https://leetcode.com/problems/valid-elements-in-an-array/
// Solved on 10th of May, 2026
import java.util.List;
import java.util.ArrayList;

class Solution {
    /**
     * Finds and returns a list of valid elements from the given array based on local maxima criteria.
     * 
     * @param nums An array of integers to be evaluated.
     * @return A List of integers containing the elements identified as valid.
     */
    public List<Integer> findValidElements(int[] nums) {
        List<Integer> validElements = new ArrayList<>();
        int n = nums.length;
        
        if (n == 0) {
            return validElements;
        }
        
        if (n == 1) {
            validElements.add(nums[0]);
            return validElements;
        }
        
        int[] rightMax = new int[n];
        rightMax[n - 1] = nums[n - 1];
        
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], nums[i]);
        }
        
        validElements.add(nums[0]);
        int currentLeftMax = nums[0];
        
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] > currentLeftMax || nums[i] > rightMax[i + 1]) {
                validElements.add(nums[i]);
            }
            currentLeftMax = Math.max(currentLeftMax, nums[i]);
        }
        
        validElements.add(nums[n - 1]);
        
        return validElements;
    }
}