// Leetcode 3922: Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/
// Solved on 23rd of May, 2026
class Solution {
    /**
     * Calculates the minimum number of flips to make a binary string coherent.
     *
     * @param s The input binary string consisting of '0's and '1's.
     * @return The minimum number of flips required.
     */
    public int minFlips(String s) {
        int n = s.length();
        int countOne = 0;
        
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                countOne++;
            }
        }
        
        int costA = countOne;
        int costB = n - countOne;
        int costC = countOne > 0 ? countOne - 1 : 1;
        
        int minCost = Math.min(costA, Math.min(costB, costC));
        
        if (n >= 2) {
            int flipsEnds = (s.charAt(0) == '0' ? 1 : 0) + (s.charAt(n - 1) == '0' ? 1 : 0);
            int onesInEnds = (s.charAt(0) == '1' ? 1 : 0) + (s.charAt(n - 1) == '1' ? 1 : 0);
            int onesInMiddle = countOne - onesInEnds;
            int costD = flipsEnds + onesInMiddle;
            minCost = Math.min(minCost, costD);
        }
        
        return minCost;
    }
}