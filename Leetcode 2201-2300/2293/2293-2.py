# Leetcode 2293: Min Max Game
# https://leetcode.com/problems/min-max-game/
# Solved on 30th of September, 2025
class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        """
        Performs a min-max game on the given list of numbers until only one number remains.
        :param nums: A list of integers.
        :return: The single integer remaining after the min-max game.
        """
        n = len(nums)
        # Repeatedly fold array in-place until length becomes 1
        while n > 1:
            half = n // 2
            for i in range(half):
                a, b = nums[2 * i], nums[2 * i + 1]
                nums[1] = a if (i % 2 == 0 and a <= b) else (
                    b if (i % 2 == 0) else (
                        a if a >= b else b))

            n = half
        return nums[0]