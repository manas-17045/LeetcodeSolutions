# Leetcode 3187: Peaks in Array
# https://leetcode.com/problems/peaks-in-array/
# Solved on 30th of September, 2025
class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Counts the number of peaks in given ranges and updates array elements.
        :param nums: The input array of integers.
        :param queries: A list of queries. Each query is either type 1 (count peaks in a range) or type 2 (update an element).
        :return: A list of integers, where each element is the result of a type 1 query.
        """
        numLength = len(nums)

        def isPeak(index):
            if not (0 < index < numLength - 1):
                return 0
            if nums[index - 1] < nums[index] and nums[index] > nums[index + 1]:
                return 1
            return 0

        peaks = [isPeak(i) for i in range(numLength)]
        segmentTree = [0] * (4 * numLength)

        def buildTree(node, start, end):
            if start == end:
                segmentTree[node] = peaks[start]
                return

            mid = start + (end - start) // 2
            leftChild = 2 * node + 1
            rightChild = 2 * node + 2

            buildTree(leftChild, start, mid)
            buildTree(rightChild, mid + 1, end)

            segmentTree[node] = segmentTree[leftChild] + segmentTree[rightChild]

        def updateTree(node, start, end, index, value):
            if start == end:
                segmentTree[node] = value
                return

            mid = start + (end - start) // 2
            leftChild = 2 * node + 1
            rightChild = 2 * node + 2

            if start <= index <= mid:
                updateTree(leftChild, start, mid, index, value)
            else:
                updateTree(rightChild, mid + 1, end, index, value)

            segmentTree[node] = segmentTree[leftChild] + segmentTree[rightChild]

        def queryTree(node, start, end, left, right):
            if right < start or end < left:
                return 0

            if left <= start and end <= right:
                return segmentTree[node]

            mid = start + (end - start) // 2
            leftChild = 2 * node + 1
            rightChild = 2 * node + 2

            sumLeft = queryTree(leftChild, start, mid, left, right)
            sumRight = queryTree(rightChild, mid + 1, end, left, right)

            return sumLeft + sumRight

        if numLength > 0:
            buildTree(0, 0, numLength - 1)

        results = []
        for query in queries:
            queryType = query[0]

            if queryType == 1:
                left, right = query[1], query[2]
                if left + 1 > right - 1:
                    results.append(0)
                else:
                    count = queryTree(0, 0, numLength - 1, left + 1, right - 1)
                    results.append(count)
            elif queryType == 2:
                index, value = query[1], query[2]

                indicesToCheck = set()
                if index > 0:
                    indicesToCheck.add(index - 1)
                indicesToCheck.add(index)
                if index < numLength - 1:
                    indicesToCheck.add(index + 1)

                oldPeakValues = {}
                for i in indicesToCheck:
                    if 0 < i < numLength - 1:
                        oldPeakValues[i] = isPeak(i)

                nums[index] = value

                for i in indicesToCheck:
                    if 0 < i < numLength - 1:
                        newPeakValue = isPeak(i)
                        if oldPeakValues.get(i, 0) != newPeakValue:
                            updateTree(0, 0, numLength - 1, i, newPeakValue)

        return results