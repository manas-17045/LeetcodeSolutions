// Leetcode 1784: Check if Binary STring Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
// Solved on 6th of March, 2026
class Solution {
    /**
     * Checks if the binary string contains at most one contiguous segment of ones.
     * @param s A binary string consisting only of '0' and '1'.
     * @return true if there is at most one segment of ones, false otherwise.
     */
    public boolean checkOnesSegment(String s) {
        return !s.contains("01");
    }
}