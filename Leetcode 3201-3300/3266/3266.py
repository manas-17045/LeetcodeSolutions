# Leetcode 3266: Final Array State After K Multiplication Operations II
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/
# Solved on 3rd of November, 2025
import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        """
        Calculates the final state of an array after k multiplication operations.
        :param nums: The initial array of integers.
        :param k: The number of multiplication operations to perform.
        :param multiplier: The value to multiply elements by.
        :return: The final state of the array after k operations, with elements modulo 10^9 + 7.
        """
        if multiplier == 1:
            return nums

        mod = 1000000007
        n = len(nums)
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)

        limit = max(nums)

        while k > 0:
            val, idx = heap[0]
            if val * multiplier > limit:
                break
            heapq.heappop(heap)
            val *= multiplier
            k -= 1
            heapq.heappush(heap, (val, idx))

        sortedStates = sorted(heap)
        cycles = k // n
        rem = k % n

        ans = [0] * n
        for i, (val, idx) in enumerate(sortedStates):
            power = cycles
            if i < rem:
                power += 1

            newValue = (val % mod) * pow(multiplier, power, mod) % mod
            ans[idx] = newValue

        return ans