// Leetcode 3999: Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/
// Solved on 21st of August, 2026
import java.util.HashSet;
import java.util.Set;
class Solution {
    /**
     * Calculates the number of distinct word groups based on the canonical 
     * cyclic representations of characters at even and odd indices.
     *
     * @param words array of strings to be categorized into groups
     * @return the total count of unique groups formed
     */
    public int minimumGroups(String[] words) {
        Set<String> uniqueGroups = new HashSet<>();
        for (String word : words) {
            int length = word.length();
            int evenLength = (length + 1) / 2;
            int oddLength = length / 2;
            char[] evenChars = new char[evenLength];
            char[] oddChars = new char[oddLength];
            for (int i = 0; i < length; i++) {
                if (i % 2 == 0) {
                    evenChars[i / 2] = word.charAt(i);
                } else {
                    oddChars[i / 2] = word.charAt(i);
                }
            }
            String canonicalEven = getCanonical(evenChars);
            String canonicalOdd = getCanonical(oddChars);
            uniqueGroups.add(canonicalEven + "#" + canonicalOdd);
        }
        return uniqueGroups.size();
    }

    private String getCanonical(char[] sequence) {
        int length = sequence.length;
        if (length <= 1) {
            return new String(sequence);
        }
        int i = 0;
        int j = 1;
        int k = 0;
        while (i < length && j < length && k < length) {
            char charI = sequence[(i + k) % length];
            char charJ = sequence[(j + k) % length];
            if (charI == charJ) {
                k++;
            } else {
                if (charI > charJ) {
                    i += k + 1;
                } else {
                    j += k + 1;
                }
                if (i == j) {
                    j++;
                }
                k = 0;
            }
        }
        int startIndex = Math.min(i, j);
        char[] result = new char[length];
        for (int m = 0; m < length; m++) {
            result[m] = sequence[(startIndex + m) % length];
        }
        return new String(result);
    }
}