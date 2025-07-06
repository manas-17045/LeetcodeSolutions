# Leetcode 3209: Number of Subarrays With AND Value of K
# https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/
# Solved on 6th of July, 2025
from collections import Counter


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of subarrays in `nums` whose bitwise AND sum equals `k`.

        Args:
            nums: A list of integers.
            k: The target bitwise AND sum.

        Returns:
            The total count of such subarrays.
        """

        totalCount = 0
        prevAnds = Counter()

        for num in nums:
            currentAnds = Counter()
            if (num & k) == k:
                currentAnds[num] += 1
                for val, count in prevAnds.items():
                    currentAnds[val & num] += count

            totalCount += currentAnds[k]
            prevAnds = currentAnds

        return totalCount