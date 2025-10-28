# Leetcode 1673: Find the Most Competitive Subsequence
# https://leetcode.com/problems/find-the-most-competitive-subsequence/
# Solved on 28th of October, 2025
class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        """
        Finds the most competitive subsequence of length k from the given array nums.
        A subsequence is considered more competitive if its first element is smaller,
        or if the first elements are equal, then its second element is smaller, and so on.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The desired length of the competitive subsequence.
        Returns:
            list[int]: The most competitive subsequence of length k.
        """
        stack = []
        n = len(nums)
        removalsAllowed = n - k

        for num in nums:
            while stack and num < stack[-1] and removalsAllowed > 0:
                stack.pop()
                removalsAllowed -= 1
            stack.append(num)

        return stack[:k]