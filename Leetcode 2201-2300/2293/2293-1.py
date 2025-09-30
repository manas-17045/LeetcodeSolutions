# Leetcode 2293: Min Max Game
# https://leetcode.com/problems/min-max-game/
# Solved on 30th of September, 2025
class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        """
        Applies a min-max game to a list of numbers until only one number remains.

        :param nums: A list of integers.
        :return: The single integer remaining after the min-max game.
        """
        currentLength = len(nums)

        while currentLength > 1:
            currentLength //= 2
            for i in range(currentLength):
                val1 = nums[2 * i]
                val2 = nums[2 * i + 1]
                if i % 2 == 0:
                    nums[i] = min(val1, val2)
                else:
                    nums[i] = max(val1, val2)

        return nums[0]