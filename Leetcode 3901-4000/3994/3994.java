// Leetcode 3994: Minimum Adjacent Swaps to Partition Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/
// Solved on 15th of August, 2026
class Solution {
    /**
     * Calculates the minimum number of adjacent swaps required to partition the array.
     * 
     * @param nums The array to partition.
     * @param a    The lower bound of the middle partition.
     * @param b    The upper bound of the middle partition.
     * @return The minimum number of adjacent swaps required to partition the array.
     */
    public int minAdjacentSwaps(int[] nums, int a, int b) {
        long totalSwaps = 0;
        int countMiddle = 0;
        int countGreater = 0;
        long modulo = 1000000007L;

        for (int num : nums) {
            if (num < a) {
                totalSwaps = (totalSwaps + countMiddle + countGreater) % modulo;
            } else if (num <= b) {
                countMiddle++;
                totalSwaps = (totalSwaps + countGreater) % modulo;
            } else {
                countGreater++;
            }
        }

        return (int) (totalSwaps % modulo);
    }
}