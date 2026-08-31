// Leetcode 4009: Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/
// Solved on 31st of August, 2026
class Solution {
    /**
     * Calculates the minimum possible maximum waiting time among all served cars
     * such that the number of served cars is maximized.
     *
     * @param demand an array representing the amount of fuel required by each car
     * @param fuel an array of length 2 representing the initial fuel in the two dispensers
     * @return the minimum possible maximum waiting time, or -1 if no cars can be served
     */
    public int minMaxWaitingTime(int[] demand, int[] fuel) {
        int n = demand.length;
        int[] prefixSum = new int[n + 1];
        
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + demand[i];
        }
        
        int[][][][] memo = new int[n + 1][fuel[0] + 1][21][21];
        int resultScore = solve(0, fuel[0], 0, 0, demand, fuel, prefixSum, memo);
        int cars = resultScore / 100;
        int maxWait = 50 - (resultScore % 100);
        
        if (cars == 0) {
            return -1;
        }
        
        return maxWait;
    }

    private int solve(int i, int f0, int b0, int b1, int[] demand, int[] fuel, int[] prefixSum, int[][][][] memo) {
        if (i == demand.length) {
            return 50;
        }
        if (memo[i][f0][b0][b1] != 0) {
            return memo[i][f0][b0][b1];
        }

        int f1 = fuel[1] - (prefixSum[i] - (fuel[0] - f0));
        int maxScore = 50;

        if (f0 >= demand[i]) {
            int w = b0;
            int nextF0 = f0 - demand[i];
            int nextB0 = demand[i];
            int nextB1 = Math.max(0, b1 - w);
            int res = solve(i + 1, nextF0, nextB0, nextB1, demand, fuel, prefixSum, memo);
            
            int subCars = res / 100;
            int subWait = 50 - (res % 100);
            
            int currentCars = 1 + subCars;
            int currentWait = Math.max(w, subWait);
            int currentScore = currentCars * 100 + (50 - currentWait);
            
            maxScore = Math.max(maxScore, currentScore);
        }

        if (f1 >= demand[i]) {
            int w = b1;
            int nextB1 = demand[i];
            int nextB0 = Math.max(0, b0 - w);
            int res = solve(i + 1, f0, nextB0, nextB1, demand, fuel, prefixSum, memo);
            
            int subCars = res / 100;
            int subWait = 50 - (res % 100);
            
            int currentCars = 1 + subCars;
            int currentWait = Math.max(w, subWait);
            int currentScore = currentCars * 100 + (50 - currentWait);
            
            maxScore = Math.max(maxScore, currentScore);
        }

        memo[i][f0][b0][b1] = maxScore;
        return maxScore;
    }
}