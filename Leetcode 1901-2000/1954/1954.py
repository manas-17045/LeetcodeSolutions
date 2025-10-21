# Leetcode 1954: Minimum Garden Perimeter to Collect Enough Apples
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
# Solved on 21st of October, 2025
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        """
        Calculates the minimum perimeter of a square garden required to collect at least `neededApples`.

        Args:
            neededApples (int): The minimum number of apples to collect.
        Returns:
            int: The minimum perimeter of the garden.
        """
        left = 1
        right = 100000
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            totalApples = 2 * mid * (mid + 1) * (2 * mid + 1)

            if totalApples >= neededApples:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans * 8