// Leetcode 2800: Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/
// Solved on 7th of January, 2026
class Solution {
    /**
     * Finds the shortest string that contains all three given strings as substrings.
     * If there are multiple such strings, returns the lexicographically smallest one.
     * @param a The first string.
     * @param b The second string.
     * @param c The third string.
     * @return The shortest string containing a, b, and c.
     */
    public String minimumString(String a, String b, String c) {
        String[] strs = {a, b, c};
        String result = "";
        int[][] permutations = {
            {0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}
        };

        for (int[] p : permutations) {
            String s1 = strs[p[0]];
            String s2 = strs[p[1]];
            String s3 = strs[p[2]];
            
            String merged = merge(merge(s1, s2), s3);
            
            if (result.isEmpty() || merged.length() < result.length() || 
               (merged.length() == result.length() && merged.compareTo(result) < 0)) {
                result = merged;
            }
        }
        return result;
    }

    private String merge(String s1, String s2) {
        if (s1.contains(s2)) {
            return s1;
        }
        for (int i = Math.min(s1.length(), s2.length()); i > 0; i--) {
            if (s1.endsWith(s2.substring(0, i))) {
                return s1 + s2.substring(i);
            }
        }
        return s1 + s2;
    }
}