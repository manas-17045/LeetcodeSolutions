# Leetcode 992: Subarrays with K Different Integers
# https://leetcode.com/problems/subarrays-with-k-different-integers/
# Solved on 8th of August, 2025
import collections


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        Calculates the number of subarrays with exactly K distinct integers.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The exact number of distinct integers required.

        Returns:
            int: The total number of subarrays with exactly k distinct integers.
        """
        def atMostK(limit: int) -> int:
            count = 0
            left = 0
            freqMap = collections.defaultdict(int)

            for right in range(len(nums)):
                freqMap[nums[right]] += 1

                while len(freqMap) > limit:
                    leftNum = nums[left]
                    freqMap[leftNum] -= 1
                    if freqMap[leftNum] == 0:
                        del freqMap[leftNum]
                    left += 1

                count += right - left + 1

            return count

        return atMostK(k) - atMostK(k - 1)