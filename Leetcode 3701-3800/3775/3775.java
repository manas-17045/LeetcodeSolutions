// Leetcode 3775: Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/
// Solved on 25th of December, 2025
class Solution {
    /**
     * Reverses words in a string that have the same vowel count as the first word.
     * @param s The input string.
     * @return The modified string with relevant words reversed.
     */
    public String reverseWords(String s) {
        int length = s.length();
        int firstSpaceIndex = s.indexOf(' ');

        if (firstSpaceIndex == -1) {
            return s;
        }

        int targetVowelCount = countVowels(s, 0, firstSpaceIndex);
        StringBuilder result = new StringBuilder(length);
        result.append(s, 0, firstSpaceIndex);

        int start = firstSpaceIndex + 1;
        while (start < length) {
            result.append(' ');
            int end = s.indexOf(' ', start);
            if (end == -1) {
                end = length;
            }

            int currentVowelCount = countVowels(s, start, end);

            if (currentVowelCount == targetVowelCount) {
                for (int i = end - 1; i >= start; i--) {
                    result.append(s.charAt(i));
                }
            } else {
                result.append(s, start, end);
            }
            start = end + 1;
        }

        return result.toString();
    }

    private int countVowels(String s, int start, int end) {
        int count = 0;
        for (int i = start; i < end; i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }
        return count;
    }
}