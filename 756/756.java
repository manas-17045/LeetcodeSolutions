// Leetcode 756: Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/
// Solved on 29th of December, 2025
import java.util.*;

class Solution {
    /**
     * Determines if a pyramid can be formed from a given bottom row and a list of allowed transitions.
     * @param bottom The bottom row of the pyramid as a string.
     * @param allowed A list of strings representing allowed transitions. Each string is 3 characters long,
     *                where the first two characters form the base and the third character is the top.
     * @return True if a pyramid can be formed, false otherwise.
     */
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        Map<String, List<Character>> transitions = new HashMap<>();
        for (String pattern : allowed) {
            String base = pattern.substring(0, 2);
            char top = pattern.charAt(2);
            transitions.computeIfAbsent(base, k -> new ArrayList<>()).add(top);
        }
        return solve(bottom, "", transitions, new HashSet<>());
    }

    private boolean solve(String currentLayer, String nextLayer, Map<String, List<Character>> transitions, Set<String> memo) {
        if (currentLayer.length() == 1) {
            return true;
        }

        if (nextLayer.length() == currentLayer.length() - 1) {
            String state = nextLayer;
            if (memo.contains(state)) {
                return false;
            }
            boolean result = solve(nextLayer, "", transitions, memo);
            if (!result) {
                memo.add(state);
            }
            return result;
        }

        int index = nextLayer.length();
        String base = currentLayer.substring(index, index + 2);

        if (transitions.containsKey(base)) {
            for (char top : transitions.get(base)) {
                if (solve(currentLayer, nextLayer + top, transitions, memo)) {
                    return true;
                }
            }
        }

        return false;
    }
}