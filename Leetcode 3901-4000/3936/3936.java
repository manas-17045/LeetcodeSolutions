// Leetcode 3936: Minimum Swaps to Move Zeros to End
// https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/
// Solved on 4th of June, 2026
class Solution {
    /**
     * Calculates the minimum number of swaps required to move all zeros to the end of the array.
     * @param nums An integer array.
     * @return The minimum number of swaps needed.
     */
    public int minimumSwaps(int[] nums) {
        int zeroCount = 0;
        for (int num : nums) {
            if (num == 0) {
                zeroCount++;
            }
        }
        int swaps = 0;
        int n = nums.length;
        for (int i = n - zeroCount; i < n; i++) {
            if (nums[i] != 0) {
                swaps++;
            }
        }
        return swaps;
    }
}