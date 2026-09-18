// Leetcode 1520: Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
// Solved on 18th of September, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Finds the maximum number of non-overlapping substrings of minimum total length
     * such that any substring containing a character also contains all occurrences of that character.
     *
     * @param s the input string consisting of lowercase English letters
     * @return a list of non-overlapping substrings satisfying the conditions
     */
    public List<String> maxNumOfSubstrings(String s) {
        int stringLength = s.length();
        int[] firstOccurrence = new int[26];
        int[] lastOccurrence = new int[26];
        Arrays.fill(firstOccurrence, -1);
        Arrays.fill(lastOccurrence, -1);

        for (int i = 0; i < stringLength; i++) {
            int charIndex = s.charAt(i) - 'a';
            if (firstOccurrence[charIndex] == -1) {
                firstOccurrence[charIndex] = i;
            }
            lastOccurrence[charIndex] = i;
        }

        List<int[]> validIntervals = new ArrayList<>();

        for (int i = 0; i < 26; i++) {
            if (firstOccurrence[i] == -1) {
                continue;
            }

            int leftBound = firstOccurrence[i];
            int rightBound = lastOccurrence[i];
            boolean isValid = true;

            for (int j = leftBound; j <= rightBound; j++) {
                int charIndex = s.charAt(j) - 'a';
                if (firstOccurrence[charIndex] < leftBound) {
                    isValid = false;
                    break;
                }
                rightBound = Math.max(rightBound, lastOccurrence[charIndex]);
            }

            if (isValid) {
                validIntervals.add(new int[]{leftBound, rightBound});
            }
        }

        validIntervals.sort((firstInterval, secondInterval) -> {
            if (firstInterval[1] != secondInterval[1]) {
                return Integer.compare(firstInterval[1], secondInterval[1]);
            }
            return Integer.compare(secondInterval[0], firstInterval[0]);
        });

        List<String> result = new ArrayList<>();
        int lastEnd = -1;

        for (int[] interval : validIntervals) {
            if (interval[0] > lastEnd) {
                result.add(s.substring(interval[0], interval[1] + 1));
                lastEnd = interval[1];
            }
        }

        return result;
    }
}