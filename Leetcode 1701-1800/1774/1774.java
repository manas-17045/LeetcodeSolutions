// Leetcode 1774: Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/
// Solved on 5th of March, 2026
class Solution {
    int bestCost;

    /**
     * Finds the closest possible dessert cost to the target.
     * 
     * @param baseCosts    An array of costs for different base ice creams.
     * @param toppingCosts An array of costs for different toppings.
     * @param target       The target cost for the dessert.
     * @return The cost closest to the target, or the smaller cost if there is a tie.
     */
    public int closestCost(int[] bestCosts, int[] toppingCosts, int target) {
        bestCost = baseCosts[0];
        for (int baseCost : baseCosts) {
            dfs(toppingCosts, 0, baseCost, target);
        }
        return bestCost;
    }

    private void dfs(int[] toppingCosts, int index, int currentCost, int target) {
        if (Math.abs(currentCost - target) < Math.abs(bestCost - target) || 
            (Math.abs(currentCost - target) == Math.abs(bestCost - target) && currentCost < bestCost)) {
            bestCost = currentCost;
        }

        if (currentCost >= target && currentCost - target >= Math.abs(bestCost - target)) {
            return;
        }

        if (index == toppingCosts.length) {
            return;
        }

        dfs(toppingCosts, index + 1, currentCost, target);
        dfs(toppingCosts, index + 1, currentCost + toppingCosts[index], target);
        dfs(toppingCosts, index + 1, currentCost + toppingCosts[index] * 2, target);
    }
}