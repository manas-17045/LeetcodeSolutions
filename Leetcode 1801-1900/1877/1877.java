// Leetcode 1877: Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
// Solved on 24th of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Minimizes the maximum pair sum in the array.
     *
     * @param nums The input array of even length.
     * @return The minimized maximum pair sum.
     */
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int maxPairSum = 0;
        int n = nums.length;
        for (int i = 0; i < n / 2; i++) {
            int currentPairSum = nums[i] + nums[n - 1 - i];
            if (currentPairSum > maxPairSum) {
                maxPairSum = currentPairSum;
            }
        }
        return maxPairSum;
    }
}