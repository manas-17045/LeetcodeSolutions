// Leetcode 3869: Count Fancy Numbers in a Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/
// Solved on 19th of March, 2026
import java.util.HashSet;

class Solution {
    /**
     * Counts the number of "fancy" numbers in the range [l, r].
     * 
     * @param l The lower bound of the range (inclusive).
     * @param r The upper bound of the range (inclusive).
     * @return The total count of fancy numbers within the specified range.
     */
    public long countFancy(long l, long r) {
        boolean[] goodSum = new boolean[150];
        for (int i = 1; i < 150; i++) {
            goodSum[i] = checkGood(i);
        }
        
        long ans = solve(r, goodSum) - solve(l - 1, goodSum);
        
        HashSet<Long> goodNums = new HashSet<>();
        for (int mask = 1; mask < 512; mask++) {
            long val = 0;
            for (int i = 0; i < 9; i++) {
                if ((mask & (1 << i)) != 0) {
                    val = val * 10 + (i + 1);
                }
            }
            goodNums.add(val);
        }
        for (int mask = 1; mask < 1024; mask++) {
            long val = 0;
            for (int i = 9; i >= 0; i--) {
                if ((mask & (1 << i)) != 0) {
                    val = val * 10 + i;
                }
            }
            goodNums.add(val);
        }
        
        for (long x : goodNums) {
            if (x >= l && x <= r) {
                int s = 0;
                long temp = x;
                while (temp > 0) {
                    s += temp % 10;
                    temp /= 10;
                }
                if (!goodSum[s]) {
                    ans++;
                }
            }
        }
        
        return ans;
    }
    
    private boolean checkGood(long x) {
        if (x < 10) {
            return true;
        }
        String s = Long.toString(x);
        boolean inc = true;
        boolean dec = true;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) <= s.charAt(i - 1)) {
                inc = false;
            }
            if (s.charAt(i) >= s.charAt(i - 1)) {
                dec = false;
            }
        }
        return inc || dec;
    }
    
    private long solve(long n, boolean[] goodSum) {
        if (n <= 0) {
            return 0;
        }
        String num = Long.toString(n);
        Long[][][] memo = new Long[20][150][2];
        return dp(num, 0, 0, 0, memo, goodSum);
    }
    
    private long dp(String num, int idx, int sum, int isLess, Long[][][] memo, boolean[] goodSum) {
        if (idx == num.length()) {
            return goodSum[sum] ? 1 : 0;
        }
        if (memo[idx][sum][isLess] != null) {
            return memo[idx][sum][isLess];
        }
        
        long res = 0;
        int limit = isLess == 1 ? 9 : num.charAt(idx) - '0';
        for (int d = 0; d <= limit; d++) {
            int nextIsLess = isLess == 1 || d < limit ? 1 : 0;
            res += dp(num, idx + 1, sum + d, nextIsLess, memo, goodSum);
        }
        return memo[idx][sum][isLess] = res;
    }
}