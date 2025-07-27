# Leetcode 2210: Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
# Solved on 27th of July, 2025
class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        """
        Counts the number of hills and valleys in an array.

        Args:
            nums: A list of integers.
        Returns:
            The number of hills and valleys.
        """

        condensedNums = []
        if nums:
            condensedNums.append(nums[0])
            for i in range(1, len(nums)):
                if nums[i] != condensedNums[-1]:
                    condensedNums.append(nums[i])

        if len(condensedNums) < 3:
            return 0

        count = 0
        for i in range(1, len(condensedNums) - 1):
            leftNeighbor = condensedNums[i - 1]
            currentNum = condensedNums[i]
            rightNeighbor = condensedNums[i + 1]

            isHill = (leftNeighbor < currentNum and currentNum > rightNeighbor)
            isValley = (leftNeighbor > currentNum and currentNum < rightNeighbor)

            if isHill or isValley:
                count += 1

        return count