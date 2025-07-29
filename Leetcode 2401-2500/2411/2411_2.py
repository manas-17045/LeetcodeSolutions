# Leetcode 2411: Smallest Subarrays With Maximum Bitwise OR
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
# Solved on 29th of July, 2025
class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        """
        Finds the length of the smallest subarray starting at each index i such that the bitwise OR of all elements in the subarray is maximized.
        :param nums: A list of integers.
        :return: A list of integers, where ans[i] is the length of the smallest subarray starting at index i.
        """
        n = len(nums)
        next_pos = [n] * 32
        ans = [1] * n

        # Scan from right to left
        for i in range(n - 1, -1, -1):
            x = nums[i]
            # Update next_pos for bits set in x
            for b in range(32):
                if (x >> b) & 1:
                    next_pos[b] = i

            # Compute how far we need to go to pick up all the bits
            longest = 1
            for b in range(32):
                if next_pos[b] < n:
                    length = next_pos[b] - i + 1
                    if length > longest:
                        longest = length

            ans[i] = longest

        return ans