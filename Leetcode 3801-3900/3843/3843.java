// Leetcode 3843: Forst Element with Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/
// Solved on 18th of February, 2026
class Solution {
    /**
     * Finds the first element in the array that has a unique frequency.
     *
     * @param nums An array of integers.
     * @return The first integer in the array whose frequency is unique, or -1 if none exist.
     */
    public int firstUniqueFreq(int[] nums) {
        int[] count = new int[100001];
        for (int num : nums) {
            count[num]++;
        }

        int[] freqCount = new int[100001];
        for (int i = 0; i < count.length; i++) {
            if (count[i] > 0) {
                freqCount[count[i]]++;
            }
        }

        for (int num : nums) {
            if (freqCount[count[num]] == 1) {
                return num;
            }
        }

        return -1;
    }
}