# Leetcode 3671: Sum of Beautiful Subsequences
# https://leetcode.com/problems/sum-of-beautiful-subsequences/
# Solved on 23rd of November, 2025
class Solution:
    def totalBeauty(self, nums: list[int]) -> int:
        """
        Calculates the total beauty of all beautiful subsequences.

        Args:
            nums: A list of integers.
        Returns:
            The total beauty modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        maxVal = 0
        for x in nums:
            if x > maxVal:
                maxVal = x

        buckets = [[] for _ in range(maxVal + 1)]
        for x in nums:
            limit = int(x ** 0.5)
            for i in range(1, limit + 1):
                if x % i == 0:
                    buckets[i].append(x)
                    d = x // i
                    if d != i:
                        buckets[d].append(x)

        bit = [0] * (maxVal + 1)
        countSeq = [0] * (maxVal + 1)

        for g in range(1, maxVal + 1):
            sub = buckets[g]
            if not sub:
                continue

            history = []
            currentGCount = 0

            for x in sub:
                idx = x - 1
                prevCount = 0
                while idx > 0:
                    prevCount = (prevCount + bit[idx]) % mod
                    idx -= idx & (-idx)

                newCount = (prevCount + 1) % mod

                idx = x
                while idx <= maxVal:
                    bit[idx] = (bit[idx] + newCount) % mod
                    idx += idx & (-idx)

                history.append((x, newCount))
                currentGCount = (currentGCount + newCount) % mod

            countSeq[g] = currentGCount

            for x, val in history:
                idx = x
                while idx <= maxVal:
                    bit[idx] = (bit[idx] - val) % mod
                    idx += idx & (-idx)

        totalBeauty = 0
        for g in range(maxVal, 0, -1):
            if countSeq[g] == 0:
                continue

            count = countSeq[g]
            for multiple in range(2 * g, maxVal + 1, g):
                count = (count - countSeq[multiple]) % mod

            countSeq[g] = count
            totalBeauty = (totalBeauty + g * count) % mod

        return totalBeauty