# Leetcode 992: Subarrays with K Different Integers
# https://leetcode.com/problems/subarrays-with-k-different-integers/
# Solved on 8th of August, 2025
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        Calculates the number of subarrays with exactly k distinct integers.

        This problem can be solved by using the principle of inclusion-exclusion.
        The number of subarrays with exactly k distinct integers is equal to
        (number of subarrays with at most k distinct integers) - (number of subarrays with at most k-1 distinct integers).

        Args:
            nums (list[int]): The input array of integers.
            k (int): The target number of distinct integers.

        Returns:
            int: The total number of subarrays with exactly k distinct integers.
        """
        def at_mostK(k_dist: int) -> int:
            if k_dist == 0:
                return 0
            count = defaultdict(int)
            left = 0
            res = 0
            distinct = 0
            for right, val in enumerate(nums):
                if count[val] == 0:
                    distinct += 1
                count[val] += 1

                while distinct > k_dist:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                # All subarrays ending at right with start in [left...right]
                res += right - left + 1
            return res

        return at_mostK(k) - at_mostK(k - 1)