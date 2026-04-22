// Leetcode 2452: Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/
// Solved on 22nd of April, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Finds all words from the queries array that are within two edits of any word in the dictionary.
     * An edit is defined as changing one character at a specific index.
     * 
     * @param queries An array of strings to be checked.
     * @param dictionary An array of strings to compare against.
     * @return A list of strings from queries that have at most two character differences with at least one word in the dictionary.
     */
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        List<String> validQueries = new ArrayList<>();
        for (String query : queries) {
            for (String word : dictionary) {
                int editCount = 0;
                for (int i = 0; i < query.length(); i++) {
                    if (query.charAt(i) != word.charAt(i)) {
                        editCount++;
                    }
                    if (editCount > 2) {
                        break;
                    }
                }
                if (editCount <= 2) {
                    validQueries.add(query);
                    break;
                }
            }
        }
        return validQueries;
    }
}