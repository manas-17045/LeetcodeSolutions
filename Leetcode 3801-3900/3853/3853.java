// Leetcode 3853: Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/
// Solved on 1st of March, 2026
class Solution {
    /**
     * Merges characters in a string if identical characters are within a distance of k.
     *
     * @param s The input string to process.
     * @param k The maximum distance between two identical characters to trigger a merge.
     * @return The resulting string after all possible merges have been performed.
     */
    public String mergeCharacters(String s, int k) {
        StringBuilder stringBuilder = new StringBuilder(s);
        boolean hasMerged = true;
        while (hasMerged) {
            hasMerged = false;
            for (int i = 0; i < stringBuilder.length(); i++) {
                int maxRight = Math.min(i + k, stringBuilder.length() - 1);
                for (int j = i + 1; j <= maxRight; j++) {
                    if (stringBuilder.charAt(i) == stringBuilder.charAt(j)) {
                        stringBuilder.deleteCharAt(j);
                        hasMerged = true;
                        break;
                    }
                }
                if (hasMerged) {
                    break;
                }
            }
        }
        return stringBuilder.toString();
    }
}