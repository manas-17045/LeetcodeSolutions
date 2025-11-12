# Leetcode 2274: Maximum Consecutive Floors Without Special Floors
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
# Solved on 12th of November, 2025
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        """
        Calculates the maximum number of consecutive floors without any special floors.

        Args:
            bottom (int): The lowest floor number.
            top (int): The highest floor number.
            special (list[int]): A list of special floor numbers.
        Returns:
            int: The maximum number of consecutive floors without special floors.
        """
        special.sort()

        maxFound = 0

        maxFound = max(maxFound, (special[0] - bottom))

        for i in range(1, len(special)):
            currentGap = special[i] - special[i - 1] - 1
            maxFound = max(maxFound, currentGap)

        maxFound = max(maxFound, (top - special[-1]))

        return maxFound