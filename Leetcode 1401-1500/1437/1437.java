// Leetcode 1437: Check If All 1's Are at Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
// Solved on 17th of November, 2025
class Solution {
    /**
     * Checks if all 1's in the given array are at least k places away from each other.
     * @param nums The input array of 0s and 1s.
     * @param k The minimum distance required between any two 1s.
     * @return True if all 1s are at least k places away, false otherwise.
     */
    public boolean kLengthApart(int[] nums, int k) {
        int prevIndex = -k - 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (i - prevIndex - 1 < k) {
                    return false;
                }
                prevIndex = i;
            }
        }
        return true;
    }
}