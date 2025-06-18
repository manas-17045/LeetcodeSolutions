# Leetcode 2966: Divide array Into Arrays With Max Difference
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
# Solved on 18th of June, 2025

class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """
        Divides the input array `nums` into subarrays of size 3 such that the difference
        between the maximum and minimum elements in each subarray is at most `k`.

        Args:
            nums: A list of integers.
            k: An integer representing the maximum allowed difference within each subarray.

        Returns:
            A list of lists, where each inner list is a subarray of size 3 satisfying the condition.
            Returns an empty list if it's not possible to divide the array according to the condition.
        """
        size = len(nums)
        nums.sort()

        resultArray = []

        for i in range(0, size, 3):
            if nums[i + 2] - nums[i] > k:
                return []

            resultArray.append(nums[i:(i + 3)])

        return resultArray