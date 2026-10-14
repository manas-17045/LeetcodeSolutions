# Leetcode 4051: Count Subarrays with Distant Sums
# https://leetcode.com/problems/count-subarrays-with-distant-sums/
# Solved on 14th of October, 2026
import bisect


class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        """
        Calculates the number of distant subarrays where the absolute difference
        between the subarray sum and the goal is at least k.

        Args:
            nums (list[int]): An array of integers representing the input sequence.
            goal (int): The target sum to compare against.
            k (int): The minimum absolute difference required to be considered distant.

        Returns:
            int: The total count of valid distant subarrays.
        """
        if k == 0:
            n = len(nums)
            return (n * (n + 1)) // 2

        prefixSum = 0
        prefixSums = [0]

        for num in nums:
            prefixSum += num
            prefixSums.append(prefixSum)

        sortedUnique = sorted(list(set(prefixSums)))
        m = len(sortedUnique)
        bit = [0] * (m + 1)

        def add(index: int, value: int):
            while index <= m:
                bit[index] += value
                index += index & (-index)

        def query(index: int) -> int:
            total = 0
            while index > 0:
                total += bit[index]
                index -= index & (-index)
            return total

        totalDistant = 0
        insertedCount = 0

        for pref in prefixSums:
            val1 = pref - goal - k
            idx1 = bisect.bisect_left(sortedUnique, val1)
            totalDistant += query(idx1)

            val2 = pref - goal + k
            idx2 = bisect.bisect_left(sortedUnique, val2)
            totalDistant += insertedCount - query(idx2)

            idxToInsert = bisect.bisect_left(sortedUnique, pref) + 1
            add(idxToInsert, 1)
            insertedCount += 1

        return totalDistant