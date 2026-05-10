// Leetcode 3917: Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/
// Solved on 10th of May, 2026
class Solution {
    /**
     * Counts the number of indices to the right of each element that have an opposite parity.
     *
     * @param nums An array of integers.
     * @return An array where each element at index i is the count of indices j > i such that nums[i] and nums[j] have different parity.
     */
    public int[] countOppositeParity(int[] parity) {
        int n = nums.length;
        int[] answer = new int[n];
        int evenCount = 0;
        int oddCount = 0;

        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] % 2 == 0) {
                answer[i] = oddCount;
                evenCount++;
            } else {
                answer[i] = evenCount;
                oddCount++;
            }
        }

        return answer;
    }
}