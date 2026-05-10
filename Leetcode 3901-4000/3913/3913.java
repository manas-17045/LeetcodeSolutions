// Leetcode 3913: Sort Vowels by Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/
// Solved on 10th of May, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Sorts the vowels in the given string based on their frequency in descending order.
     * If frequencies are equal, the vowel that appeared first in the original string comes first.
     * @param s The input string containing lowercase English letters.
     * @return A new string where non-vowel characters remain in place and vowels are reordered.
     */
    public String sortVowels(String s) {
        int n = s.length();
        int[] counts = new int[256];
        int[] firstOccur = new int[256];
        java.util.Arrays.fill(firstOccur, -1);
        
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            counts[c]++;
            if (firstOccur[c] == -1) {
                firstOccur[c] = i;
            }
        }

        char[] vowels = {'a', 'e', 'i', 'o', 'u'};
        java.util.List<Character> presentVowels = new java.util.ArrayList<>();
        for (char v : vowels) {
            if (counts[v] > 0) {
                presentVowels.add(v);
            }
        }

        presentVowels.sort((a, b) -> {
            if (counts[a] != counts[b]) {
                return Integer.compare(counts[b], counts[a]);
            }
            return Integer.compare(firstOccur[a], firstOccur[b]);
        });

        char[] result = s.toCharArray();
        int vowelIdx = 0;
        int currentVowelCount = 0;
        
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (isVowel(c)) {
                char targetVowel = presentVowels.get(vowelIdx);
                result[i] = targetVowel;
                currentVowelCount++;
                if (currentVowelCount == counts[targetVowel]) {
                    vowelIdx++;
                    currentVowelCount = 0;
                }
            }
        }

        return new String(result);
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}