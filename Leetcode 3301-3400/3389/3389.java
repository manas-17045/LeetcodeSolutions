// Leetcode 3389: Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/
// Solved on 4th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of operations to make all character frequencies equal.
     * An operation consists of deleting a character.
     * @param s The input string.
     * @return The minimum number of operations.
     */
    public int makeStringGood(String s) {
        int[] count = new int[26];
        int maxFreq = 0;
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
            maxFreq = Math.max(maxFreq, count[c - 'a']);
        }

        int n = s.length();
        int minOps = n;

        for (int t = 1; t <= maxFreq; t++) {
            int costZero = count[0];
            int excessZero = count[0];

            int costKeep;
            int excessKeep;
            
            if (count[0] >= t) {
                costKeep = count[0] - t;
                excessKeep = count[0] - t;
            } else {
                costKeep = t - count[0];
                excessKeep = 0;
            }

            for (int i = 1; i < 26; i++) {
                int cur = count[i];

                int nextCostZero = Math.min(costZero, costKeep) + cur;
                int nextExcessZero = cur;

                int isoCost, deficit, nextExcessKeepCand;
                if (cur >= t) {
                    isoCost = cur - t;
                    deficit = 0;
                    nextExcessKeepCand = cur - t;
                } else {
                    isoCost = t - cur;
                    deficit = t - cur;
                    nextExcessKeepCand = 0;
                }

                int fromZero = costZero + isoCost - Math.min(excessZero, deficit);
                int fromKeep = costKeep + isoCost - Math.min(excessKeep, deficit);

                int nextCostKeep = Math.min(fromZero, fromKeep);
                int nextExcessKeep = nextExcessKeepCand;

                costZero = nextCostZero;
                excessZero = nextExcessZero;
                costKeep = nextCostKeep;
                excessKeep = nextExcessKeep;
            }
            minOps = Math.min(minOps, Math.min(costZero, costKeep));
        }

        return minOps;
    }
}