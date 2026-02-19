// Leetcode 696: Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/
// Solved on 19th of February, 2026
class Solution {
    /**
     * Counts the number of non-empty substrings that have the same number of 0's and 1's,
     * and all those 0's and all those 1's are grouped consecutively.
     * @param s The input binary string.
     * @return The total count of valid binary substrings.
     */
    public int countBinarySubstrings(String s) {
        int totalCount = 0;
        int prevLength = 0;
        int currLength = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i - 1) != s.charAt(i)) {
                totalCount += Math.min(prevLength, currLength);
                prevLength = currLength;
                currLength = 1;
            } else {
                currLength++;
            }
        }
        totalCount += Math.min(prevLength, currLength);
        return totalCount;
    }
}