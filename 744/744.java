// Leetcode 744: Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/
// Solved on 31st of January, 2026
class Solution {
    /**
     * Finds the smallest character in the array that is lexicographically greater than the target.
     *
     * @param letters A sorted array of characters in non-decreasing order.
     * @param target  The character to compare against.
     * @return The smallest character in letters that is greater than target, or the first character if none exist.
     */
    public char nextGreatestLetter(char[] letters, char target) {
        int start = 0;
        int end = letters.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (letters[mid] <= target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return letters[start % letters.length];
    }
}