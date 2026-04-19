// Leetcode 3896: Minimum Operations to Transform Array into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/
// Solved on 19th of April, 2026
class Solution {
    /**
     * Calculates the minimum operations to transform an array into an alternating prime sequence.
     * 
     * @param nums An array of integers to be transformed.
     * @return The minimum number of operations required.
     */
    public int minOperations(int[] nums) {
        int maxLimit = 100050;
        boolean[] primeFlags = new boolean[maxLimit];
        for (int i = 2; i < maxLimit; i++) {
            primeFlags[i] = true;
        }
        for (int i = 2; i * i < maxLimit; i++) {
            if (primeFlags[i]) {
                for (int j = i * i; j < maxLimit; j += i) {
                    primeFlags[j] = false;
                }
            }
        }
        int[] nextPrimeVal = new int[maxLimit];
        int currentNextPrime = 2;
        for (int i = maxLimit - 1; i >= 0; i--) {
            if (primeFlags[i]) {
                currentNextPrime = i;
                break;
            }
        }
        for (int i = maxLimit - 1; i >= 0; i--) {
            if (primeFlags[i]) {
                currentNextPrime = i;
            }
            nextPrimeVal[i] = currentNextPrime;
        }
        int totalOps = 0;
        for (int i = 0; i < nums.length; i++) {
            int currentValue = nums[i];
            if (i % 2 == 0) {
                totalOps += nextPrimeVal[currentValue] - currentValue;
            } else {
                if (primeFlags[currentValue]) {
                    if (currentValue == 2) {
                        totalOps += 2;
                    } else {
                        totalOps += 1;
                    }
                }
            }
        }
        return totalOps;
    }
}