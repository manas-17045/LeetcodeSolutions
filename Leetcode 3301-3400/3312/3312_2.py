# Leetcode 3312: Sorted GCD Pair Queries
# https://leetcode.com/problems/sorted-gcd-pair-queries/
# Solved on 16th of June, 2025
import bisect


class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        Calculates the k-th smallest GCD among all pairs of numbers in `nums` for each query `q`.

        Args:
            nums: A list of integers.
            queries: A list of integers representing the k-th smallest GCD to find.

        Returns:
            A list of integers, where each element is the k-th smallest GCD corresponding
            to the respective query in `queries`.
        """
        # Build frequency table and find maximum value
        maxV = max(nums)
        freq = [0] * (maxV + 1)
        for v in nums:
            freq[v] += 1

        # cntDiv[d] = how many nums are divisible by d
        cntDiv = [0] * (maxV + 1)
        for d in range(1, (maxV + 1)):
            for m in range(d, (maxV + 1), d):
                cntDiv[d] += freq[m]

        f = [0] * (maxV + 1)
        # Process d in descending order
        for d in range(maxV, 0, -1):
            c = cntDiv[d]
            # Total pairs both divisible by d
            totalPairs = c * (c - 1) // 2
            j = 2 * d
            sub = 0
            while j <= maxV:
                sub += f[j]
                j += d
            f[d] = totalPairs - sub

        # Collect only the GCD's that actually occur, build prefix sum
        gcds = []
        cum = []
        running = 0
        for d in range(1, (maxV + 1)):
            if f[d] > 0:
                running += f[d]
                gcds.append(d)
                cum.append(running)

        # Answer each query by binary-searching cum to find which block it falls in
        ans = []
        for q in queries:
            i = bisect.bisect_right(cum, q)
            ans.append(gcds[i])
        return ans