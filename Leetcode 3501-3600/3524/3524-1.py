# Leetcode 3524: Find X Value of Array I
# https://leetcode.com/problems/find-x-value-of-array-i/
# Solved on 3rd of October, 2025
class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        """
        Calculates the count of subarrays whose product modulo k equals x, for each x from 0 to k-1.

        Args:
            nums: A list of integers.
            k: An integer.
        Returns:
            A list of integers, where result[x] is the count of subarrays whose product modulo k is x.
        """
        n = len(nums)
        if k == 1:
            numSubarrays = n * (n + 1) // 2
            return [numSubarrays]

        result = [0] * k
        nonZeroProdSubarrayCount = 0

        lastZeroIndex = -1
        for i in range(n + 1):
            isBoundary = (i == n) or (nums[i] % k == 0)

            if isBoundary:
                segmentStart = lastZeroIndex + 1
                segmentEnd = i
                segmentLen = segmentEnd - segmentStart

                if segmentLen > 0:
                    nonZeroProdSubarrayCount += segmentLen * (segmentLen + 1) // 2

                    currentEndingCounts = [0] * k

                    for j in range(segmentStart, segmentEnd):
                        val = nums[j]
                        vModK = val % k

                        newEndingCounts = [0] * k

                        for p in range(k):
                            if currentEndingCounts[p] > 0:
                                productModK = (p * vModK) % k
                                newEndingCounts[productModK] += currentEndingCounts[p]

                        newEndingCounts[vModK] += 1

                        currentEndingCounts = newEndingCounts

                        for x in range(k):
                            result[x] += currentEndingCounts[x]

                lastZeroIndex = i

        totalSubarrays = n * (n + 1) // 2
        zeroProdSubarrayCount = totalSubarrays - nonZeroProdSubarrayCount
        result[0] += zeroProdSubarrayCount

        return result