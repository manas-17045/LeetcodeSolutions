// Leetcode 3645: Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/
// Solved on 29th of December, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Calculates the maximum total score from an optimal activation order.
     * @param value An array of integers representing the value of each item.
     * @param limit An array of integers representing the activation limit for each item.
     * @return The maximum total score achievable.
     */
    public long maxTotal(int[] value, int[] limit) {
        int n = value.length;
        List<Integer>[] groups = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            groups[i] = new ArrayList<>();
        }

        for (int i = 0; i < n; i++) {
            groups[limit[i]].add(value[i]);
        }

        long totalScore = 0;
        for (int i = 1; i <= n; i++) {
            List<Integer> list = groups[i];
            if (list.isEmpty()) {
                continue;
            }
            list.sort((a, b) -> b - a);
            int count = 0;
            for (int val : list) {
                if (count == i) {
                    break;
                }
                totalScore += val;
                count++;
            }
        }
        return totalScore;
    }
}