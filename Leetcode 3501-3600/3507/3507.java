// Leetcode 3507: Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
// Solved on 22nd of January, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to sort the array by repeatedly
     * replacing the pair of adjacent elements with the minimum sum with their sum.
     * @param nums An array of integers.
     * @return The minimum number of operations to sort the array.
     */
    public int minimumPairRemovals(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nums[i];
        }

        int operations = 0;

        while (true) {
            boolean sorted = true;
            for (int i = 0; i < n - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    sorted = false;
                    break;
                }
            }

            if (sorted) {
                return operations;
            }

            int minSum = Integer.MAX_VALUE;
            int minIndex = -1;

            for (int i = 0; i < n - 1; i++) {
                int sum = arr[i] + arr[i + 1];
                if (sum < minSum) {
                    minSum = sum;
                    minIndex = i;
                }
            }

            arr[minIndex] = minSum;
            for (int i = minIndex + 1; i < n - 1; i++) {
                arr[i] = arr[i + 1];
            }
            n--;
            operations++;
        }
    }
}