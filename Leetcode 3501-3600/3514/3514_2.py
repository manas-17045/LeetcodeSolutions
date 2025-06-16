# Leetcode 3514: Number of Unique XOR Triplets II
# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/
# Solved on 16th of June, 2025

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        """
        Finds the number of unique XOR values of triplets (i, j, k) where i < j < k
        and nums[i] ^ nums[j] ^ nums[k] is the XOR value.

        This solution uses a dynamic programming approach to efficiently track
        possible XOR values of pairs and then combines them with the current element
        to find triplet XORs.

        Args:
            nums: A list of integers.
        """
        if not nums:
            return 0

        MAX_XOR = 2048

        pairs_xor = [False] * MAX_XOR
        pair_vals = []

        T = [False] * MAX_XOR

        seen = {}
        distinct_vals = []

        for c in nums:
            # Build all new pairs ending at this index j with c = nums[j]
            if not pairs_xor[0]:
                pairs_xor[0] = True
                pair_vals.append(0)

            # For each previously seen distinct x, mark x^c
            for x in distinct_vals:
                v = x ^ c
                if not pairs_xor[v]:
                    pairs_xor[v] = True
                    pair_vals.append(v)

            # Now, c is the third index k: combine it with *all* pairs so far
            for pv in pair_vals:
                T[pv ^ c]= True

            # Record c into seen[] if new
            if c not in seen:
                seen[c] = 1
                distinct_vals.append(c)
            else:
                seen[c] += 1

        # Return how many distinct triplet XORS we found
        return sum(T)