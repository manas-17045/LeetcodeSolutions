// Leetcode 3669: Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/
// Solved on 28th of December, 2025
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private int minDiff = Integer.MAX_VALUE;
    private int[] bestSplit;

    /**
     * Finds a balanced k-factor decomposition of n such that the difference between the maximum and minimum factors is minimized.
     *
     * @param n The number to decompose.
     * @param k The number of factors in the decomposition.
     * @return An array of k integers representing the factors that minimize the difference between the maximum and minimum factors.
     */
    public int[] minDifference(int n, int k) {
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                divisors.add(i);
                if (i * i != n) {
                    divisors.add(n / i);
                }
            }
        }
        Collections.sort(divisors);

        bestSplit = new int[k];
        int[] currentSplit = new int[k];
        
        backtrack(divisors, n, k, 0, 1, 0, currentSplit);
        
        return bestSplit;
    }

    private void backtrack(List<Integer> divisors, int target, int k, int startIdx, long currentProduct, int count, int[] currentSplit) {
        if (count == k) {
            if (currentProduct == target) {
                int minVal = currentSplit[0];
                int maxVal = currentSplit[0];
                for (int i = 1; i < k; i++) {
                    minVal = Math.min(minVal, currentSplit[i]);
                    maxVal = Math.max(maxVal, currentSplit[i]);
                }
                int diff = maxVal - minVal;
                if (diff < minDiff) {
                    minDiff = diff;
                    System.arraycopy(currentSplit, 0, bestSplit, 0, k);
                }
            }
            return;
        }

        for (int i = startIdx; i < divisors.size(); i++) {
            int div = divisors.get(i);
            
            if (currentProduct * div > target) {
                break;
            }

            currentSplit[count] = div;
            backtrack(divisors, target, k, i, currentProduct * div, count + 1, currentSplit);
        }
    }
}