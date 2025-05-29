# Leetcode 2862: Maximum Element-Sum of a Complete Subset of Indices
# https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/
# Solved on 28th of May, 2025
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum element-sum of a complete subset of indices.

        A complete subset of indices is a subset of indices {i_1, i_2, ..., i_k}
        such that the product of any two indices i_j * i_l is a perfect square.
        This condition is equivalent to saying that all indices in the subset
        have the same square-free part.

        The square-free part of a positive integer n is the product of the
        distinct prime factors of n. For example, the square-free part of 12
        (2^2 * 3) is 2 * 3 = 6. The square-free part of 18 (2 * 3^2) is 2 * 3 = 6.
        The square-free part of 7 is 7.

        Args:
            nums: A list of integers.

        Returns:
            The maximum sum of elements nums[i-1] for indices i in a complete subset.
        """
        n_len = len(nums)

        # Constraints: 1 <= nums.length <= 10^4. So n_len is at least 1.
        # If n_len could be 0, we'd return 0 here.

        # Precompute Smallest Prime Factor (SPF) up to n_len
        # spf[i] stores the smallest prime factor of i.
        # For a prime number i, spf[i] = i.
        spf = [0] * (n_len + 1)
        primes = [] # List of prime numbers found so far

        # Sieve to calculate SPF for numbers from 2 to n_len
        for i in range(2, n_len + 1):
            if spf[i] == 0: # i is a prime, as it hasn't been marked by a smaller prime
                spf[i] = i
                primes.append(i)

            # For each prime p, mark multiples of p.
            # Optimization: if p > spf[i], then i * p has already been marked by spf[i] (which is smaller than p).
            # So, we only need to mark with primes p <= spf[i].
            for p in primes:
                if p > spf[i] or i * p > n_len:
                    break
                spf[i * p] = p  # Smallest prime factor of i * p is p

        # Compute square-free part of all indices from 1 to n_len
        # sf_val[k] stores the square-free part of k.
        sf_val = [0] * (n_len + 1)  # sf_val[0] is unused.

        # sf_val[1] must be 1. Since n_len >= 1, this is always safe.
        sf_val[1] = 1   # Base case: square-free part of 1 is 1.

        # Calculate sf_val[i] using a DP-like approach based on SPF.
        # This relies on sf_val[j] for j < i already being computed.
        for i in range(2, n_len + 1):
            # Smallest prime factor of i
            p = spf[i]
            # i / p
            i_div_p = i // p

            # If p also divides i_div_p, it means p*p was a factor of i.
            # sf_val[12] should be sf_val[12 / (2*2)] = sf_val[3].
            # So, sf_val[i] = sf_val[ (i/p) / p ].
            if i_div_p % p == 0:
                sf_val[i] = sf_val[i_div_p // p]
            # Else, p was a factor of i with exponent 1 (or any odd exponent for p in prime factorization of i).
            # sf_val[6] should be sf_val[6/2] * 2 = sf_val[3] * 2.
            # So, sf_val[i] = sf_val[i/p] * p.
            else:
                sf_val[i] = sf_val[i_div_p] * p

        # Group sums of elements by the square-free part of their 1-based index
        square_free_map = defaultdict(int)
        # Iterate 1-based indices: 1, 2, ..., n_len
        for k in range(1, n_len + 1):
            s = sf_val[k]   # Square-free part of index k
            # nums is 0-indexed, problem indices are 1-based
            square_free_map[s] += nums[k - 1]

        # Find the maximum sum among all groups
        # Since n_len >= 1 (from constraints), index 1 exists. sf_val[1]=1.
        # nums[0] will be part of the sum for square_free_map[1].
        # Thus, square_free_map.values() will not be empty.
        # Constraints also state nums[i] >= 1, so all sums are positive.

        return max(square_free_map.values())