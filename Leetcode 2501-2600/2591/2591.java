// Leetcode 2591: Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/
// Solved on 25th of October, 2025
class Solution{
    /**
     * Distributes `money` among `children` such that each child receives at least 1 dollar,
     * and as many children as possible receive exactly 8 dollars.
     * @param money The total amount of money to distribute.
     * @param children The number of children.
     * @return The maximum number of children who can receive exactly 8 dollars. Returns -1 if it's impossible to give each child at least 1 dollar.
     */
    public int distMoney(int money, int children) {
        if (money < children) {
            return -1;
        }

        if (money > children * 8) {
            return children - 1;
        }

        if (money == children * 8) {
            return children;
        }

        int moneyAfterOnes = money - children;
        int countEight = moneyAfterOnes / 7;
        int moneyRemaining = moneyAfterOnes % 7;
        int childrenRemnaining = children - countEight;

        if (moneyRemaining == 3 && childrenRemnaining == 1) {
            return countEight - 1;
        }

        return countEight;
    }
}