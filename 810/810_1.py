# Leetcode 810: Chalkboard XOR Game
# https://leetcode.com/problems/chalkboard-xor-game/
# Solved on 25th of July, 2025
class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        """
        Determines if the first player can win the Chalkboard XOR Game.

        :param nums: A list of integers representing the numbers on the chalkboard.
        :return: True if the first player can win, False otherwise.
        """
        xorSum = 0
        for currentNum in nums:
            xorSum ^= currentNum

        numCount = len(nums)
        return xorSum == 0 or numCount % 2 == 0