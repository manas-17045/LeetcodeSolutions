// Leetcode 3839: Number of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/
// Solved on 16th of February, 2026
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the number of groups where at least two words share the same prefix of length k.
     *
     * @param words An array of strings to be processed.
     * @param k     The length of the prefix to consider for grouping.
     * @return      The total number of prefix-connected groups.
     */
    public int prefixConnected(String[] words, int k) {
        Map<String, Integer> prefixCounts = new HashMap<>();
        for (String word : words) {
            if (word.length() >= k) {
                String prefix = word.substring(0, k);
                prefixCounts.put(prefix, prefixCounts.getOrDefault(prefix, 0) + 1);
            }
        }

        int groupCount = 0;
        for (int count : prefixCounts.values()) {
            if (count >= 2) {
                groupCount++;
            }
        }
        return groupCount;
    }
}