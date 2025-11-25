# Leetcode 3533: Concatenated Divisibility
# https://leetcode.com/problems/concatenated-divisibility/
# Solved on 25th of November, 2025
class Solution:
    def concatenatedDivisibility(self, nums: list[int], k: int) -> list[int]:
        """
        Finds a permutation of `nums` such that the concatenated number formed by this permutation is divisible by `k`.

        Args:
            nums: A list of non-negative integers.
            k: An integer representing the divisor.
        Returns:
            A list of integers representing the permutation if found, otherwise an empty list.
        """
        n = len(nums)
        nums.sort()
        shifts = []
        vals = []
        for x in nums:
            length = len(str(x))
            shifts.append(pow(10, length, k))
            vals.append(x % k)

        memo = {}

        def solve(mask, currentRem):
            if mask == (1 << n) - 1:
                return currentRem == 0

            state = (mask, currentRem)
            if state in memo:
                return memo[state]

            for i in range(n):
                if not (mask & (1 << i)):
                    nextRem = (currentRem * shifts[i] + vals[i]) % k
                    if solve(mask | (1 << i), nextRem):
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        if not solve(0, 0):
            return []

        res = []
        mask = 0
        currentRem = 0

        for _ in range(n):
            for i in range(n):
                if not (mask & (1 << i)):
                    nextRem = (currentRem * shifts[i] + vals[i]) % k
                    if solve(mask | (1 << i), nextRem):
                        res.append(nums[i])
                        mask |= (1 << i)
                        currentRem = nextRem
                        break

        return res