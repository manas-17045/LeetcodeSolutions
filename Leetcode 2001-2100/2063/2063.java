// Leetcode 2063: Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/
// Solved on 22nd of November, 2025
class Solution {
    /**
     * Calculates the total number of vowels across all possible substrings of a given word.
     * @param word The input string.
     * @return The total count of vowels in all substrings.
     */
    public int countVowels(String word) {
        long totalVowels = 0;
        long length = word.length();
        for (int i = 0; i < length; i++) {
            char c = word.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                totalVowels += (i + 1) * (length - i);
            }
        }
        return totalVowels;
    }
}