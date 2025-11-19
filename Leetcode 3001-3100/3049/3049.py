# Leetcode 3049: Earliest Second to Mark Indices II
# https://leetcode.com/problems/earliest-second-to-mark-indices-ii/
# Solved on 19th of November, 2025
import heapq


class Solution:
    def earliestSecondToMarkIndices(self, nums: list[int], changeIndices: list[int]) -> int:
        """
        Finds the earliest second by which all indices can be marked.

        Args:
            nums: A list of integers representing the values at each index.
            changeIndices: A list of integers representing the index to mark at each second.
        Returns:
            The earliest second by which all indices can be marked, or -1 if it's not possible.
        """
        n = len(nums)
        m = len(changeIndices)

        if n > m:
            return -1

        first_occurrence = {}
        for s, idx in enumerate(changeIndices):
            curr_idx = idx - 1
            if curr_idx not in first_occurrence:
                first_occurrence[curr_idx] = s + 1

        total_nums = sum(nums)
        base_cost = total_nums + n

        def check(limit):
            reset_ops = {}
            for i in range(n):
                if i in first_occurrence and first_occurrence[i] <= limit:
                    reset_ops[first_occurrence[i]] = i

            pq = []
            capacity = 0

            for t in range(limit, 0, -1):
                if t in reset_ops:
                    idx = reset_ops[t]
                    val = nums[idx]

                    if val > 1:
                        heapq.heappush(pq, val)
                        capacity -= 1

                        if capacity < 0:
                            heapq.heappop(pq)
                            capacity += 2
                    else:
                        capacity += 1
                else:
                    capacity += 1

            saved = 0
            for v in pq:
                saved += (v - 1)

            return (base_cost - saved) <= limit

        low, high = n, m
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans