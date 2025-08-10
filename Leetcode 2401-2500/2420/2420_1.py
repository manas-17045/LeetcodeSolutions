# Leetcode 2420: Find All Good Indices
# https://leetcode.com/problems/find-all-good-indices/
# Solved on 10th of August, 2025
class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        """
        Finds all "good" indices in a given list of integers.
        An index `i` is considered "good" if the `k` elements before it are non-increasing
        and the `k` elements after it are non-decreasing.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The length of the non-increasing and non-decreasing subarrays to check.
        Returns:
            list[int]: A list of all good indices.
        """
        n = len(nums)

        nonIncreasingRun = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                nonIncreasingRun[i] = nonIncreasingRun[i - 1] + 1

        nonDecreasingRun = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nonDecreasingRun[i] = nonDecreasingRun[i + 1] + 1

        result = []
        for i in range(k, n - k):
            if nonIncreasingRun[i - 1] >= k and nonDecreasingRun[i + 1] >= k:
                result.append(i)

        return result