// Leetcode 1807: Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
// Solved on 27th of November, 2025
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    /**
     * Evaluates a string by replacing bracketed keys with their corresponding values from a knowledge base.
     * If a key is not found, it is replaced with a '?'.
     * @param s The input string containing bracketed keys.
     * @param knowledge A list of key-value pairs, where each inner list contains [key, value].
     * @return The evaluated string with keys replaced by their values or '?'.
     */
    public String evaluate(String s, List<List<String>> knowledge) {
        Map<String, String> map = new HashMap<>();
        for (List<String> pair : knowledge) {
            map.put(pair.get(0), pair.get(1));
        }
        
        StringBuilder sb = new StringBuilder();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '(') {
                int j = s.indexOf(')', i + 1);
                String key = s.substring(i + 1, j);
                sb.append(map.getOrDefault(key, "?"));
                i = j;
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}