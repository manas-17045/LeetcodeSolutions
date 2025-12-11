// Leetcode 2953: Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/
// Solved on 11th of December, 2025
class Solution {
    /**
     * Counts the number of "complete" substrings in a given word.
     * A substring is complete if all its characters appear exactly `k` times,
     * and the difference between any two adjacent characters is at most 2.
     * @param word The input string.
     * @param k The required frequency for each character in a complete substring.
     * @return The total count of complete substrings.
     */
    public int countCompleteSubstrings(String word, int k) {
        int n = word.length();
        int totalCompleteSubstrings = 0;
        int start = 0;

        for (int i = 0; i < n; i++) {
            if (i > 0 && Math.abs(word.charAt(i) - word.charAt(i - 1)) > 2) {
                totalCompleteSubstrings += countWithinSegment(word, k, start, i - 1);
                start = i;
            }
        }
        totalCompleteSubstrings += countWithinSegment(word, k, start, n - 1);

        return totalCompleteSubstrings;
    }

    private int countWithinSegment(String word, int k, int start, int end) {
        int count = 0;
        int segmentLength = end - start + 1;

        for (int uniqueChars = 1; uniqueChars <= 26; uniqueChars++) {
            int windowSize = uniqueChars * k;
            if (windowSize > segmentLength) {
                break;
            }

            int[] charCounts = new int[26];
            int matchCount = 0;

            for (int i = start; i < start + windowSize; i++) {
                int charIndex = word.charAt(i) - 'a';
                charCounts[charIndex]++;
                if (charCounts[charIndex] == k) {
                    matchCount++;
                } else if (charCounts[charIndex] == k + 1) {
                    matchCount--;
                }
            }

            if (matchCount == uniqueChars) {
                count++;
            }

            for (int i = start + windowSize; i <= end; i++) {
                int enteringCharIndex = word.charAt(i) - 'a';
                charCounts[enteringCharIndex]++;
                if (charCounts[enteringCharIndex] == k) {
                    matchCount++;
                } else if (charCounts[enteringCharIndex] == k + 1) {
                    matchCount--;
                }

                int leavingCharIndex = word.charAt(i - windowSize) - 'a';
                charCounts[leavingCharIndex]--;
                if (charCounts[leavingCharIndex] == k) {
                    matchCount++;
                } else if (charCounts[leavingCharIndex] == k - 1) {
                    matchCount--;
                }

                if (matchCount == uniqueChars) {
                    count++;
                }
            }
        }
        return count;
    }
}