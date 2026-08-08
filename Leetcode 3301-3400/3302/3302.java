// Leetcode 3302: Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/
// Solved on 8th of August, 2026
class Solution {
    /**
     * Finds the lexicographically smallest valid subsequence of word1 that forms word2.
     * @param word1 The string from which to find the subsequence.
     * @param word2 The subsequence to find.
     * @return The lexicographically smallest valid subsequence of word1 that forms word2.
     */
    public int[] validSequence(String word1, String word2) {
        int length1 = word1.length();
        int length2 = word2.length();
        int[] lastIndices = new int[length2 + 1];
        lastIndices[length2] = length1;
        int pointer = length1 - 1;
        for (int j = length2 - 1; j >= 0; j--) {
            while (pointer >= 0 && word1.charAt(pointer) != word2.charAt(j)) {
                pointer--;
            }
            lastIndices[j] = pointer;
            if (pointer >= 0) {
                pointer--;
            }
        }
        int[] resultSequence = new int[length2];
        boolean hasChanged = false;
        int currentIndex = 0;
        for (int j = 0; j < length2; j++) {
            boolean foundMatch = false;
            while (currentIndex < length1) {
                if (word1.charAt(currentIndex) == word2.charAt(j)) {
                    resultSequence[j] = currentIndex;
                    currentIndex++;
                    foundMatch = true;
                    break;
                } else if (!hasChanged && lastIndices[j + 1] > currentIndex) {
                    resultSequence[j] = currentIndex;
                    hasChanged = true;
                    currentIndex++;
                    foundMatch = true;
                    break;
                }
                currentIndex++;
            }
            if (!foundMatch) {
                return new int[0];
            }
        }
        return resultSequence;
    }
}