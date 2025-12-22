# Leetcode 3757: Number of Effective Subsequences
# https://leetcode.com/problems/number-of-effective-subsequences/
# Solved on 22nd of December, 2025
class Solution:
    def countEffective(self, nums: list[int]) -> int:
        """
        Calculates the number of effective subsequences.

        :param nums: A list of integers.
        :return: The number of effective subsequences modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        k = 0
        for x in nums:
            k |= x

        if k == 0:
            return 0

        limit = 1 << k.bit_length()
        cnt = [0] * limit
        for x in nums:
            cnt[x] += 1

        bitLen = k.bit_length()
        for i in range(bitLen):
            if (k >> i) & 1:
                bit = 1 << i
                step = bit * 2
                for start in range(0, limit, step):
                    for j in range(start, start + bit):
                        cnt[j + bit] += cnt[j]

        pow2 = [1] * (len(nums) + 1)
        curr = 1
        for i in range(1, len(nums) + 1):
            curr = (curr * 2) % mod
            pow2[i] = curr

        dp = [pow2[c] for c in cnt]

        for i in range(bitLen):
            if (k >> i) & 1:
                bit = 1 << i
                step = bit * 2
                for start in range(0, limit, step):
                    for j in range(start, start + bit):
                        val = dp[j + bit] - dp[j]
                        if val < 0:
                            val += mod
                        dp[j + bit] = val

        totalSubsets = pow2[len(nums)]
        ans = (totalSubsets - dp[k] + mod) % mod

        return ans