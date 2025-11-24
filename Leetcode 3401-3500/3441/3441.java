// Leetcode 3441: Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/
// Solved on 24th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum cost good caption for a given input caption.
     * @param caption The input caption string.
     * @return The minimum cost good caption, or an empty string if no good caption can be formed.
     */
    public String minCostGoodCaption(String caption) {
        int n = caption.length();
        if (n < 3) {
            return "";
        }

        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[n] = 0;

        int[] bestLen = new int[n];
        int[] bestChar = new int[n];
        
        int[] firstChar = new int[n + 1];
        int[] runLength = new int[n + 1];
        int[] secondChar = new int[n + 1];
        
        firstChar[n] = -1; 
        runLength[n] = 0;
        secondChar[n] = 26;

        for (int i = n - 1; i >= 0; i--) {
            int iBestLen = -1;
            int iBestChar = -1;
            int iBestRun = -1;
            int iBestSecond = -1;
            int iMinCost = Integer.MAX_VALUE;

            for (int c = 0; c < 26; c++) {
                for (int len = 3; len <= 5; len++) {
                    if (i + len > n) {
                        continue;
                    }
                    if (dp[i + len] == Integer.MAX_VALUE) {
                        continue;
                    }

                    int cost = 0;
                    for (int k = 0; k < len; k++) {
                        cost += Math.abs(caption.charAt(i + k) - ('a' + c));
                    }

                    int totalCost = cost + dp[i + len];
                    
                    if (totalCost > iMinCost) {
                        continue;
                    }

                    int j = i + len;
                    int candRun = len;
                    int candSecond = 26;
                    
                    if (j < n) {
                        if (firstChar[j] == c) {
                            candRun += runLength[j];
                            candSecond = secondChar[j];
                        } else {
                            candSecond = firstChar[j];
                        }
                    }
                    
                    if (totalCost < iMinCost) {
                        iMinCost = totalCost;
                        iBestLen = len;
                        iBestChar = c;
                        iBestRun = candRun;
                        iBestSecond = candSecond;
                    } else if (totalCost == iMinCost) {
                        if (c > iBestChar) {
                            continue;
                        }
                        
                        if (candRun == iBestRun) {
                            continue;
                        }
                        
                        int minR = Math.min(candRun, iBestRun);
                        int candValAtDiff = (candRun == minR) ? candSecond : c;
                        int bestValAtDiff = (iBestRun == minR) ? iBestSecond : c;
                        
                        if (candValAtDiff < bestValAtDiff) {
                            iBestLen = len;
                            iBestChar = c;
                            iBestRun = candRun;
                            iBestSecond = candSecond;
                        }
                    }
                }
            }
            
            dp[i] = iMinCost;
            if (iMinCost != Integer.MAX_VALUE) {
                bestLen[i] = iBestLen;
                bestChar[i] = iBestChar;
                firstChar[i] = iBestChar;
                runLength[i] = iBestRun;
                secondChar[i] = iBestSecond;
            }
        }

        if (dp[0] == Integer.MAX_VALUE) {
            return "";
        }

        StringBuilder sb = new StringBuilder();
        int idx = 0;
        while (idx < n) {
            int len = bestLen[idx];
            int c = bestChar[idx];
            for (int k = 0; k < len; k++) {
                sb.append((char) ('a' + c));
            }
            idx += len;
        }
        return sb.toString();
    }
}