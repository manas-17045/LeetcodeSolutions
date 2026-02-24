// Leetcode 3847: Find the Score Difference in a Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/
// Solved on 23rd of February, 2026
class Solution {
    public int scoreDifference(int[] nums) {
        int difference = 0;
        boolean isPlayerOne = true;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 != 0) {
                isPlayerOne = !isPlayerOne;
            }
            if ((i + 1) % 6 == 0) {
                isPlayerOne = !isPlayerOne;
            }
            if (isPlayerOne) {
                difference += nums[i];
            } else {
                difference -= nums[i];
            }
        }
        return difference;
    }
}