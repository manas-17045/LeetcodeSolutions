// Leetcode 3020: Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/
// Solved on 13th of November, 2025
import java.util.*;

class Solution {
    /**
     * Finds the maximum length of a subset where for any element `x` in the subset,
     * `x*x` is also in the subset, and `sqrt(x)` is also in the subset.
     *
     * @param nums An array of integers.
     * @return The maximum length of such a subset.
     */
    public int maximumLength(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int v : nums) {
            freq.put(v, freq.getOrDefault(v, 0) + 1);
        }
        int ans = 1;
        if (freq.containsKey(1)) {
            int c = freq.get(1);
            ans = Math.max(ans, c % 2 == 1 ? c : c - 1);
        }
        long limit = 1000000000L;
        for (int key : freq.keySet()) {
            if (key == 1) {
                continue;
            }
            long val = key;
            List<Long> powers = new ArrayList<>();
            while (val <= limit && freq.containsKey((int)val)) {
                powers.add(val);
                if (val > limit / val) {
                    break;
                }
                val = val * val;
            }
            int m = powers.size();
            for (int k = 0; k < m; k++) {
                boolean ok = true;
                for (int i = 0; i < k; i++) {
                    int cnt = freq.get((int)(long)powers.get(i));
                    if (cnt < 2) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) {
                    break;
                }
                int centerCnt = freq.get((int)(long)powers.get(k));
                if (centerCnt >= 1) {
                    ans = Math.max(ans, 2 * k + 1);
                }
            }
        }
        return ans;
    }
}