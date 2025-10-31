# Leetcode 3255: Find the Power of K-Size Subarrays II
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/
# Solved on 31st of October, 2025
class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        """
        Calculates the "power" of k-size subarrays.
        :param nums: A list of integers.
        :param k: The size of the subarrays.
        :return: A list where each element represents the "power" of the corresponding k-size subarray.
        """
        numLength = len(nums)
        resultsList = [-1] * (numLength - k + 1)
        currentConsecutiveLength = 0

        for index in range(numLength):
            if index > 0 and nums[index] == nums[index - 1] + 1:
                currentConsecutiveLength += 1
            else:
                currentConsecutiveLength = 1

            resultIndex = index - k + 1

            if resultIndex >= 0:
                if currentConsecutiveLength >= k:
                    resultsList[resultIndex] = nums[index]

        return resultsList