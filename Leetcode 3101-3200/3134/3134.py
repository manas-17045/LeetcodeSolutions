# Leetcode 3134: Find the Median of the Uniqueness Array
# https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/
# Solved on 6th of November, 2025
import collections


class Solution:
    def medianOfUniquenessArray(self, nums: list[int]) -> int:
        """
        Finds the median of the uniqueness array. The uniqueness array is formed by the number of distinct elements
        in all possible subarrays of the given array `nums`.

        :param nums: A list of integers.
        :return: The median value of the uniqueness array.
        """
        n = len(nums)
        totalSubarrays = (n * (n + 1)) // 2
        medianRank = (totalSubarrays + 1) // 2

        def countAtMostKDistinct(k: int) -> int:

            freqMap = collections.Counter()
            totalCount = 0
            left = 0

            for right in range(n):
                freqMap[nums[right]] += 1

                while len(freqMap) > k:
                    freqMap[nums[left]] -= 1
                    if freqMap[nums[left]] == 0:
                        del freqMap[nums[left]]
                    left += 1

                totalCount += (right - left + 1)

            return totalCount

        low = 1
        high = n
        ans = 1

        while low <= high:
            mid = (low + high) // 2

            if countAtMostKDistinct(mid) >= medianRank:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans