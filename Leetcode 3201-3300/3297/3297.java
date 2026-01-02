// Leetcode 3297: Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/
// Solved on 2nd of January, 2026
class Solution{
    /**
     * Counts the number of substrings in word1 that can be rearranged to form word2.
     * @param word1 The string to search within.
     * @param word2 The target string to form.
     * @return The total count of valid substrings.
     */
    public long validSubsItringCount(String word1, String word2) {
        int[] charCounts = new int[26];
        for (int i = 0; i < word2.length(); i++) {
            charCounts[word2.charAt(i) - 'a']++;
        }

        long validCount = 0;
        int required = word2.length();
        int left = 0;
        int n = word1.length();

        for (int right = 0; right < n; right++) {
            int rightIndex = word1.charAt(right) - 'a';
            if (charCounts[rightIndex] > 0) {
                required--;
            }
            charCounts[rightIndex]--;

            while (required == 0) {
                int leftIndex = word1.charAt(left) - 'a';
                charCounts[leftIndex]++;
                if (charCounts[leftIndex] > 0) {
                    required++;
                }
                left++;
            }
            validCount += left;
        }

        return validCount;
    }
}