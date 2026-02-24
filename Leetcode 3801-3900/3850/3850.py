# Leetcode 3850: Count Sequences to K
# https://leetcode.com/problems/count-sequences-to-k/
# Solved on 24th of February, 2026
class Solution:
    def countSequences(self, nums: list[int], k: int) -> int:
        """
        Calculates the number of sequences that can be formed from nums to reach target k.

        :param nums: A list of integers containing only factors of 2, 3, and 5.
        :param k: The target integer to reach through multiplication/division sequences.
        :return: The total count of valid sequences.
        """
        tempK = k
        k2 = k3 = k5 = 0

        while tempK % 2 == 0:
            k2 += 1
            tempK //= 2
        while tempK % 3 == 0:
            k3 += 1
            tempK //= 3
        while tempK % 5 == 0:
            k5 += 1
            tempK //= 5

        if tempK != 1:
            return 0

        fact = {
            1: (0, 0, 0),
            2: (1, 0, 0),
            3: (0, 1, 0),
            4: (2, 0, 0),
            5: (0, 0, 1),
            6: (1, 1, 0)
        }

        n = len(nums)
        rem2 = [0] * (n + 1)
        rem3 = [0] * (n + 1)
        rem5 = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            d2, d3, d5 = fact[nums[i]]
            rem2[i] = rem2[i + 1] + d2
            rem3[i] = rem3[i + 1] + d3
            rem5[i] = rem5[i + 1] + d5

        memo = {}

        def dfs(i: int, r2: int, r3: int, r5: int) -> int:
            if abs(r2) > rem2[i] or abs(r3) > rem3[i] or abs(r5) > rem5[i]:
                return 0
            if i == n:
                return 1

            state = (i, r2, r3, r5)
            if state in memo:
                return memo[state]

            d2, d3, d5 = fact[nums[i]]

            ans = 0
            ans += dfs(i + 1, r2 - d2, r3 - d3, r5 - d5)
            ans += dfs(i + 1, r2 + d2, r3 + d3, r5 + d5)
            ans += dfs(i + 1, r2, r3, r5)

            memo[state] = ans
            return ans

        return dfs(0, k2, k3, k5)