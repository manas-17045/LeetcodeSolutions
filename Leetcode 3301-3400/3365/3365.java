// Leetcode 3365: Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/
// Solved on 5th of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Checks if string `s` can be rearranged into string `t` by splitting both into `k` substrings of equal length
     * and then rearranging the substrings of `s` to match `t`.
     *
     * @param s The source string.
     * @param t The target string.
     * @param k The number of substrings to split `s` and `t` into.
     * @return `true` if `s` can be rearranged to form `t`, `false` otherwise.
     */
    public boolean isPossibleToRearrange(String s, String t, int k) {
        int n = s.length();
        int size = n / k;
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i += size) {
            String sub = s.substring(i, i + size);
            map.put(sub, map.getOrDefault(sub, 0) + 1);
        }

        for (int i = 0; i < n; i += size) {
            String sub = t.substring(i, i + size);
            if (!map.containsKey(sub) || map.get(sub) == 0) {
                return false;
            }
            map.put(sub, map.get(sub) - 1);
        }

        return true;
    }
}