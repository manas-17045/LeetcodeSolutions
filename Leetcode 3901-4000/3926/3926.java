// Leetcode 3926: Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/
// Solved on 24th of May, 2026
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Counts the occurrences of specific query words within a text formed by concatenating multiple chunks.
     *
     * @param chunks  An array of strings that, when concatenated, form the full text to be analyzed.
     * @param queries An array of strings representing the words to search for in the processed text.
     * @return An array of integers where each element represents the frequency of the corresponding query word.
     */
    public int[] countWordOccurrences(String[] chunks, String[] queries) {
        StringBuilder builder = new StringBuilder();
        for (String chunk : chunks) {
            builder.append(chunk);
        }
        
        char[] characters = builder.toString().toCharArray();
        int length = characters.length;
        Map<String, Integer> wordCount = new HashMap<>();
        StringBuilder wordBuilder = new StringBuilder();
        
        for (int i = 0; i < length; i++) {
            char current = characters[i];
            if (current >= 'a' && current <= 'z') {
                wordBuilder.append(current);
            } else if (current == '-') {
                if (i > 0 && i < length - 1 && 
                    characters[i - 1] >= 'a' && characters[i - 1] <= 'z' && 
                    characters[i + 1] >= 'a' && characters[i + 1] <= 'z') {
                    wordBuilder.append(current);
                } else {
                    if (wordBuilder.length() > 0) {
                        String word = wordBuilder.toString();
                        wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
                        wordBuilder.setLength(0);
                    }
                }
            } else {
                if (wordBuilder.length() > 0) {
                    String word = wordBuilder.toString();
                    wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
                    wordBuilder.setLength(0);
                }
            }
        }
        
        if (wordBuilder.length() > 0) {
            String word = wordBuilder.toString();
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }
        
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            result[i] = wordCount.getOrDefault(queries[i], 0);
        }
        
        return result;
    }
}