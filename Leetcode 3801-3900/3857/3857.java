// Leetcode 3857: Minimum Cost to Split into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/
// Solved on 2nd of March, 2026
class Solution {
    /**
     * Calculates the minimum cost to split a group of size n into ones.
     * @param n The initial size of the group.
     * @return The minimum total cost of splitting.
     */
    public int minCost(int n) {
        return n * (n - 1) / 2;
    }
}