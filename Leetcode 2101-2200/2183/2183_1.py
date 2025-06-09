# Leetcode 2183: Count Array Pairs Divisible by K
# https://leetcode.com/problems/count-array-pairs-divisible-by-k/
# Solved on 9th of June, 2025
import math
from collections import Counter


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        pairCount = 0
        gcdCounts = Counter()

        for num in nums:
            currentGcd = math.gcd(num, k)

            for prevGcd, frequency in gcdCounts.items():
                if (currentGcd * prevGcd) % k == 0:
                    pairCount += frequency

            gcdCounts[currentGcd] += 1

        return pairCount