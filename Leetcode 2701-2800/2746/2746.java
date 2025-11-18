// Leetcode 2746: Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/
// Solved on 18th of November, 2025
class Solution {
    /**
     * Minimizes the length of the concatenated string by strategically overlapping words.
     * @param words An array of strings to be concatenated.
     * @return The minimum possible length of the concatenated string.
     */
    public int minimizeConcatenatedLength(String[] words) {
        int[][] dp = new int[26][26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                dp[i][j] = 100000000;
            }
        }

        String firstWord = words[0];
        int firstLen = firstWord.length();
        dp[firstWord.charAt(0) - 'a'][firstWord.charAt(firstLen - 1) - 'a'] = firstLen;

        for (int i = 1; i < words.length; i++) {
            int[][] nextDp = new int[26][26];
            for (int r = 0; r < 26; r++) {
                for (int c = 0; c < 26; c++) {
                    nextDp[r][c] = 100000000;
                }
            }

            String currentWord = words[i];
            int currentLen = currentWord.length();
            int startChar = currentWord.charAt(0) - 'a';
            int endChar = currentWord.charAt(currentLen - 1) - 'a';

            for (int j = 0; j < 26; j++) {
                for (int k = 0; k < 26; k++) {
                    if (dp[j][k] == 100000000) {
                        continue;
                    }

                    int len1 = dp[j][k] + currentLen - (k == startChar ? 1 : 0);
                    nextDp[j][endChar] = Math.min(nextDp[j][endChar], len1);

                    int len2 = dp[j][k] + currentLen - (endChar == j ? 1 : 0);
                    nextDp[startChar][k] = Math.min(nextDp[startChar][k], len2);
                }
            }
            dp = nextDp;
        }

        int minLength = 100000000;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                minLength = Math.min(minLength, dp[i][j]);
            }
        }
        return minLength;
    }
}