# Leetcode 3267: Count Almost Equal Pairs II
# https://leetcode.com/problems/count-almost-equal-pairs-ii/
# Solved on 23rd of June, 2025
import itertools
from collections import Counter


class Solution:
    def countPairs(self, nums: list[int]) -> int:
        """
        Counts the number of pairs (i, j) such that i < j and nums[i] and nums[j]
        are "similar". Two numbers are similar if one can be obtained from the other
        by at most two swaps of digits.

        The approach involves:
        1. Converting numbers to zero-padded strings to handle varying lengths.
        2. Grouping numbers by their digit multiset (sorted string representation).
           Numbers in different groups cannot be similar.
        3. Within each group, enumerating pairs:
           - Identical pairs (0 swaps).
           - Pairs reachable by one swap.
           - Pairs reachable by exactly two swaps (excluding those reachable by one swap).
        """
        # Stringify and zero-pad
        strs = [str(x) for x in nums]
        M = max(map(len, strs))
        padded = [s.zfill(M) for s in strs]

        # Group by digit-multiset
        groups = {}
        for s in padded:
            key = ''.join(sorted(s))
            groups.setdefault(key, []).append(s)

        # Precompute all index-pairs for swapping
        pairs = list(itertools.combinations(range(M), 2))

        total = 0
        for bucket in groups.values():
            freq = Counter(bucket)
            # Zero-swap (identical) pairs
            for s, c in freq.items():
                total += c * (c - 1) // 2

            # Prepare for one/two swap enumeration
            uniq = sorted(freq.keys())
            lookup = set(uniq)

            for s in uniq:
                fs = freq[s]
                # Build sets of neighbors
                oneSet = set()
                arr = list(s)
                # One-swap
                for i, j in pairs:
                    arr[i], arr[j] = arr[j], arr[i]
                    oneSet.add(''.join(arr))
                    arr[i], arr[j] = arr[j], arr[i]

                # Count one-swap neighbors within group, s < t to avoid duplicates
                for t in oneSet:
                    if t in freq and s < t:
                        total += fs * freq[t]

                # Two-swap (nested)
                twoSet = set()
                for i, j in pairs:
                    arr[i], arr[j] = arr[j], arr[i]
                    for k, l in pairs:
                        arr[k], arr[l] = arr[l], arr[k]
                        twoSet.add(''.join(arr))
                        arr[k], arr[l] = arr[l], arr[k]
                    arr[i], arr[j] = arr[j], arr[i]

                # Remove any one-swap neighbors or original
                twoExact = twoSet - oneSet
                if s in twoExact:
                    twoExact.remove(s)

                # Count two-swap-only neighbors
                for t in twoExact:
                    if t in freq and s < t:
                        total += fs * freq[t]

        return total