# Leetcode 3092: Most Frequent IDs
# https://leetcode.com/problems/most-frequent-ids/
# Solved on 4th of January, 2026
import heapq


class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        """
        Calculates the most frequent ID after each operation.

        Args:
            nums (list[int]): A list of IDs.
            freq (list[int]): A list of frequencies corresponding to the IDs.

        Returns:
            list[int]: A list where each element is the frequency of the most frequent ID after each operation.
        """
        frequencyMap = {}
        maxHeap = []
        resultList = []

        for i in range(len(nums)):
            currentId = nums[i]
            currentFreq = freq[i]

            if currentId in frequencyMap:
                frequencyMap[currentId] += currentFreq
            else:
                frequencyMap[currentId] = currentFreq

            heapq.heappush(maxHeap, [-frequencyMap[currentId], currentId])

            while maxHeap and -maxHeap[0][0] != frequencyMap[maxHeap[0][1]]:
                heapq.heappop(maxHeap)

            if not maxHeap:
                resultList.append(0)
            else:
                resultList.append(-maxHeap[0][0])

        return resultList