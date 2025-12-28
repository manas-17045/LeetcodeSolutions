// Leetcode 3694: Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/
// Solved on 28th of December, 2025
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Calculates the number of distinct points reachable after removing a substring of length k.
     * The string `s` represents a sequence of moves ('U', 'D', 'L', 'R').
     *
     * @param s The input string representing the moves.
     * @param k The length of the substring to be removed.
     * @return The number of distinct points reachable.
     */
    public int distinctPoints(String s, int k) {
        Set<Long> seenPoints = new HashSet<>();
        long windowX = 0;
        long windowY = 0;

        for (int i = 0; i < k; i++) {
            char c = s.charAt(i);
            if (c == 'U') {
                windowY++;
            } else if (c == 'D') {
                windowY--;
            } else if (c == 'L') {
                windowX--;
            } else if (c == 'R') {
                windowX++;
            }
        }

        seenPoints.add((windowX << 32) | (windowY & 0xFFFFFFFFL));

        for (int i = k; i < s.length(); i++) {
            char inChar = s.charAt(i);
            if (inChar == 'U') {
                windowY++;
            } else if (inChar == 'D') {
                windowY--;
            } else if (inChar == 'L') {
                windowX--;
            } else if (inChar == 'R') {
                windowX++;
            }

            char outChar = s.charAt(i - k);
            if (outChar == 'U') {
                windowY--;
            } else if (outChar == 'D') {
                windowY++;
            } else if (outChar == 'L') {
                windowX++;
            } else if (outChar == 'R') {
                windowX--;
            }

            seenPoints.add((windowX << 32) | (windowY & 0xFFFFFFFFL));
        }

        return seenPoints.size();
    }
}