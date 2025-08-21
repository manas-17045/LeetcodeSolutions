# Leetcode 2216: Minimum Deletions to Make Array Beautiful
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
# Solved on 21st of August, 2025
class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of deletions required to make the array beautiful.
        An array is beautiful if for every even index i, nums[i] != nums[i+1].

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The minimum number of deletions.
        """
        numCount = len(nums)
        elementsKept = 0
        currentIndex = 0

        while currentIndex < numCount:
            elementsKept += 1
            pairStartIndexValue = nums[currentIndex]

            nextIndex = currentIndex + 1
            while nextIndex < numCount and nums[nextIndex] == pairStartIndexValue:
                nextIndex += 1

            if nextIndex < numCount:
                elementsKept += 1
                currentIndex = nextIndex + 1
            else:
                currentIndex = numCount

        if elementsKept % 2 != 0:
            elementsKept -= 1

        return numCount - elementsKept