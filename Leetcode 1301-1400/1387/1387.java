// Leetcode 1387: Sort Integers by The Value
// https://leetcode.com/problems/sort-integers-by-the-value/
// Solved on 22nd of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Finds the k-th integer in a given range [lo, hi] when sorted by their power value.
     * The power value of an integer x is the number of steps required to transform x into 1 using the Collatz conjecture rules.
     * @param lo The lower bound of the range (inclusive).
     * @param hi The upper bound of the range (inclusive).
     * @param k The k-th smallest element to find.
     * @return The k-th integer sorted by power value.
     */
    public int getKth(int lo, int hi, int k) {
        int[] arr = new int[hi - lo + 1];
        for (int i = 0; i < arr.length; i++) {
            int num = lo + i;
            arr[i] = (getPower(num) << 10) | num;
        }
        Arrays.sort(arr);
        return arr[k - 1] & 1023;
    }

    private int getPower(int num) {
        int steps = 0;
        while (num != 1) {
            if ((num & 1) == 0) {
                num >>= 1;
            } else {
                num = 3 * num + 1;
            }
            steps++;
        }
        return steps;
    }
}