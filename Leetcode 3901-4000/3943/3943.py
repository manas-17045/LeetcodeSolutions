# Leetcode 3943: Number of Pairs After Increment
# https://leetcode.com/problems/number-of-pairs-after-increment/
# Solved on 9th of June, 2026
class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of pairs (i, j) such that nums1[i] + nums2[j] equals a target value
        after performing range increment updates on nums2.

        :param nums1: List of integers representing the first array.
        :param nums2: List of integers representing the second array.
        :param queries: List of queries where type 1 is range update and type 2 is pair counting.
        :return: A list of results for each type 2 query.
        """
        n = len(nums2)
        blockSize = int(n ** 0.5) + 1
        numBlocks = (n + blockSize - 1) // blockSize

        freq = [{} for _ in range(numBlocks)]
        lazy = [0] * numBlocks

        for i in range(n):
            b = i // blockSize
            freq[b][nums2[i]] = freq[b].get(nums2[i], 0) + 1

        nums1Freq = {}
        for num in nums1:
            nums1Freq[num] = nums1Freq.get(num, 0) + 1

        ansArr = []

        for q in queries:
            if q[0] == 1:
                x, y, val = q[1], q[2], q[3]
                startBlock = x // blockSize
                endBlock = y // blockSize

                if startBlock == endBlock:
                    freqBlock = freq[startBlock]
                    for i in range(x, y + 1):
                        oldVal = nums2[i]
                        freqBlock[oldVal] -= 1
                        if freqBlock[oldVal] == 0:
                            del freqBlock[oldVal]
                        nums2[i] += val
                        newVal = nums2[i]
                        freqBlock[newVal] = freqBlock.get(newVal, 0) + 1
                else:
                    freqStart = freq[startBlock]
                    end1 = (startBlock + 1) * blockSize
                    for i in range(x, end1):
                        oldVal = nums2[i]
                        freqStart[oldVal] -= 1
                        if freqStart[oldVal] == 0:
                            del freqStart[oldVal]
                        nums2[i] += val
                        newVal = nums2[i]
                        freqStart[newVal] = freqStart.get(newVal, 0) + 1

                    for b in range(startBlock + 1, endBlock):
                        lazy[b] += val

                    freqEnd = freq[endBlock]
                    start2 = endBlock * blockSize
                    for i in range(start2, y + 1):
                        oldVal = nums2[i]
                        freqEnd[oldVal] -= 1
                        if freqEnd[oldVal] == 0:
                            del freqEnd[oldVal]
                        nums2[i] += val
                        newVal = nums2[i]
                        freqEnd[newVal] = freqEnd.get(newVal, 0) + 1
            else:
                tot = q[1]
                res = 0
                for b in range(numBlocks):
                    currentLazy = lazy[b]
                    currentFreq = freq[b]
                    for v1, count in nums1Freq.items():
                        needed = tot - v1 - currentLazy
                        if needed in currentFreq:
                            res += count * currentFreq[needed]

                ansArr.append(res)

        return ansArr