# Leetcode 3576: Transform Array to All Equal Elements
# https://leetcode.com/problems/transform-array-to-all-equal-elements/
# Solved on 17th of October, 2025
class Solution:
    def canMakeEqual(self, nums: list[int], k: int) -> bool:
        """
        Determines if an array can be transformed into an array of all equal elements (either 1 or -1)
        within a given number of operations.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The maximum number of operations allowed.

        Returns:
            bool: True if the array can be transformed, False otherwise.
        """
        n = len(nums)

        def checkTarget(targetVal):
            tempList = list(nums)
            opsCount = 0

            for i in range(n - 1):
                if tempList[i] != targetVal:
                    opsCount += 1
                    tempList[i + 1] = -tempList[i + 1]

            if tempList[n - 1] == targetVal:
                return opsCount <= k

            return False

        if checkTarget(1):
            return True

        if checkTarget(-1):
            return True

        return False