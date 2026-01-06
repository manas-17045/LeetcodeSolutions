// Leetcode 2896: Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/
// Solved on 6th of January, 2026
class Solution {
    /**
     * Calculates the minimum operations to make two strings equal.
     * @param s1 The first string.
     * @param s2 The second string.
     * @param x The cost of an operation to flip a single character.
     * @return The minimum cost to make s1 equal to s2, or -1 if it's impossible.
     */
    public int minOperations(String s1, String s2, int x) {
        int n = s1.length();
        int count = 0;
        int lastIndex = -1;
        int solved = 0;
        int open = 0;
        int prevSolved = 0;
        int prevOpen = 0;
        int inf = 100000000;

        for (int i = 0; i < n; i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                count++;
                if (count == 1) {
                    solved = inf;
                    open = x;
                    prevSolved = 0;
                    prevOpen = inf;
                } else {
                    int distance = i - lastIndex;
                    int newSolved = Math.min(open, prevSolved + distance);
                    int newOpen = Math.min(solved + x, prevOpen + distance);
                    prevSolved = solved;
                    prevOpen = open;
                    solved = newSolved;
                    open = newOpen;
                }
                lastIndex = i;
            }
        }

        if (count % 2 != 0) {
            return -1;
        }

        return solved;
    }
}