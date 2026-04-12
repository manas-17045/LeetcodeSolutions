// Leetcode 1320: Minimum Distance to Type a Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
// Solved on 12th of April, 2026
class Solution {
    /**
     * Calculates the minimum total distance to type a word using two fingers.
     *
     * @param word The string to be typed.
     * @return The minimum distance required to type the entire word.
     */
    public int minimumDistance(String word) {
        int[] dp = new int[27];
        for (int i = 0; i < 26; i++) {
            dp[i] = 30000;
        }
        int prev = 26;

        for (int i = 0; i < word.length(); i++) {
            int curr = word.charAt(i) - 'A';
            int[] nextDp = new int[27];
            for (int j = 0; j < 27; j++) {
                nextDp[j] = 30000;
            }

            for (int other = 0; other < 27; other++) {
                if (dp[other] != 30000) {
                    int movePrev = dp[other] + getDist(prev, other);
                    if (movePrev < nextDp[other]) {
                        nextDp[other] = movePrev;
                    }

                    int moveOther = dp[other] + getDist(other, curr);
                    if (moveOther < nextDp[curr]) {
                        nextDp[curr] = moveOther;
                    }
                }
            }
            dp = nextDp;
            prev = curr;
        }

        int minTotal = 30000;
        for (int cost : dp) {
            if (cost < minTotal) {
                minTotal = cost;
            }
        }

        return minTotal;
    }

    private int getDist(int from, int to) {
        if (from == 26) {
            return 0;
        }
        int fromRow = from / 6;
        int fromCol = from % 6;
        int toRow = to / 6;
        int toCol = to % 6;
        return Math.abs(fromRow - toRow) + Math.abs(fromCol - toCol);
    }
}