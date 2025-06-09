# Leetcode 2183: Count Array Pairs Divisible by K
# https://leetcode.com/problems/count-array-pairs-divisible-by-k/
# Solved on 9th of June, 2025
import math


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        # Enumerate all divisors of k
        divs = []
        i = 1
        while i * i <= k:
            if k % i == 0:
                divs.append(i)
                if i * i < k:
                    divs.append(k // i)
            i += 1

        # Count how many times we've seen each gcd-value so far
        cnt = {d: 0 for d in divs}
        ans = 0

        for num in nums:
            g = math.gcd(num, k)
            for d in divs:
                if (g * d) % k == 0:
                    ans += cnt[d]
            cnt[g] += 1

        return ans