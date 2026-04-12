// Leetcode 3890: Integers With Multiple Sum of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/
// Solved on 12th of April, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Finds all integers up to n that can be expressed as the sum of two cubes in at least two different ways.
     *
     * @param n The upper bound (inclusive) for the integers to check.
     * @return A list of integers that satisfy the condition, sorted in ascending order.
     */
    public List<Integer> findGoodIntegers(int n) {
        int[] sums = new int[500500];
        int size = 0;
        
        for (int a = 1; ; a++) {
            long aCubed = (long) a * a * a;
            if (aCubed * 2 > n) {
                break;
            }
            for (int b = a; ; b++) {
                long sum = aCubed + (long) b * b * b;
                if (sum > n) {
                    break;
                }
                sums[size++] = (int) sum;
            }
        }
        
        Arrays.sort(sums, 0, size);
        
        List<Integer> result = new ArrayList<>();
        int lastAdded = -1;
        
        for (int i = 1; i < size; i++) {
            if (sums[i] == sums[i - 1]) {
                if (sums[i] != lastAdded) {
                    result.add(sums[i]);
                    lastAdded = sums[i];
                }
            }
        }
        
        return result;
    }
}