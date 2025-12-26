// Leetcode 3752: Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/
// Solved on 25th of December, 2025
class Solution {
    /**
     * Given an integer n and a target sum, return the lexicographically smallest negated permutation of numbers from 1 to n
     * such that the sum of the elements in the permutation equals the target.
     * A negated permutation means each number from 1 to n appears exactly once, either as itself or its negation.
     * If no such permutation exists, return an empty array.
     */
    public int[] lexSmallestNegatedPerm(int n, long target) {
        long sum = (long) n * (n + 1) / 2;
        long diff = sum - target;

        if (diff < 0 || diff % 2 != 0) {
            return new int[0];
        }

        long targetNegSum = diff / 2;

        if (targetNegSum > sum) {
            return new int[0];
        }

        boolean[] isNegated = new boolean[n + 1];
        for (int i = n; i >= 1; i--) {
            if (targetNegSum >= i) {
                targetNegSum -= i;
                isNegated[i] = true;
            }
        }

        int[] result = new int[n];
        int index = 0;

        for (int i = n; i >= 1; i--) {
            if (isNegated[i]) {
                result[index++] = -i;
            }
        }

        for (int i = 1; i <= n; i++) {
            if (!isNegated[i]) {
                result[index++] = i;
            }
        }

        return result;
    }
}