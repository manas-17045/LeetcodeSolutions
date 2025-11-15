// Leetcode 3234: Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
// Solved on 15th of November, 2025
import java.util.ArrayList;

class Solution {
    /**
     * Counts the number of substrings with dominant ones.
     * @param s The input string consisting of '0's and '1's.
     * @return The number of substrings where the count of '1's is greater than or equal to the count of '0's squared.
     */
    public int numberOfSubstrings(String s) {
        int n = s.length();
        ArrayList<Integer> zeroPos = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0'){
                zeroPos.add(i);
            }
        }
        int m = zeroPos.size();
        long ans = 0;
        int prev = -1;
        for (int i = 0; i <= m; i++) {
            int cur = (i == m ? n : zeroPos.get(i));
            int gap = cur - prev - 1;
            if (gap > 0) {
                ans += (long) gap * (gap + 1) / 2;
            }
            prev = cur;
        }
        for (int k = 1; k <= m; k++) {
            long requiredLen = (long) k + (long) k * k;
            if (requiredLen > n) {
                break;
            }
            for (int i = 0; i + k - 1 < m; i++) {
                int leftBound = (i == 0 ? 0 : zeroPos.get(i - 1) + 1);
                int startMax = zeroPos.get(i);
                int endMin = zeroPos.get(i + k - 1);
                int endMax = (i + k < m ? zeroPos.get(i + k) - 1 : n - 1);
                int e1 = Math.max(endMin, (int)Math.max(endMin, requiredLen + leftBound - 1));
                if (endMax < e1) {
                    continue;
                }
                int thresh = (int)(requiredLen + startMax - 1);
                long add = 0;
                if (e1 <= Math.min(endMax, thresh - 1)) {
                    int a = e1;
                    int b = Math.min(endMax, thresh - 1);
                    long terms = b - a + 1;
                    long first = (long)a - requiredLen + 1 - leftBound + 1;
                    long last = (long)b - requiredLen + 1 - leftBound + 1;
                    add += terms * (first + last) / 2;
                }
                int s2 = Math.max(e1, thresh);
                if (s2 <= endMax) {
                    long terms = endMax - s2 + 1;
                    long val = startMax - leftBound + 1;
                    add += terms * val;
                }
                if (add > 0) {
                    ans += add;
                }
            }
        }
        return (int) ans;
    }
}