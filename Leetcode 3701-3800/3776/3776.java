// Leetcode 3776: Minimum Moves to Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/
// Solved on 25th of December, 2025
class Solution {
    /**
     * Calculates the minimum moves to balance a circular array.
     * @param balance An array of integers representing the balance at each position.
     * @return A long integer representing the minimum number of moves, or -1 if it's impossible to balance.
     */
    public long minMoves(int[] balance) {
        long totalSum = 0;
        int negativeIndex = -1;
        int n = balance.length;

        for (int i = 0; i < n; i++) {
            totalSum += balance[i];
            if (balance[i] < 0) {
                negativeIndex = i;
            }
        }

        if (totalSum < 0) {
            return -1;
        }

        if (negativeIndex == -1) {
            return 0;
        }

        long deficit = -1L * balance[negativeIndex];
        long moves = 0;
        long[] supplies = new long[n / 2 + 1];

        for (int i = 0; i < n; i++) {
            if (balance[i] > 0) {
                int distance = Math.abs(i - negativeIndex);
                distance = Math.min(distance, n - distance);
                supplies[distance] += balance[i];
            }
        }

        for (int dist = 1; dist < supplies.length; dist++) {
            if (supplies[dist] > 0) {
                long take = Math.min(deficit, supplies[dist]);
                moves += take * dist;
                deficit -= take;
                if (deficit == 0) {
                    break;
                }
            }
        }

        return moves;
    }
}