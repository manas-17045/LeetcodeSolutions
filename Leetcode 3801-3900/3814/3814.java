// Leetcode 3814: Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/
// Solved on 22nd of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum total capacity of at most two machines that can be
     * purchased within the given budget.
     * @param costs An array of integers representing the cost of each machine.
     * @param capacity An array of integers representing the capacity of each machine.
     * @param budget An integer representing the maximum budget.
     * @return The maximum total capacity within the budget.
     */
    public int maxCapacity(int[] costs, int[] capacity, int budget) {
        int n = costs.length;
        int[][] machines = new int[n][2];

        for (int i = 0; i < n; i++) {
            machines[i][0] = costs[i];
            machines[i][1] = capacity[i];
        }

        Arrays.sort(machines, (a, b) -> Integer.compare(a[0], b[0]));

        int[] maxCap = new int[n];
        maxCap[0] = machines[0][1];
        for (int i = 1; i < n; i++) {
            maxCap[i] = Math.max(maxCap[i - 1], machines[i][1]);
        }

        long maxTotalCapacity = 0;

        for (int i = 0; i < n; i++) {
            int currentCost = machines[i][0];
            int currentCap = machines[i][1];

            if (currentCost >= budget) {
                continue;
            }

            maxTotalCapacity = Math.max(maxTotalCapacity, currentCap);

            int target = budget - currentCost;

            int l = 0, r = i - 1;
            int bestIdx = -1;

            while (l <= r) {
                int mid = l + (r - l) / 2;
                if (machines[mid][0] < target) {
                    bestIdx = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }

            if (bestIdx != -1) {
                maxTotalCapacity = Math.max(maxTotalCapacity, (long) currentCap + maxCap[bestIdx]);
            }
        }

        return (int) maxTotalCapacity;
    }
}