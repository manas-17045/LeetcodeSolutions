// Leetcode 3499: Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/
// Solved on 30th of October, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Calculates the maximum number of active sections (consecutive '1's) that can be achieved after at most one trade.
     * A trade involves changing a '0' to a '1'.
     * @param s The input string consisting of '0's and '1's.
     * @return The maximum number of active sections after at most one trade.
     */
    public int maxActiveSectionsAfterTrade(String s) {
        if (s == null || s.isEmpty()) {
            return 0;
        }

        int initialOnes = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                initialOnes++;
            }
        }

        String t = '1' + s + '1';
        List<Integer> blockLengths = new ArrayList<>();
        int augN = t.length();
        int i = 0;
        while (i < augN) {
            char currentChar = t.charAt(i);
            int j = i;
            while (j < augN && t.charAt(j) == currentChar) {
                j++;
            }
            blockLengths.add(j - i);
            i = j;
        }

        int numBlocks = blockLengths.size();
        if (numBlocks < 3) {
            return initialOnes;
        }

        int maxOriginalGain = 0;
        for (int k = 1; k < numBlocks - 1; k += 2) {
            maxOriginalGain = Math.max(maxOriginalGain, blockLengths.get(k));
        }

        int maxTotal = initialOnes;

        for (int k = 2; k < numBlocks - 1; k += 2) {
            int currentLoss = blockLengths.get(k);
            int prevZeroLen = blockLengths.get(k - 1);
            int nextZeroLen = blockLengths.get(k + 1);

            int mergedZeroLen = prevZeroLen + currentLoss + nextZeroLen;
            int maxGainForThisTrade = Math.max(maxOriginalGain, mergedZeroLen);
            int currentTotal = initialOnes - currentLoss + maxGainForThisTrade;
            maxTotal = Math.max(maxTotal, currentTotal);
        }

        return maxTotal;
    }
}