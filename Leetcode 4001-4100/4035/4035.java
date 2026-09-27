// Leetcode 4035: Maximum Valid Split Positions I
// https://leetcode.com/problems/maximum-valid-split-positions-i/
// Solved on 27th of September, 2026
class Solution {
    /**
     * Calculates the maximum number of valid split positions achievable
     * by removing at most one element from the given array.
     *
     * @param nums the array of integers
     * @return the maximum possible score of valid split positions
     */
    public int maxvalidSplits(int[] nums) {
        int n = nums.length;
        if (n < 2) {
            return 0;
        }

        int[] prefixGcd = new int[n];
        int[] suffixGcd = new int[n];

        int maxScore = evaluateScore(nums, -1, prefixGcd, suffixGcd);

        for (int skipIndex = 0; skipIndex < n; skipIndex++) {
            int currentScore = evaluateScore(nums, skipIndex, prefixGcd, suffixGcd);
            if (currentScore > maxScore) {
                maxScore = currentScore;
            }
        }

        return maxScore;
    }

    private int evaluateScore(int[] nums, int skipIndex, int[] prefixGcd, int[] suffixGcd) {
        int n = nums.length;
        int m = (skipIndex == -1) ? n : n - 1;
        if (m < 2) {
            return 0;
        }

        for (int i = 0; i < m; i++) {
            int actualIndex = (skipIndex != -1 && i >= skipIndex) ? i + 1 : i;
            if (i == 0) {
                prefixGcd[i] = nums[actualIndex];
            } else {
                prefixGcd[i] = gcd(prefixGcd[i - 1], nums[actualIndex]);
            }
        }

        for (int i = m - 1; i >= 0; i--) {
            int actualIndex = (skipIndex != -1 && i >= skipIndex) ? i + 1 : i;
            if (i == m - 1) {
                suffixGcd[i] = nums[actualIndex];
            } else {
                suffixGcd[i] = gcd(suffixGcd[i + 1], nums[actualIndex]);
            }
        }

        int validSplits = 0;
        for (int i = 0; i < m - 1; i++) {
            if (prefixGcd[i] == suffixGcd[i + 1]) {
                validSplits++;
            }
        }

        return validSplits;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }
}