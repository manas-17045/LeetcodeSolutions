# Leetcode 3691: Maximum Total Subarray Value II
# https://leetcode.com/problems/maximum-total-subarray-value-ii/
# Solved on 4th of December, 2025
import heapq


class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum total value of k subarrays, where the value of a subarray is its maximum element minus its minimum element.

        Args:
            nums: A list of integers representing the input array.
            k: An integer representing the number of subarrays to select.

        Returns:
            An integer representing the maximum total value.
        """
        n = len(nums)
        m = n.bit_length()

        stMin = [nums]
        stMax = [nums]

        for j in range(1, m):
            prevMin = stMin[-1]
            prevMax = stMax[-1]
            shift = 1 << (j - 1)

            currMin = [min(a, b) for a, b in zip(prevMin, prevMin[shift:])]
            stMin.append(currMin)

            currMax = [max(a, b) for a, b in zip(prevMax, prevMax[shift:])]
            stMax.append(currMax)

        heap = []
        for l in range(n):
            length = n - l
            kLog = length.bit_length() - 1
            rowMin = stMin[kLog]
            rowMax = stMax[kLog]

            mn = min(rowMin[l], rowMin[n - (1 << kLog)])
            mx = max(rowMax[l], rowMax[n - (1 << kLog)])
            val = mx - mn
            heapq.heappush(heap, (-val, l, n - 1))

        totalValue = 0

        for _ in range(k):
            negVal, l, r = heapq.heappop(heap)
            totalValue -= negVal

            if l < r:
                nextR = r - 1
                length = nextR - l + 1
                kLog = length.bit_length() - 1
                rowMin = stMin[kLog]
                rowMax = stMax[kLog]

                mn = min(rowMin[l], rowMin[nextR - (1 << kLog) + 1])
                mx = max(rowMax[l], rowMax[nextR - (1 << kLog) + 1])
                newVal = mx - mn
                heapq.heappush(heap, (-newVal, l, nextR))

        return totalValue