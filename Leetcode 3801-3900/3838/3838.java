// Leetcode 3838: Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/
// Solved on 15th of February, 2026
class Solution {
    /**
     * Maps an array of words to a string based on the sum of weights of their characters.
     *
     * @param words   An array of strings to be processed.
     * @param weights An integer array of size 26 representing weights for 'a' through 'z'.
     * @return A string where each character corresponds to the mapped weight of each input word.
     */
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder resultBuilder = new StringBuilder();
        for (String word : words) {
            int totalWeight = 0;
            for (int i = 0; i < word.length(); i++) {
                totalWeight += weights[word.charAt(i) - 'a'];
            }
            int remainder = totalWeight % 26;
            char mappedChar = (char) ('z' - remainder);
            resultBuilder.append(mappedChar);
        }
        return resultBuilder.toString();
    }
}