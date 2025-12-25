// Leetcode 3780: Maximum Sum of Three Numbers Divisible by Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/
// Solved on 25th of December, 2025
class Solution {
    /**
     * Calculates the maximum sum of three numbers from the input array that is divisible by three.
     * @param nums An array of integers.
     * @return An integer representing the maximum possible sum.
     */
    public int maximumSum(int[] nums) {
        int[] zero = new int[3];
        int[] one = new int[3];
        int[] two = new int[3];

        for (int num : nums) {
            if (num % 3 == 0) {
                update(zero, num);
            } else if (num % 3 == 1) {
                update(one, num);
            } else {
                update(two, num);
            }
        }

        int maxVal = 0;

        if (zero[2] != 0) {
            maxVal = Math.max(maxVal, zero[0] + zero[1] + zero[2]);
        }
        if (one[2] != 0) {
            maxVal = Math.max(maxVal, one[0] + one[1] + one[2]);
        }
        if (two[2] != 0) {
            maxVal = Math.max(maxVal, two[0] + two[1] + two[2]);
        }
        if (zero[0] != 0 && one[0] != 0 && two[0] != 0) {
            maxVal = Math.max(maxVal, zero[0] + one[0] + two[0]);
        }

        return maxVal;
    }

    private void update(int[] bucket, int num) {
        if (num > bucket[0]) {
            bucket[2] = bucket[1];
            bucket[1] = bucket[0];
            bucket[0] = num;
        } else if (num > bucket[1]) {
            bucket[2] = bucket[1];
            bucket[1] = num;
        } else if (num > bucket[2]) {
            bucket[2] = num;
        }
    }
}