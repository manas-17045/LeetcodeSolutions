// Leetcode 4043: Count Rotations With Exactly K Equal Adjacent Pairs
// https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/
// Solved on 4th of October, 2026
class Solution {
    /**
     * Calculates the number of cyclic rotations of a string that contain
     * exactly k equal adjacent character pairs.
     *
     * @param s the string to evaluate
     * @param k the target count of equal adjacent pairs
     * @return the number of cyclic rotations whose score equals k
     */
    public int countRotations(String s, int k) {
        int length = s.length();
        int totalEqualPairs = 0;

        for (int i = 0; i < length; i++) {
            int nextIndex = (i + 1) % length;
            if (s.charAt(i) == s.charAt(nextIndex)) {
                totalEqualPairs++;
            }
        }

        if (k == totalEqualPairs - 1) {
            return totalEqualPairs;
        }

        if (k == totalEqualPairs) {
            return length - totalEqualPairs;
        }

        return 0;
    }
}