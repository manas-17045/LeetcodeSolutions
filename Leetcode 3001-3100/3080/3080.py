# Leetcode 3080: Mark Elements on Array by Performing Queries
# https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/
# Solved on 24th of October, 2025
class Solution:
    def unmarkedSumArray(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the sum of unmarked elements in an array after performing a series of queries.

        Args:
            nums: A list of integers representing the initial array.
            queries: A list of lists, where each inner list `[index, k]` represents a query.
                     `index` is the 0-based index of an element to mark, and `k` is the number of
                     smallest unmarked elements to mark.
        Returns:
            A list of integers, where each element is the sum of unmarked elements after each query.
        """

        n = len(nums)
        currentSum = sum(nums)
        answer = []
        isMarked = [False] * n

        valueIndexPairs = []
        for i in range(n):
            valueIndexPairs.append((nums[i], i))

        valueIndexPairs.sort()

        pairPointer = 0

        for query in queries:
            indexToMark = query[0]
            k = query[1]

            if not isMarked[indexToMark]:
                isMarked[indexToMark] = True
                currentSum -= nums[indexToMark]

            elementsToMark = k
            while elementsToMark > 0 and pairPointer < n:
                value, index = valueIndexPairs[pairPointer]

                if not isMarked[index]:
                    isMarked[index] = True
                    currentSum -= value
                    elementsToMark -= 1

                pairPointer += 1

            answer.append(currentSum)

        return answer