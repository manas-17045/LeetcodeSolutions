# Leetcode 3501: Maximize Active Section with Trade II
# https://leetcode.com/problems/maximize-active-section-with-trade-ii/
# Solved on 28th of February, 2026
import bisect
import math


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        """
        Calculates the maximum number of active sections (ones) after performing a trade
        within the specified query ranges.

        :param s: A binary string representing the initial sections.
        :param queries: A list of queries, where each query is a range [l, r].
        :return: A list of integers representing the maximum active sections for each query.
        """
        totalOnes = s.count('1')
        n = len(s)

        blocks = []
        starts = []
        ends = []
        i = 0

        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                end = i - 1
                blocks.append((start, end))
                starts.append(start)
                ends.append(end)
            else:
                i += 1

        if not blocks:
            return [totalOnes] * len(queries)

        m = len(blocks)
        lenBlocks = [b[1] - b[0] + 1 for b in blocks]
        sumBlocks = [lenBlocks[i] + lenBlocks[i + 1] for i in range(m - 1)]

        numSums = len(sumBlocks)
        logTable = [0] * (numSums + 1)
        if numSums > 0:
            maxK = int(math.log2(numSums)) + 1
            st = [[0] * maxK for _ in range(numSums)]
            for i in range(numSums):
                st[i][0] = sumBlocks[i]
            for j in range(1, maxK):
                for i in range(numSums - (1 << j) + 1):
                    st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])

            for i in range(2, numSums + 1):
                logTable[i] = logTable[i // 2] + 1

        ans = []
        for l, r in queries:
            x = bisect.bisect_left(ends, l)
            y = bisect.bisect_right(starts, r) - 1

            if x > y:
                ans.append(totalOnes)
                continue

            if x == y:
                ans.append(totalOnes)
                continue

            if y == x + 1:
                cx = min(r, ends[x]) - max(l, starts[x]) + 1
                cy = min(r, ends[y]) - max(l, starts[y]) + 1
                ans.append(totalOnes + cx + cy)
                continue

            cx = ends[x] - max(l, starts[x]) + 1
            cy = min(r, ends[y]) - starts[y] + 1

            gainLeft = cx + lenBlocks[x + 1]
            gainRight = lenBlocks[y - 1] + cy
            maxGain = max(gainLeft, gainRight)

            leftRMQ = x + 1
            rightRMQ = y - 2
            if leftRMQ <= rightRMQ:
                length = rightRMQ - leftRMQ + 1
                k = logTable[length]
                gainMid = max(st[leftRMQ][k], st[rightRMQ - (1 << k) + 1][k])
                maxGain = max(maxGain, gainMid)

            ans.append(totalOnes + maxGain)

        return ans