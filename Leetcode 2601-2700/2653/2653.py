# Leetcode 2653: Sliding Subarray Beauty
# https://leetcode.com/problems/sliding-subarray-beauty/
# Solved on 8th of November, 2025
class Solution:
    def getSubarrayBeauty(self, nums: list[int], k: int, x: int) -> list[int]:
        """
        Calculates the beauty of all subarrays of length k.

        Args:
            nums: The input list of integers.
            k: The length of the subarrays.
            x: The x-th smallest negative number to consider for beauty.
        Returns:
            A list of integers, where each element is the beauty of the corresponding subarray.
        """

        n = len(nums)
        resultArray = []
        negFrequency = [0] * 50

        def findCurrentBeauty():
            currentCount = 0
            for i in range(50):
                currentCount += negFrequency[i]
                if currentCount >= x:
                    return i - 50

            return 0

        for i in range(n):
            incomingNum = nums[i]
            if incomingNum < 0:
                negFrequency[incomingNum + 50] += 1

            if i >= k:
                outgoingNum = nums[i - k]
                if outgoingNum < 0:
                    negFrequency[outgoingNum + 50] -= 1

            if i >= k - 1:
                resultArray.append(findCurrentBeauty())

        return resultArray