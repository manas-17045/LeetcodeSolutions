// Leetcode 4021: Minimum Operations to Make a Rotated Palindrome I
// https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-i/
// Solved on 12th of September, 2026
class Solution {
    /**
     * Calculates the minimum number of operations (rotations and character increments)
     * required to transform the given string into a palindrome.
     *
     * @param s the input string consisting of lowercase English letters
     * @return the minimum total operations needed to make the string a palindrome
     */
    public int minOperations(String s) {
        int n = s.length();
        char[] chars = s.toCharArray();
        int minOps = Integer.MAX_VALUE;

        for (int r = 0; r < n; r++) {
            int currentOps = r;
            for (int i = 0; i < n / 2; i++) {
                int leftIndex = (r + i) % n;
                int rightIndex = (r + n - 1 - i) % n;
                int diff = Math.abs(chars[leftIndex] - chars[rightIndex]);
                currentOps += Math.min(diff, 26 - diff);
                if (currentOps >= minOps) {
                    break;
                }
            }
            minOps = Math.min(minOps, currentOps);
        }

        return minOps;
    }
}