// Leetcode 3574: Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/
// Solved on 6th of December, 2025
class Solution {
    /**
     * Calculates the maximum possible GCD score of a subarray.
     * @param nums The input array of integers.
     * @param k The maximum allowed cost for a subarray to be considered for double score.
     * @return The maximum GCD score.
     */
    public long maxGCDScore(int[] nums, int k) {
        int n = nums.length;
        long maxScore = 0;

        for (int i = 0; i < n; i++) {
            long currentGcd = nums[i];
            long currentCost = 1;
            
            if (currentGcd > maxScore) {
                maxScore = currentGcd;
            }
            if (currentCost <= k) {
                if (currentGcd * 2 > maxScore) {
                    maxScore = currentGcd * 2;
                }
            }

            for (int j = i + 1; j < n; j++) {
                long newGcd = gcd(currentGcd, nums[j]);
                
                if (newGcd != currentGcd) {
                    long ratio = currentGcd / newGcd;
                    if (ratio % 2 == 0) {
                        currentCost = 0;
                    }
                    currentGcd = newGcd;
                }
                
                if ((nums[j] / currentGcd) % 2 != 0) {
                    currentCost++;
                }
                
                long currentLen = j - i + 1;
                long score = currentLen * currentGcd;
                if (score > maxScore) {
                    maxScore = score;
                }
                
                if (currentCost <= k) {
                    if (score * 2 > maxScore) {
                        maxScore = score * 2;
                    }
                }
            }
        }
        return maxScore;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}