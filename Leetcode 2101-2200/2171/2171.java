// Leetcode 2171: Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/
// Solved on 6th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of magic beans to remove such that all remaining beans have the same count.
     * @param beans An array of integers representing the count of beans in each bag.
     * @return The minimum number of beans to remove.
     */
    public long minimumRemoval(int[] beans) {
        Arrays.sort(beans);
        
        long totalSum = 0;
        for (int bean : beans) {
            totalSum += bean;
        }
        
        long maxRemaining = 0;
        long n = beans.length;
        
        for (int i = 0; i < n; i++) {
            long currentRemaining = (long) beans[i] * (n - i);
            maxRemaining = Math.max(maxRemaining, currentRemaining);
        }
        
        return totalSum - maxRemaining;
    }
}