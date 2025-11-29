// Leetcode 2121: Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/
// Solved on 29th of November, 2025
class Solution {
    /**
     * Calculates the sum of absolute differences between the index of each element and the indices of all other identical elements.
     *
     * @param arr The input array of integers.
     * @return An array where each element result[i] is the sum of |i - j| for all j where arr[i] == arr[j] and i != j.
     */
    public long[] getDistances(int[] arr) {
        int length = arr.length;
        long[] result = new long[length];
        long[] sum = new long[100001];
        int[] count = new int[100001];

        for (int i = 0; i < length; i++) {
            int value = arr[i];
            result[i] += (long) i * count[value] - sum[value];
            sum[value] += i;
            count[value]++;
        }

        sum = new long[100001];
        count = new int[100001];

        for (int i = length - 1; i >= 0; i--) {
            int value = arr[i];
            result[i] += sum[value] - (long) i * count[value];
            sum[value] += i;
            count[value]++;
        }

        return result;
    }
}