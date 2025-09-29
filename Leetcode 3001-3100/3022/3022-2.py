# Leetcode 3022: Minimize OR of Remaining Elements Using Operations
# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/
# Solved on 29th of September, 2025
class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum possible bitwise OR sum of the remaining elements after performing at most k operations.

        Args:
            nums: A list of integers.
            k: The maximum number of operations allowed.
        Returns:
            The minimum possible bitwise OR sum.
        """
        n = len(nums)
        need = n - k

        max_or = 0
        for v in nums:
            max_or |= v

        UB = (1 << 30)  - 1

        def feasible(target: int) -> bool:

            mask_bad = (~target) & UB
            cnt = 0
            cur_and = UB
            for v in nums:
                cur_and &= v
                if (cur_and & mask_bad) == 0:
                    cnt += 1
                    cur_and = UB
                    if cnt >= need:
                        return True

            return cnt >= need

        ans_mask = max_or

        for bit in range(30, -1, -1):
            if ans_mask & (1 << bit):
                candidate = ans_mask & ~(1 << bit)
                if feasible(candidate):
                    ans_mask = candidate

        return ans_mask