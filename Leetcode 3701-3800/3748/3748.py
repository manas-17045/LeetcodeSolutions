# Leetcode 3748: Count Stable Subarrays
# https://leetcode.com/problems/count-stable-subarrays/
# Solved on 6th of November, 2025
class Solution:
    def countStableSubarrays(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Counts the number of stable subarrays for given queries.

        A subarray is stable if its elements are in non-decreasing order.

        Args:
            nums: A list of integers.
            queries: A list of [l, r] pairs representing query ranges (inclusive).
        Returns:
            A list of integers, where each element is the count of stable subarrays for the corresponding query.
        """

        n = len(nums)
        runIds = [0] * n
        runStarts = [0]

        currentRun = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                currentRun += 1
                runStarts.append(i)
            runIds[i] = currentRun

        numRuns = len(runStarts)
        prefixContribs = [0] * (numRuns + 1)

        for i in range(numRuns):
            start = runStarts[i]
            end = runStarts[i + 1] - 1 if i < numRuns - 1 else n - 1
            length = end - start + 1
            contrib = (length * (length + 1)) // 2
            prefixContribs[i + 1] = prefixContribs[i] + contrib

        result = []
        for l, r in queries:
            u = runIds[l]
            v = runIds[r]

            if u == v:
                length = r - l + 1
                result.append((length * (length + 1)) // 2)
            else:
                endU = runStarts[u + 1] - 1
                lenLeft = endU - l + 1
                res = (lenLeft * (lenLeft + 1)) // 2

                startV = runStarts[v]
                lenRight = r - startV + 1
                res += (lenRight * (lenRight + 1)) // 2

                res += prefixContribs[v] - prefixContribs[u + 1]
                result.append(res)

        return result