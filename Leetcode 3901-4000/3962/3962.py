# Leetcode 3962: Maximum Subarray Sum After at Most K Swaps
# https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/
# Solved on 13th of Octiber, 2026
from heapq import heappop, heappush, heappushpop


class Solution:
    def maxSum(slef, nums: list[int], k: int) -> int:
        """
        Calculates the maximum possible subarray sum after performing at most k element swaps.

        Parameters:
            nums (list[int]): The input list of integers.
            k (int): The maximum number of allowed swap operations.

        Returns:
            int: The maximum possible subarray sum achievable after at most k swaps.
        """
        arrayLen = len(nums)

        if k == 0:
            maxSubarraySum = nums[0]
            currRunningSum = 0
            for currVal in nums:
                currRunningSum = max(currVal, currRunningSum + currVal)
                if currRunningSum > maxSubarraySum:
                    maxSubarraySum = currRunningSum
            return maxSubarraySum

        descIndices = sorted(range(arrayLen), key=lambda idx: nums[idx], reverse=True)
        indexRank = [0] * arrayLen
        for rankPos, originalIdx in enumerate(descIndices):
            indexRank[originalIdx] = rankPos

        maxSubarraySum = nums[0]

        for leftIdx in range(arrayLen):
            inUsedHeap = []
            inRemHeap = []
            inUsedSum = 0
            outUsedSum = 0
            windowSum = 0
            outPtr = 0

            for rightIdx in range(leftIdx, arrayLen):
                currVal = nums[rightIdx]
                windowSum += currVal

                if indexRank[rightIdx] < outPtr:
                    outUsedSum -= currVal
                    poppedVal = -heappop(inUsedHeap)
                    inUsedSum -= poppedVal
                    heappush(inRemHeap, poppedVal)
                
                if inUsedHeap and currVal < -inUsedHeap[0]:
                    poppedVal = -heappushpop(inUsedHeap, -currVal)
                    inUsedSum += currVal - poppedVal
                    heappush(inRemHeap, poppedVal)
                else:
                    heappush(inRemHeap, currVal)

                while len(inUsedHeap) < k and inRemHeap:
                    while outPtr < arrayLen and leftIdx <= descIndices[outPtr] <= rightIdx:
                        outPtr += 1
                    if outPtr == arrayLen:
                        break
                    bestOutVal = nums[descIndices[outPtr]]
                    bestInVal = inRemHeap[0]
                    if bestInVal < bestOutVal:
                        heappop(inRemHeap)
                        heappush(inUsedHeap, -bestInVal)
                        inUsedSum += bestInVal
                        outUsedSum += bestOutVal
                        outPtr += 1
                    else:
                        break

                candidateSum = windowSum - inUsedSum + outUsedSum
                if candidateSum > maxSubarraySum:
                    maxSubarraySum = candidateSum

        return maxSubarraySum