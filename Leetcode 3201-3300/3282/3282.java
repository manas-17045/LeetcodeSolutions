// Leetcode 3282: Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/
// Solved on 2nd of January, 2026
class Solution {
    /**
     * Calculates the maximum score achievable by reaching the end of the array.
     * The score is accumulated by adding the maximum element encountered so far up to the current index (exclusive of the last element).
     * @param nums A list of integers representing the array.
     * @return The maximum score.
     */
    public long findMaximumScore(List<Integer> nums) {
        long ans = 0;
        int max = 0;
        int n = nums.size();

        for (int i = 0; i < n - 1; i++) {
            if (nums.get(i) > max) {
                max = nums.get(i);
            }
            ans += max;
        }
        return ans;
    }
}