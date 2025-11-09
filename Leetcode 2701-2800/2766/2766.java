// Leetcode 2766: Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/
// Solved on 9th of November, 2025
import java.util.*;

class Solution {
    /**
     * Relocates marbles based on a series of move operations.
     *
     * @param nums An array representing the initial positions of marbles.
     * @param moveFrom An array where `moveFrom[i]` is the original position of a marble to be moved.
     * @param moveTo An array where `moveTo[i]` is the new position for the marble moved from `moveFrom[i]`.
     * @return A sorted list of the final unique positions of all marbles.
     */
    public List<Integer> relocateMarbles(int[] nums, int[] moveFrom, int[] moveTo) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);
        for (int i = 0; i < moveFrom.length; i++) {
            int from = moveFrom[i];
            int to = moveTo[i];
            if (from == to) continue;
            if (set.contains(from)) {
                set.remove(from);
                set.add(to);
            }
        }
        ArrayList<Integer> res = new ArrayList<>(set);
        Collections.sort(res);
        return res;
    }
}