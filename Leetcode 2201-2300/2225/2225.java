// Leetcode 2225: Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/
// Solved on 10th of November, 2025
import java.util.*;

class Solution {
    /**
     * Finds players who have zero losses and players who have exactly one loss.
     *
     * @param matches A 2D array where each inner array `[winner, loser]` represents a match.
     * @return A list of two lists: the first list contains players with zero losses, and the second list contains players with one loss.
     */
    public List<List<Integer>> findWinners(int[][] matches) {
        int maxId = 0;
        for (int[] m : matches) {
            if (m[0] > maxId) {
                maxId = m[0];
            }
            if (m[1] > maxId) {
                maxId = m[1];
            }
        }
        int[] lossCount = new int[maxId + 1];
        boolean[] played = new boolean[maxId + 1];
        for (int[] m : matches) {
            int winner = m[0];
            int loser = m[1];
            played[winner] = true;
            played[loser] = true;
            lossCount[loser]++;
        }
        List<Integer> zeroList = new ArrayList<>();
        List<Integer> oneList = new ArrayList<>();
        for (int i = 1; i <= maxId; i++) {
            if (!played[i]) {
                continue;
            }
            if (lossCount[i] == 0) {
                zeroList.add(i);
            } else if (lossCount[i] == 1) {
                oneList.add(i);
            }
        }
        List<List<Integer>> result = new ArrayList<>();
        result.add(zeroList);
        result.add(oneList);
        return result;
    }
}