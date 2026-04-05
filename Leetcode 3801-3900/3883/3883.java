// Leetcode 3883: Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/
// Solved on 5th of April, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Counts the number of non-decreasing arrays where each element's digit sum matches the given array.
     *
     * @param digitSum An array of integers representing the required digit sum for each element.
     * @return The total number of valid non-decreasing arrays modulo 10^9 + 7.
     */
    public int countArrays(int[] digitSum) {
        int mod = 1000000007;
        List<List<Integer>> groups = new ArrayList<>();

        for (int i = 0; i <= 50; i++) {
            groups.add(new ArrayList<>());
        }

        for (int i = 0; i <= 5000; i++) {
            int sum = 0;
            int temp = 0;
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            groups.get(sum).add(i);
        }

        List<Integer> prevCand = groups.get(digitSum[0]);
        if (prevCand.isEmpty()) {
            return 0;
        }

        int[] dp = new int[prevCand.size()];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = 1;
        }

        for (int i = 1; i < digitSum.length; i++) {
            List<Integer> currCand = groups.get(digitSum[i]);
            if (currCand.isEmpty()) {
                return 0;
            }
            
            int[] nextDp = new int[currCand.size()];
            int prefixSum = 0;
            int ptr = 0;
            
            for (int j = 0; j < currCand.size(); j++) {
                int val = currCand.get(j);
                while (ptr < prevCand.size() && prevCand.get(ptr) <= val) {
                    prefixSum = (prefixSum + dp[ptr]) % mod;
                    ptr++;
                }
                nextDp[j] = prefixSum;
            }
            
            dp = nextDp;
            prevCand = currCand;
        }
        
        int total = 0;
        for (int val : dp) {
            total = (total + val) % mod;
        }
        
        return total;
    }
}