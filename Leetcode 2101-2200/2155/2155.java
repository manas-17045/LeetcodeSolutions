// Leetcode 2155: All Divisions Wuth the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/
// Solved on 11th of November, 2025
import java.util.*;

class Solution {
    /**
     * Calculates all division indices that result in the highest score.
     * The score for a division at index `i` is the sum of zeros in the left subarray `nums[0...i-1]`
     * and ones in the right subarray `nums[i...n-1]`.
     * @param nums The input binary array.
     * @return A list of all division indices that yield the maximum score.
     */
    public List<Integer> maxScoreIndices(int[] nums) {
        int n = nums.length;
        int totalOnes = 0;
        for (int v : nums) {
            if (v == 1) totalOnes++;
        }
        List<Integer> res = new ArrayList<>();
        int zerosLeft = 0;
        int onesSeen = 0;
        int maxScore = -1;
        for (int i = 0; i <= n; i++) {
            int onesRight = totalOnes - onesSeen;
            int score = zerosLeft + onesRight;
            if (score > maxScore) {
                res.clear();
                res.add(i);
                maxScore = score;
            } else if (score == maxScore) {
                res.add(i);
            }
            if (i < n) {
                if (nums[i] == 0) {
                    zerosLeft++;
                } else {
                    onesSeen++;
                }
            }
        }
        return res;
    }
}