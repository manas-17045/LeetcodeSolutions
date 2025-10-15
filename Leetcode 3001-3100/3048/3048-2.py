# Leetcode 3048: Earliest Second to Mark Indices I
# https://leetcode.com/problems/earliest-second-to-mark-indices-i/
# Solved on 15th of October, 2025
class Solution:
    def earliestSecondToMarkIndices(self, nums: list[int], changeIndices: list[int]) -> int:
        """
        Finds the earliest second by which all indices can be marked.
        :param nums: A list of integers representing the initial values of the indices.
        :param changeIndices: A list of integers representing the index that can be changed at each second.
        :return: The earliest second by which all indices can be marked, or -1 if it's impossible.
        """
        n = len(nums)
        m = len(changeIndices)

        # Helper function: can we finish marking all indices within first k seconds?
        def can(k: int) -> bool:
            if k < n:
                return False

            last = [-1] * n
            for s in range(k):
                idx = changeIndices[s] - 1
                last[idx] = s + 1

            # If any index never appears in first k seconds -> impossible
            for j in range(n):
                if last[j] == -1:
                    return False

            tasks = [(last[j], nums[j]) for j in range(n)]
            # Sort by deadline ascending
            tasks.sort()

            # Cumulative decrements required so far
            cum_need = 0
            for processed_count, (deadline, need) in enumerate(tasks):
                if need > 0:
                    cum_need += need

                available = (deadline - 1) - processed_count
                if cum_need > available:
                    return False

            # All checks passed
            return True

        lo, hi = 1, m
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans