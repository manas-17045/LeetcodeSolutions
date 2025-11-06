// Leetcode 3639: Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/
// Solved on 6th of November, 2025
class Solution {
    /**
     * Calculates the minimum time required to activate at least k substrings.
     * @param s The input string.
     * @param order An array representing the order in which characters are activated.
     * @param k The minimum number of substrings to activate.
     * @return The minimum time (index in 'order') to activate at least k substrings.
     */
    public int minTime(String s, int[] order, int k) {
        int n = s.length();
        long totalSub = (long) n * (n + 1) / 2;
        if (totalSub < k){
            return -1;
        }
        int low = 0;
        int high = n - 1;
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (check(s, order, mid, k, totalSub)){
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private boolean check(String s, int[] order, int t, int k, long totalSub) {
        int n = s.length();
        boolean[] star = new boolean[n];
        for (int i = 0; i <= t; i++){
            star[order[i]] = true;
        }
        long noStarSub = 0;
        int len = 0;
        for (int i = 0; i < n; i++) {
            if (!star[i]){
                len++;
            }
            else {
                if (len > 0) {
                    noStarSub += (long) len * (len + 1) / 2;
                    len = 0;
                }
            }
        }
        if (len > 0){
            noStarSub += (long) len * (len + 1) / 2;
        }
        long valid = totalSub - noStarSub;
        return valid >= k;
    }
}