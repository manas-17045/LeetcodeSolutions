# Leetcode 4017: Peaks in Array II
# https://leetcode.com/problems/peaks-in-array-ii/
# Solved on 9th of September, 2026
class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Processes peak subarray count and update queries on an integer array.

        :param nums: A list of integers.
        :param queries: A list of queries of type 1 (count) or type 2 (update).
        :return: A list of integers representing answers to type 1 queries.
        """
        numElements = len(nums)
        treeSize = numElements + 2
        treeCount = [0] * (treeSize + 1)
        treeVal = [0] * (treeSize + 1)

        def updateCount(index: int, delta: int) -> None:
            while index <= treeSize:
                treeCount[index] += delta
                index += index & (-index)

        def queryCount(index: int) -> int:
            total = 0
            while index > 0:
                total += treeCount[index]
                index -= index & (-index)
            return total

        def updateVal(index: int, delta: int) -> None:
            while index <= treeSize:
                treeVal[index] += delta
                index += index & (-index)

        def queryVal(index: int) -> int:
            total = 0
            while index > 0:
                total += treeVal[index]
                index -= index & (-index)
            return total

        def findKth(k: int) -> int:
            idx = 0
            step = 1 << treeSize.bit_length()
            while step > 0:
                nextIdx = idx + step
                if nextIdx <= treeSize and treeCount[nextIdx] < k:
                    idx = nextIdx
                    k -= treeCount[idx]
                step >>= 1
            return idx + 1

        def checkPeak(idx: int) -> bool:
            if idx <= 0 or idx >= numElements - 1:
                return False
            return nums[idx] > nums[idx - 1] and nums[idx] > nums[idx + 1]

        def addPeak(peakIdx: int) -> None:
            bitIdx = peakIdx + 1
            countBefore = queryCount(bitIdx)
            totalPeaks = queryCount(treeSize)
            prevPeak = 0 if countBefore == 0 else findKth(countBefore) - 1
            nextPeak = None if countBefore == totalPeaks else findKth(countBefore + 1) - 1
            updateCount(bitIdx, 1)
            updateVal(bitIdx, peakIdx * (peakIdx - prevPeak))
            if nextPeak is not None:
                updateVal(nextPeak + 1, nextPeak * (prevPeak - peakIdx))

        def removePeak(peakIdx: int) -> None:
            bitIdx = peakIdx + 1
            rank = queryCount(bitIdx)
            totalPeaks = queryCount(treeSize)
            prevPeak = 0 if rank == 1 else findKth(rank - 1) - 1
            nextPeak = None if rank == totalPeaks else findKth(rank + 1) - 1
            updateCount(bitIdx, -1)
            updateVal(bitIdx, -peakIdx * (peakIdx - prevPeak))
            if nextPeak is not None:
                updateVal(nextPeak + 1, nextPeak * (peakIdx - prevPeak))

        for i in range(1, numElements - 1):
            if checkPeak(i):
                addPeak(i)

        answerList = []
        for query in queries:
            if query[0] == 1:
                leftBound, rightBound = query[1], query[2]
                if rightBound - leftBound < 2:
                    answerList.append(0)
                    continue
                countBefore = queryCount(leftBound + 1)
                countUpTo = queryCount(rightBound)
                if countUpTo <= countBefore:
                    answerList.append(0)
                    continue
                firstPeak = findKth(countBefore + 1) - 1
                lastPeak = findKth(countUpTo) - 1
                prevFirst = 0 if countBefore == 0 else findKth(countBefore) - 1
                sumVal = queryVal(lastPeak + 1) - queryVal(firstPeak)
                ans = rightBound * (lastPeak - leftBound) - sumVal + firstPeak * (leftBound - prevFirst)
                answerList.append(ans)
            else:
                updateIdx, newVal = query[1], query[2]
                if nums[updateIdx] == newVal:
                    continue
                candidates = [i for i in range(max(1, updateIdx - 1), min(numElements - 1, updateIdx + 2))]
                oldPeakStatus = {i: checkPeak(i) for i in candidates}
                nums[updateIdx] = newVal
                newPeakStatus = {i: checkPeak(i) for i in candidates}
                toRemove = [i for i in candidates if oldPeakStatus[i] and not newPeakStatus[i]]
                toAdd = [i for i in candidates if not oldPeakStatus[i] and newPeakStatus[i]]
                for i in toRemove:
                    removePeak(i)
                for i in toAdd:
                    addPeak(i)

        return answerList