# Leetcode 3937: Minimum Operations to Make Array Modulo Alternating I
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/
# Solved on 6th of June, 2026
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum operations to make the array modulo alternating.
        An array is modulo alternating if nums[i] % k != nums[i+1] % k for all i.

        :param nums: List of integers to be modified.
        :param k: The modulo divisor.
        :return: The minimum number of operations required.
        """
        evenCounts = [0] * k
        oddCounts = [0] * k

        for i in range(len(nums)):
            curRem = nums[i] % k
            if i % 2 == 0:
                evenCounts[curRem] += 1
            else:
                oddCounts[curRem] += 1

        evenCost = [0] * k
        oddCost = [0] * k

        for targetRem in range(k):
            for curRem in range(k):
                if evenCounts[curRem] > 0:
                    evenCost[targetRem] += evenCounts[curRem] * min((targetRem - curRem) % k, (curRem - targetRem) % k)
                if oddCounts[curRem] > 0:
                    oddCost[targetRem] += oddCounts[curRem] * min((targetRem - curRem) % k, (curRem - targetRem) % k)

        minOps = float('inf')

        for xRem in range(k):
            for yRem in range(k):
                if xRem != yRem:
                    totalOps = evenCost[xRem] + oddCost[yRem]
                    if totalOps < minOps:
                        minOps = totalOps

        return int(minOps)