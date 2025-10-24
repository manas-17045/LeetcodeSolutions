// Leetcode 2134: Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
// Solved on 24th of October, 2025
class Solution {
    /**
     * Calculates the minimum number of swaps required to group all 1's together in a circular binary array.
     *
     * @param nums The input circular binary array (containing only 0s and 1s).
     * @return The minimum number of swaps needed.
     */
    public int minSwaps(int[] nums) {
        int n = nums.length;
        
        // Count total number of 1's
        int totalOnes = 0;
        for (int num : nums) {
            totalOnes += num;
        }
        
        // Edge case: if no 1's or all 1's, no swaps needed
        if (totalOnes == 0 || totalOnes == n) {
            return 0;
        }
        
        // Find the window of size totalOnes with maximum 1's
        // Initial window
        int currentOnes = 0;
        for (int i = 0; i < totalOnes; i++) {
            currentOnes += nums[i];
        }
        
        int maxOnes = currentOnes;
        
        // Slide the window through the circular array
        // We need to check n windows in total (circular)
        for (int i = 0; i < n; i++) {
            // Remove the leftmost element of previous window
            currentOnes -= nums[i];
            // Add the new rightmost element (circular index)
            currentOnes += nums[(i + totalOnes) % n];
            // Update maximum
            maxOnes = Math.max(maxOnes, currentOnes);
        }
        
        // Minimum swaps = total 1's - maximum 1's already in a window
        return totalOnes - maxOnes;
    }
}