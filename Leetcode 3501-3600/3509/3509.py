# Leetcode 3509: Maximum Product of Subsequences With an Alternating Sum Equal to K
# https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/
# Solved on 16th of December, 2025
class Solution:
    def maxProduct(self, nums: list[int], k: int, limit: int) -> int:
        """
        Finds the maximum product of a subsequence whose alternating sum equals k.
        :param nums: A list of integers.
        :param k: The target alternating sum.
        :param limit: The maximum possible product.
        :return: The maximum product of a subsequence with an alternating sum equal to k,
                 or -1 if no such subsequence exists.
        """
        OFFSET = 2500

        if abs(k) > 2000:
            return -1

        dp = [[0, 0] for _ in range(limit + 1)]
        zeroDp = [0, 0]
        allDp = [0, 0]

        for x in nums:
            if x == 0:
                newZ0 = zeroDp[1]
                newZ1 = zeroDp[0]

                newZ0 |= allDp[1]
                newZ1 |= allDp[0]

                newZ1 |= (1 << OFFSET)

                zeroDp[0] |= newZ0
                zeroDp[1] |= newZ1

            else:
                for p in range(limit // x, 0, -1):
                    np = p * x
                    dp[np][1] |= (dp[p][0] << x)
                    dp[np][0] |= (dp[p][1] >> x)

                if x <= limit:
                    dp[x][1] |= (1 << (x + OFFSET))

                z0 = zeroDp[0]
                z1 = zeroDp[1]
                zeroDp[1] |= (z0 << x)
                zeroDp[0] |= (z1 >> x)

                a0 = allDp[0]
                a1 = allDp[1]
                allDp[1] |= (a0 << x)
                allDp[0] |= (a1 >> x)
                allDp[1] |= (1 << (x + OFFSET))

        target = 1 << (k + OFFSET)

        for p in range(limit, 0, -1):
            if (dp[p][0] | dp[p][1]) & target:
                return p

        if (zeroDp[0] | zeroDp[1]) & target:
            return 0

        return -1