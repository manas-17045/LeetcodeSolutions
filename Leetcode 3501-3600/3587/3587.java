// Leetcode 3587: Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/
// Solved on 6th of November, 2025
import java.util.ArrayList;

class Solution {
    /**
     * Calculates the minimum number of adjacent swaps required to arrange the elements of an array such that their parities alternate.
     *
     * @param nums The input array of integers.
     * @return The minimum number of swaps needed, or -1 if it's impossible to achieve an alternating parity arrangement.
     */
    public int minSwaps(int[] nums) {
        int n = nums.length;
        ArrayList<Integer> evenIndices = new java.util.ArrayList<>();
        for (int i = 0; i < n; i++) {
            if ((nums[i] & 1) == 0){
                evenIndices.add(i);
            }
        }
        int ev = evenIndices.size();
        int od = n - ev;
        if (Math.abs(ev - od) > 1){
            return -1;
        }
        long best = Long.MAX_VALUE;
        if (ev >= od) {
            long sum = 0;
            for (int i = 0; i < evenIndices.size(); i++) {
                int target = 2 * i;
                sum += Math.abs(evenIndices.get(i) - target);
            }
            best = Math.min(best, sum);
        }
        if (od >= ev) {
            long sum = 0;
            for (int i = 0; i < evenIndices.size(); i++) {
                int target = 2 * i + 1;
                sum += Math.abs(evenIndices.get(i) - target);
            }
            best = Math.min(best, sum);
        }
        return (int)best;
    }
}