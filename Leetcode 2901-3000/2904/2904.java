// Leetcode 2904: Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
// Solved on 26th of August, 2026
class Solution {
    /**
     * Finds the shortest and lexicographically smallest beautiful substring
     * containing exactly k ones in a given binary string.
     *
     * @param s the binary string to search within
     * @param k the exact count of ones required in the substring
     * @return the shortest and lexicographically smallest beautiful substring,
     *         or an empty string if no such substring exists
     */
    public String shortestBeautifulSubstring(String s, int k) {
        int n = s.length();
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                count++;
            }
        }

        if (count < k) {
            return "";
        }

        int[] indices = new int[count];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                indices[idx++] = i;
            }
        }

        String result = "";
        int minLength = Integer.MAX_VALUE;

        for (int i = 0; i <= count - k; i++) {
            int left = indices[i];
            int right = indices[i + k - 1];
            int currentLength = right - left + 1;
            String current = s.substring(left, right + 1);

            if (currentLength < minLength) {
                minLength = currentLength;
                result = current;
            } else if (currentLength == minLength && current.compareTo(result) < 0) {
                result = current;
            }
        }

        return result;
    }
}