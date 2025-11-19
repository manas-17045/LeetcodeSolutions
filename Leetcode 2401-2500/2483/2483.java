// Leetcode 2483: Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/
// Solved on 19th of November, 2025
class Solution {
    /**
     * Calculates the best closing time for a shop to minimize penalty.
     * @param customers A string representing customer visits for each hour. 'Y' means a customer visited, 'N' means no customer.
     * @return The earliest closing hour that results in the minimum penalty.
     */
    public int bestClosingTime(String customers) {
        int currentScore = 0;
        int maxScore = 0;
        int bestTime = 0;

        for (int i = 0; i < customers.length(); i++) {
            if (customers.charAt(i) == 'Y') {
                currentScore++;
            } else {
                currentScore--;
            }

            if (currentScore > maxScore) {
                maxScore = currentScore;
                bestTime = i + 1;
            }
        }

        return bestTime;
    }
}