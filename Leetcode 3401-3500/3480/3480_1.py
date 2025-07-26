# Leetcpde 3480: Maximize Subarrays After Removing One Conflicting Pair
# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/
# Solved on 26th of July, 2025
import collections
from bisect import bisect_right


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        """
        Calculates the maximum number of subarrays after removing one conflicting pair.

        Args:
            n (int): The upper bound for the elements in the subarrays (1 to n).
            conflictingPairs (list[list[int]]): A list of pairs [u, v] that are conflicting.
        Returns:
            int: The maximum number of subarrays.
        """
        if not conflictingPairs:
            return n * (n + 1) // 2

        # Count frequencies and find unique pairs
        pairCounter = collections.Counter(tuple(sorted(p)) for p in conflictingPairs)
        uniquePairs = set(pairCounter.keys())

        leftsByRight = collections.defaultdict(list)
        rightsByLeft = collections.defaultdict(list)

        for u, v in uniquePairs:
            leftsByRight[v].append(u)
            rightsByLeft[u].append(v)

        for u in rightsByLeft:
            rightsByLeft[u].sort()

        # Calculate L1, L2, and baseCount
        l1 = [0] * (n + 1)
        l2 = [0] * (n + 1)
        maxLeft = 0
        secondMaxLeft = 0

        for r in range(1, n + 1):
            if r in leftsByRight:
                for left in sorted(leftsByRight[r], reverse=True):
                    if left > maxLeft:
                        secondMaxLeft = maxLeft
                        maxLeft = left
                    elif left > secondMaxLeft and left < maxLeft:
                        secondMaxLeft = left
            l1[r] = maxLeft
            l2[r] = secondMaxLeft

        baseCount = 0
        for r in range(1, n + 1):
            baseCount += r - l1[r]

        # Calculate potential gain for each TYPE of pair
        potentialGains = collections.defaultdict(int)
        for r in range(1, n + 1):
            u = l1[r]
            if u == 0:
                continue

            vOptions = rightsByLeft[u]
            numActiveSupporters = bisect_right(vOptions, r)

            if numActiveSupporters == 1:
                gainAtR = u - l2[r]
                if gainAtR > 0:
                    v = vOptions[0]
                    potentialGains[(u, v)] += gainAtR

        # Find max *actual* gain based on pair counts
        maxActualGain = 0
        for pair_type, gain in potentialGains.items():
            if pairCounter[pair_type] == 1:
                maxActualGain = max(maxActualGain, gain)

        return baseCount + maxActualGain