// Leetcode 2162: Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/
// Solved on 22nd of November, 2025
class Solution {
    /**
     * Calculates the minimum cost to set a cooking time on a digital timer.
     * @param startAt The digit the timer is currently at.
     * @param moveCost The cost to move to an adjacent digit.
     * @param pushCost The cost to push a digit button.
     * @param targetSeconds The target cooking time in seconds.
     * @return The minimum cost to set the target cooking time.
     */
    public int minCostTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        int minCost = Integer.MAX_VALUE;
        int minutes = targetSeconds / 60;
        int seconds = targetSeconds % 60;

        if (minutes <= 99) {
            minCost = Math.min(minCost, calculateCost(startAt, moveCost, pushCost, minutes, seconds));
        }

        if (minutes - 1 >= 0 && seconds + 60 <= 99) {
            minCost = Math.min(minCost, calculateCost(startAt, moveCost, pushCost, minutes - 1, seconds + 60));
        }

        return minCost;
    }

    private int calculateCost(int startAt, int moveCost, int pushCost, int minutes, int seconds) {
        int number = minutes * 100 + seconds;
        String text = String.valueOf(number);
        int current = startAt;
        int cost = 0;

        for (int i = 0; i < text.length(); i++) {
            int next = text.charAt(i) - '0';
            if (next != current) {
                cost += moveCost;
                current = next;
            }
            cost += pushCost;
        }
        return cost;
    }
}