# Leetcode 1998: GCD Sort of an Array
# https://leetcode.com/problems/gcd-sort-of-an-array/
# Solved on 14th of July, 2025
class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra

class Solution:
    def gcdSort(self, nums: list[int]) -> bool:
        """
        Determines if an array can be sorted by swapping elements that share a common factor greater than 1.

        :param nums: A list of integers.
        :return: True if the array can be sorted, False otherwise.
        """
        n = len(nums)
        # Prepare smallest-prime-factor SPF) sieve up to max(nums)
        maxv = max(nums)
        spf = list(range(maxv + 1))
        for i in range(2, int(maxv**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, (maxv + 1), i):
                    if spf[j] == j:
                        spf[j] = i

        # Build DSU over [0...maxv], to union each number with its prime factors
        dsu = DSU(maxv + 1)
        for x in nums:
            orig = x
            # Factorize x and union with each distinct prime factor
            while x > 1:
                p = spf[x]
                dsu.union(orig, p)
                while x % p == 0:
                    x //= p

        # Check if we can place each sorted value into its position by swaps
        sorted_nums = sorted(nums)
        for a, b in zip(nums, sorted_nums):
            if dsu.find(a) != dsu.find(b):
                return False
        return True