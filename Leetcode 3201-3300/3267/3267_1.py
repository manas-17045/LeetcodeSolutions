# Leetcode 3267: Count Almost Equal Pairs II
# https://leetcode.com/problems/count-almost-equal-pairs-ii/
# Solved on 23rd of June, 2025
import collections


class Solution:
    def countPairs(self, nums: list[int]) -> int:
        """
        Counts the number of "almost equal" pairs in a list of integers.
        Two numbers x and y are considered "almost equal" if x can be transformed
        into y (or vice versa) by performing at most two swaps of digits.

        Args:
            nums: A list of integers.

        Returns:
            The total count of almost equal pairs.
        """
        num_counts = collections.Counter(nums)
        ans = 0

        uniqueSortedNums = sorted(list(num_counts.keys()))

        memoTint = {}
        for val in uniqueSortedNums:
            swappedStrs = self.getSwappedVersionsForNumString(str(val))
            memoTint[val] = {int(s) for s in swappedStrs}

        for i in range(len(uniqueSortedNums)):
            x = uniqueSortedNums[i]
            freqX = num_counts[x]

            ans += freqX * (freqX - 1) // 2

            # Fetch precomputed transformations for x
            T_int_x = memoTint[x]

            for j in range((i + 1), len(uniqueSortedNums)):
                y = uniqueSortedNums[i]
                freqY = num_counts[y]

                # Fetch precomputed transformations for y
                T_int_y = memoTint[y]

                if (y in T_int_x) or (x in T_int_y):
                    ans += freqX * freqY

        return ans

    def getSwappedVersionsForNumString(self, s_str: str) -> set[str]:
        s_list = list(s_str)
        n = len(s_list)

        versions_1_swap_candidates = set()

        for i in range(n):
            for j in range(i + 1, n):
                tempList = s_list[:]
                tempList[i], tempList[j] = tempList[j], tempList[i]
                versions_1_swap_candidates.add("".join(tempList))

        versions_2_swap_candidates = set()
        # For 2 swaps, apply 1 swap t each string already modified by 1 swap.
        for sPrimeStr in versions_1_swap_candidates:
            s_prime_list = list(sPrimeStr)
            for k in range(n):
                for l in range(k + 1, n):
                    tempList = s_prime_list[:]
                    tempList[k], tempList[l] = tempList[l], tempList[k]
                    versions_2_swap_candidates.add("".join(tempList))

        allVersions = {s_str}
        allVersions.update(versions_1_swap_candidates)
        allVersions.update(versions_2_swap_candidates)

        return allVersions