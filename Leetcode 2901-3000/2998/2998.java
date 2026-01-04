// Leetcode 2998: Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to make x equal to y.
     * @param x The starting integer.
     * @param y The target integer.
     * @return The minimum number of operations.
     */
    public int minimumOperationsToMakeEqual(int x, int y) {
        if (x <= y) {
            return y - x;
        }
        int[] memo = new int[x + 1];
        return calculate(x, y, memo);
    }

    private int calculate(int x, int y, int[] memo) {
        if (x <= y) {
            return y - x;
        }
        if (memo[x] != 0) {
            return memo[x];
        }

        int result = x - y;

        int distToNextDiv11 = 11 - (x % 11);
        int opsDiv11 = Math.min(x % 11, distToNextDiv11);
        int nextVal11 = (x % 11 == 0) ? x / 11 : (x % 11 < distToNextDiv11 ? x / 11 : x / 11 + 1);
        
        result = Math.min(result, x % 11 + 1 + calculate(x / 11, y, memo));
        result = Math.min(result, (11 - x % 11) + 1 + calculate(x / 11 + 1, y, memo));

        result = Math.min(result, x % 5 + 1 + calculate(x / 5, y, memo));
        result = Math.min(result, (5 - x % 5) + 1 + calculate(x / 5 + 1, y, memo));

        memo[x] = result;
        return result;
    }
}