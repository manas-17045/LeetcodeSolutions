// Leetcode 1925: Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/
// Solved on 8th of December, 2025
class Solution {
    /**
     * Counts the number of "square sum triples" (a, b, c) such that a^2 + b^2 = c^2, where 1 <= a, b, c <= n.
     * @param n The upper limit for a, b, and c.
     * @return The total count of such triples.
     */
    public int countTriple(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                int sum = a * a + b * b;
                int c = (int) Math.sqrt(sum);
                if (c <= n && c * c== sum) {
                    count++;
                }
            }
        }
        return count;
    }
}