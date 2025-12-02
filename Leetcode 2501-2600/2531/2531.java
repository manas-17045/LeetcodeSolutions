// Leetcode 2531: Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/
// Solved on 2nd of November, 2025
class Solution {
    public boolean isItPossible(String word1, String word2) {
        /**
         * Checks if it's possible to make the number of distinct characters equal in two words by swapping one character.
         * @param word1 The first word.
         * @param word2 The second word.
         * @return True if it's possible to make the number of distinct characters equal, false otherwise.
         */
        int[] count1 = new int[26];
        int[] count2 = new int[26];

        for (int i = 0; i < word1.length(); i++) {
            count1[word1.charAt(i) - 'a']++;
        }
        for (int i = 0; i < word2.length(); i++) {
            count2[word2.charAt(i) - 'a']++;
        }

        int distinct1 = 0;
        int distinct2 = 0;
        for (int i = 0; i < 26; i++) {
            if (count1[i] > 0) {
                distinct1++;
            }
            if (count2[i] > 0) {
                distinct2++;
            }
        }

        for (int i = 0; i < 26; i++) {
            if (count1[i] == 0) continue;
            for (int j = 0; j < 26; j++) {
                if (count2[j] == 0) {
                    continue;
                }

                if (i == j) {
                    if (distinct1 == distinct2) {
                        return true;
                    }
                    continue;
                }

                int newDistinct1 = distinct1;
                int newDistinct2 = distinct2;

                if (count1[i] == 1) {
                    newDistinct1--;
                }
                if (count1[j] == 0) {
                    newDistinct1++;
                }

                if (count2[j] == 1) {
                    newDistinct2--;
                }
                if (count2[i] == 0) {
                    newDistinct2++;
                }

                if (newDistinct1 == newDistinct2) {
                    return true;
                }
            }
        }
        return false;
    }
}