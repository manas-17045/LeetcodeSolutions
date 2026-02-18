// Leetcode 3842: Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/
// Solved on 18th of February, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Toggles the state of light bulbs based on the provided list of bulb indices.
     * 
     * @param bulbs A list of integers representing the indices of light bulbs to toggle.
     * @return A list of integers representing the indices of bulbs that are currently in the 'on' state.
     */
    public List<Integer> toggleLightBulbs(List<Integer> bulbs) {
        boolean[] states = new boolean[101];
        for (int bulb : bulbs) {
            states[bulb] = !states[bulb];
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= 100; i++) {
            if (states[i]) {
                result.add(i);
            }
        }
        return result;
    }
}