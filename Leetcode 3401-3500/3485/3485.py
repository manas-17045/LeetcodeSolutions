# Leetcode 3485: Longest Common Prefix of K Strings After Removal
# https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/
# Solved on 15th of December, 2025
import sys
sys.setrecursionlimit(200000)


class Solution:
    def longestCommonPrefix(self, words: list[str], k: int) -> list[int]:
        """
        Calculates the longest common prefix for each word in `words` after removing `k` other words.
        :param words: A list of strings.
        :param k: The number of words to remove.
        :return: A list of integers, where each element `i` is the length of the longest common prefix
                 for `words[i]` after removing `k` other words.
        """
        n = len(words)
        if n <= k:
            return [0] * n

        totalChars = sum(len(w) for w in words)
        capacity = totalChars + 2

        children = [{} for _ in range(capacity)]
        cnt = [0] * capacity
        depth = [0] * capacity

        nodesCount = 1
        wordEndNodes = []

        for w in words:
            curr = 0
            cnt[0] += 1
            for char in w:
                if char not in children[curr]:
                    children[curr][char] = nodesCount
                    depth[nodesCount] = depth[curr] + 1
                    nodesCount += 1
                curr = children[curr][char]
                cnt[curr] += 1
            wordEndNodes.append(curr)

        tin = [0] * nodesCount
        tout = [0] * nodesCount
        timer = 0

        def dfs(u):
            nonlocal timer
            timer += 1
            tin[u] = timer
            for v in children[u].values():
                dfs(v)
            tout[u] = timer

        dfs(0)

        lAlways = 0
        intervals = []

        for u in range(nodesCount):
            c = cnt[u]
            d = depth[u]
            if c > k:
                if d > lAlways:
                    lAlways = d
            elif c == k:
                intervals.append((tin[u], tout[u], d))

        if not intervals:
            return [lAlways] * n

        maxTime = timer + 1
        leftMax = [-1] * (maxTime + 1)
        rightMax = [-1] * (maxTime + 1)

        sortedByEnd = sorted(intervals, key=lambda x: x[1])
        curr = -1
        ptr = 0
        numIntervals = len(intervals)

        for t in range(1, maxTime + 1):
            while ptr < numIntervals and sortedByEnd[ptr][1] < t:
                if sortedByEnd[ptr][2] > curr:
                    curr = sortedByEnd[ptr][2]
                ptr += 1
            leftMax[t] = curr

        sortedByStart = sorted(intervals, key=lambda x: x[0])
        curr = -1
        ptr = numIntervals - 1

        for t in range(maxTime, 0, -1):
            while ptr >= 0 and sortedByStart[ptr][0] > t:
                if sortedByStart[ptr][2] > curr:
                    curr = sortedByStart[ptr][2]
                ptr -= 1
            rightMax[t] = curr

        ans = []
        for endNode in wordEndNodes:
            t = tin[endNode]
            val = max(leftMax[t], rightMax[t])
            ans.append(max(lAlways, val))

        return ans