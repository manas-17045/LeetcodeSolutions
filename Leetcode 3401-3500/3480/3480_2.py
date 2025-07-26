# Leetcpde 3480: Maximize Subarrays After Removing One Conflicting Pair
# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/
# Solved on 26th of July, 2025
import heapq


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        """
        Calculates the maximum number of valid subarrays [l..r] that can be formed,
        potentially by removing at most one conflicting pair.
        :param n: The upper bound for the integers in the subarrays (1 to n).
        :param conflictingPairs: A list of pairs [u, v] that cannot both be included in a valid subarray.
        :return: The maximum number of valid subarrays.
        """
        # Group pairs by their smaller endpoint x
        m = len(conflictingPairs)
        buckets = [[] for _ in range(n + 2)]
        for idx, (a, b) in enumerate(conflictingPairs):
            x, y = (a, b) if a < b else (b, a)
            buckets[x].append((y, idx))

        heap = []  # min-heap of (y_j, j) for all pairs with x_j >= current l
        delta = [0] * m  # delta[j] = extra valid subarrays if we remove pair j
        valid_base = 0  # valid subarrays with no removal
        INF = n + 1

        # Sweep l from n down to 1
        for l in range(n, 0, -1):
            # Add all pairs whose x == l
            for y, j in buckets[l]:
                heapq.heappush(heap, (y, j))

            # Peek the smallest endpoint y1 (and its pair-id i1)
            if heap:
                y1, i1 = heap[0]
            else:
                y1, i1 = INF, -1

            # Peek the second-smallest endpoint y2
            if len(heap) >= 2:
                ytmp, jtmp = heapq.heappop(heap)
                y2, _ = heap[0]
                heapq.heappush(heap, (ytmp, jtmp))
            else:
                y2 = INF

            # With no removal, subarrays [l..r] with r < y1 are valid: count = y1 - l
            valid_base += y1 - l

            # If we remove the pair that gave y1, we extend to r < y2 instead:
            if i1 != -1:
                delta[i1] += (y2 - y1)

        # Best we can do is remove the pair with the largest delta
        best_gain = max(delta) if delta else 0
        return valid_base + best_gain