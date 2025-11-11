// Leetcode 3314: Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
// Solved on 11th of November, 2025
import java.util.List;

class Solution {
    /**
     * Constructs an array `ans` where `ans[i]` is the smallest non-negative integer `x`
     * such that `(x | (x + 1))` equals `nums[i]`. If no such `x` exists, `ans[i]` is -1.
     * @param nums A list of integers.
     * @return An array `ans` where `ans[i]` is the found `x` or -1.
     */
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int p = nums.get(i);
            int foundVal = -1;
            for (int x = 0; x < p; x++) {
                if ((x | (x + 1)) == p) {
                    foundVal = x;
                    break;
                }
            }
            ans[i] = foundVal;
        }
        return ans;
    }
}