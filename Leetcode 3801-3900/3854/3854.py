# Leetcode 3854: Minimum Operations to Make Array Parity Alternating
# https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/
# Solved on 1st of March, 2026
class Solution:
    def makeParityAlternating(self, nums: list[int]) -> list[int]:
        """
        Calculates the minimum operations to make the array parity alternating and the
        minimum possible difference between the maximum and minimum elements in such an array.

        :param nums: List of integers to be transformed.
        :return: A list containing [minimum operations, minimum possible difference].
        """
        listLength = len(nums)
        opsEvenFirst = 0
        opsOddFirst = 0

        for i in range(listLength):
            currentParity = nums[i] % 2
            if currentParity != i % 2:
                opsEvenFirst += 1
            if currentParity != 1 - (i % 2):
                opsOddFirst += 1

        minOpsCount = min(opsEvenFirst, opsOddFirst)

        def getMinDiff(startParity):
            elementTuples =[]
            for i in range(listLength):
                currentParity = nums[i] % 2
                targetParity = i % 2 if startParity == 0 else 1 - (i % 2)

                if currentParity == targetParity:
                    elementTuples.append((nums[i], i))
                else:
                    elementTuples.append((nums[i] - 1, i))
                    elementTuples.append((nums[i] + 1, i))

            elementTuples.sort(key=lambda x: x[0])
            minDifference = float('inf')
            frequencyMap = {}
            leftPointer = 0
            uniqueCount = 0

            for rightPointer in range(len(elementTuples)):
                index = elementTuples[rightPointer][1]

                if frequencyMap.get(index, 0) == 0:
                    uniqueCount += 1
                frequencyMap[index] = frequencyMap.get(index, 0) + 1

                while uniqueCount == listLength:
                    currentDiff = elementTuples[rightPointer][0] - elementTuples[leftPointer][0]
                    if currentDiff < minDifference:
                        minDifference = currentDiff

                    leftElementIndex = elementTuples[leftPointer][1]
                    frequencyMap[leftElementIndex] -= 1
                    if frequencyMap[leftElementIndex] == 0:
                        uniqueCount -= 1
                    leftPointer += 1

            return minDifference

        minPossibleDiff = float('inf')

        if opsEvenFirst == minOpsCount:
            currentMinDiff = getMinDiff(0)
            if currentMinDiff < minPossibleDiff:
                minPossibleDiff = currentMinDiff

        if opsOddFirst == minOpsCount:
            currentMinDiff = getMinDiff(1)
            if currentMinDiff < minPossibleDiff:
                minPossibleDiff = currentMinDiff

        return [minOpsCount, minPossibleDiff]