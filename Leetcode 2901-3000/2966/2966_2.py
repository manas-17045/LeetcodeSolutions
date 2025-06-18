# Leetcode 2966: Divide array Into Arrays With Max Difference
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
# Solved on 18th of June, 2025

class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """
        Divides an array `nums` into groups of three such that the difference
        between the maximum and minimum element in each group is at most `k`.

        Args:
            nums: A list of integers.
            k: An integer representing the maximum allowed difference within a group.

        Returns:
            A list of lists, where each inner list is a group of three elements,
            or an empty list if the array cannot be divided according to the criteria.
        """
        # Sort the input array
        nums.sort()
        n = len(nums)
        ans = []

        # Try to partition into n/3 groups of size 3
        for i in range(0, n, 3):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if c - a > k:
                return []
            ans.append([a, b, c])

        return ans