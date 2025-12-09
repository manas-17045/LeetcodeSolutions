// Leetcode 3583: Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/
// Solved on 9th ofDecember, 2025
class Solution {
    /**
     * Counts the number of special triplets (i, j, k) in the array such that nums[i] * 2 = nums[j] + nums[k].
     * The indices i, j, k must be distinct.
     *
     * @param nums The input array of integers.
     * @return The count of special triplets modulo 1000000007.
     */
    public int specialTriplets(int[] nums) {
        int mod = 1000000007;
        int maxVal = 100001;
        int[] leftFreq = new int[maxVal];
        int[] rightFreq = new int[maxVal];
        long ans = 0;

        for (int num : nums) {
            rightFreq[num]++;
        }

        for (int num : nums) {
            rightFreq[num]--;

            int target = num * 2;
            if (target < maxVal) {
                long leftCount = leftFreq[target];
                long rightCount = rightFreq[target];
                ans = (ans + leftCount * rightCount) % mod;
            }

            leftFreq[num]++;
        }

        return (int) ans;
    }
}