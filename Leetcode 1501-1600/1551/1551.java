// Leetcode 1551: Minimum Operations to Make Array Equal
// https://leetcode.com/problems/minimum-operations-to-make-array-equal/
// Solved on 27th of November, 2025
class Solution {
    public int minOperations(int n) {
    /**
     * Calculates the minimum number of operations to make all elements of an array equal.
     * The array is defined as arr[i] = (2 * i) + 1 for all valid i.
     * An operation consists of choosing two indices x and y (0 <= x, y < n) and performing arr[x] -= 1 and arr[y] += 1.
     *
     * @param n The length of the array.
     * @return The minimum number of operations required.
     */
        return n * n / 4;
    }
}