# Leetcode 810: Chalkboard XOR Game
# https://leetcode.com/problems/chalkboard-xor-game/
# Solved on 25th of July, 2025
class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        """
        Determines if the first player can win the XOR game.

        :param nums: A list of integers representing the numbers on the board.
        :return: True if the first player can win, False otherwise.
        """
        total_xor = 0
        for num in nums:
            total_xor ^= num

        return total_xor == 0 or len(nums) % 2 == 0