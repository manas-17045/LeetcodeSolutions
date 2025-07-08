# Leetcode 798: Smallest Rotation with Highest Score
# https://leetcode.com/problems/smallest-rotation-with-highest-score/
# Solved on 8th of July, 2025
class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        """
        Finds the smallest rotation index k that maximizes the score.

        The score is calculated by counting how many elements nums[i] satisfy nums[i] <= i
        after rotating the array by k positions.

        Args:
            nums: A list of integers.
        Returns:
            The smallest rotation index k that yields the highest score.
        """
        n = len(nums)
        change = [0] * (n + 1)

        for i, num in enumerate(nums):
            low = (i - num + 1 + n) % n
            high = i

            if low <= high:
                change[low] += 1
                change[high + 1] -= 1
            else:
                change[0] += 1
                change[high + 1] -= 1
                change[low] += 1

        minLost = n + 1
        bestRotationIIndex = 0
        lostPoints = 0

        for k in range(n):
            lostPoints += change[k]
            if lostPoints < minLost:
                minLost = lostPoints
                bestRotationIIndex = k

        return bestRotationIIndex