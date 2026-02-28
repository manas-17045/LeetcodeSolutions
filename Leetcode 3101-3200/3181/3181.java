// Leetcode 3181: Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/
// Solved on 28th of February, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum total reward that can be obtained using the given reward values.
     * 
     * @param rewardValues An array of integers representing the available rewards.
     * @return The maximum total reward possible.
     */
    public int maxTotalReward(int[] rewardValues) {
        Arrays.sort(rewardValues);
        int maxValue = rewardValues[rewardValues.length - 1];
        long[] dpArray = new long[(maxValue * 2) / 64 + 2];
        dpArray[0] = 1L;
        int lastValue = -1;
        for (int value : rewardValues) {
            if (value == lastValue) {
                continue;
            }
            lastValue = value;
            int limitWord = value / 64;
            int shiftWords = value / 64;
            int shiftBits = value % 64;
            long mask = (1L << shiftBits) - 1L;
            for (int i = 0; i <= limitWord; i++) {
                long currentBits = dpArray[i];
                if (i == limitWord) {
                    currentBits &= mask;
                }
                if (currentBits == 0L) {
                    continue;
                }
                dpArray[i + shiftWords] |= (currentBits << shiftBits);
                if (shiftBits > 0) {
                    dpArray[i + shiftWords + 1] |= (currentBits >>> (64 - shiftBits));
                }
            }
        }
        for (int i = dpArray.length - 1; i >= 0; i--) {
            if (dpArray[i] != 0L) {
                return i * 64 + 63 - Long.numberOfLeadingZeros(dpArray[i]);
            }
        }
        return 0;
    }
}