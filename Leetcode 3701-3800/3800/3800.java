// Leetcode 3800: Minimum Cost to Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/
// Solved on 9th of January, 2026
class Solution {
    /**
     * Calculates the minimum cost to make two binary strings equal.
     * @param s The first binary string.
     * @param t The second binary string.
     * @param flipCost The cost to flip a single bit (0 to 1 or 1 to 0).
     * @param swapCost The cost to swap a '0' in s to '1' in t with a '1' in s to '0' in t.
     * @param crossCost The cost to perform a "cross" operation, which involves flipping two bits and then swapping them.
     * @return The minimum total cost to make string s equal to string t.
     */
    public long minimumCost(String s, String t, int flipCost, int swapCost, int crossCost) {
        long countZeroOne = 0;
        long countOneZero = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) != t.charAt(i)) {
                if (s.charAt(i) == '0') {
                    countZeroOne++;
                } else {
                    countOneZero++;
                }
            }
        }

        long totalCost = 0;
        long commonPairs = Math.min(countZeroOne, countOneZero);
        totalCost += commonPairs * Math.min(swapCost, 2L * flipCost);

        long remaining = Math.abs(countZeroOne - countOneZero);
        totalCost += (remaining / 2) * Math.min((long) crossCost + swapCost, 2L * flipCost);

        if (remaining % 2 == 1) {
            totalCost += flipCost;
        }

        return totalCost;
    }
}