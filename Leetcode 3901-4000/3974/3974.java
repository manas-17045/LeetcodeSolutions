// Leetcode 3974: Maximum Total Sum of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/
// Solved on 18th of July, 2026
import java.util.Arrays;

class Solution {
    /**
     * Finds the maximum total sum of k selected elements from the array.
     * 
     * @param nums The input array of integers.
     * @param k The number of elements to select.
     * @param mul The multiplier.
     * @return The maximum total sum of k selected elements.
     */
    public long maxSum(int[] nums, int k, int mul) {
        Arrays.sort(nums);
        long totalSum = 0;
        int currentMul = mul;
        int index = nums.length - 1;
        for (int i = 0; i < k; i++) {
            long effectiveMul = Math.max(currentMul, 1);
            totalSum += (long) nums[index] * effectiveMul;
            currentMul--;
            index--;
        }
        return totalSum;
    }
}