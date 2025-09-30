# Leetcode 3478: Choose K Elements With Maximum Sum
# https://leetcode.com/problems/choose-k-elements-with-maximum-sum/
# Solved on 29th of September, 2025
import heapq


class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        """
        Finds the maximum sum of k elements from nums2 for each element in nums1,
        considering elements from nums2 whose corresponding nums1 value is less than or equal to the current nums1 value.
        :param nums1: A list of integers.
        :param nums2: A list of integers.
        :param k: The number of elements to choose from nums2.
        :return: A list of integers, where each element resultArray[i] is the maximum sum of k elements from nums2.
        """
        n = len(nums1)

        combinedData = []
        for i in range(n):
            combinedData.append((nums1[i], nums2[i], i))

        combinedData.sort()

        resultArray = [0] * n
        minHeap = []
        currentSum = 0

        i = 0
        while i < n:
            j = i
            while j < n and combinedData[j][0] == combinedData[i][0]:
                j += 1

            for p in range(i, j):
                originalIndex = combinedData[p][2]
                resultArray[originalIndex] = currentSum

            for p in range(i, j):
                currentNum2 = combinedData[p][1]

                if len(minHeap) < k:
                    heapq.heappush(minHeap, currentNum2)
                    currentSum += currentNum2
                elif currentNum2 > minHeap[0]:
                    poppedValue = heapq.heappushpop(minHeap, currentNum2)
                    currentSum += currentNum2 - poppedValue

            i = j

        return resultArray