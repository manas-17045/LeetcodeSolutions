# Leetcode 3847: Find the Score Difference in a Game
# https://leetcode.com/problems/find-the-score-difference-in-a-game/
# Solved on 23rd of February, 2026
class Solution:
    def coreDifference(self, nums: list[int]) -> int:

        scoreDiff = 0
        isPlayerOne = True

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                isPlayerOne = not isPlayerOne

            if i % 6 == 5:
                isPlayerOne = not isPlayerOne

            if isPlayerOne:
                scoreDiff += nums[i]
            else:
                scoreDiff -= nums[i]

        return scoreDiff