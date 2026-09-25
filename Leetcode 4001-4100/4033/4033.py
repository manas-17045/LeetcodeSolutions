# Leetcode 4033: Valid K-Unique Subarrays I
# https://leetcode.com/problems/valid-k-unique-subarrays-i/
# Solved on 25th of September, 2026
class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        """
        Evaluates a list of queries to determine if each subarray contains exactly
        k distinct elements, all of which appear an even number of times.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The required number of distinct elements.
            queries (list[list[int]]): A list of query intervals [left, right].

        Returns:
            list[bool]: A boolean array where each element corresponds to the validity of a query.
        """
        numLen = len(nums)
        queryLen = len(queries)
        blockSize = max(1, int(numLen / (queryLen ** 0.5)))

        queryList = []
        for i in range(queryLen):
            queryList.append((queries[i][0], queries[i][1], i))

        queryList.sort(key=lambda x: (x[0] // blockSize, x[1] if (x[0] // blockSize) % 2 == 0 else -x[1]))

        ansArr = [False] * queryLen
        freqMap = [0] * 100005
        distinctCount = 0
        oddCount = 0

        leftPtr = 0
        rightPtr = -1

        for queryLeft, queryRight, queryIdx in queryList:
            while leftPtr > queryLeft:
                leftPtr -= 1
                currentNum = nums[leftPtr]
                freqMap[currentNum] += 1
                if freqMap[currentNum] == 1:
                    distinctCount += 1
                    oddCount += 1
                elif freqMap[currentNum] % 2 == 0:
                    oddCount -= 1
                else:
                    oddCount += 1

            while rightPtr < queryRight:
                rightPtr += 1
                currentNum = nums[rightPtr]
                freqMap[currentNum] += 1
                if freqMap[currentNum] == 1:
                    distinctCount += 1
                    oddCount += 1
                elif freqMap[currentNum] % 2 == 0:
                    oddCount -= 1
                else:
                    oddCount += 1

            while leftPtr < queryLeft:
                currentNum = nums[leftPtr]
                freqMap[currentNum] -= 1
                if freqMap[currentNum] == 0:
                    distinctCount -= 1
                    oddCount -= 1
                elif freqMap[currentNum] % 2 == 0:
                    oddCount -= 1
                else:
                    oddCount += 1
                leftPtr += 1

            while rightPtr > queryRight:
                currentNum = nums[rightPtr]
                freqMap[currentNum] -= 1
                if freqMap[currentNum] == 0:
                    distinctCount -= 1
                    oddCount -= 1
                elif freqMap[currentNum] % 2 == 0:
                    oddCount -= 1
                else:
                    oddCount += 1
                rightPtr -= 1

            if distinctCount == k and oddCount == 0:
                ansArr[queryIdx] = True

        return ansArr