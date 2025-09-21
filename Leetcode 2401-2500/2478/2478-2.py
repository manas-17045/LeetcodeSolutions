# Leetcode 2478: Number of Beautiful Partitions
# https://leetcode.com/problems/number-of-beautiful-partitions/
# Solved on 21st of September, 2025
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        """
        Calculates the number of beautiful partitions of a string `s`.

        Args:
            s (str): The input string consisting of digits.
            k (int): The number of partitions required.
            minLength (int): The minimum length of each partition.

        Returns:
            int: The number of beautiful partitions.
        """
        MOD = 10**9 + 7
        n = len(s)
        prime_digits = {'2', '3', '5', '7'}

        # Quick impossible checks
        if s[0] not in prime_digits:
            return 0
        if s[-1] in prime_digits:
            return 0
        if k * minLength > n:
            return 0

        is_cut_after = [False] * n
        for p in range(n - 1):
            if (s[p] not in prime_digits) and (s[p + 1] in prime_digits):
                is_cut_after[p] = True

        dp_prev = [0] * n

        start = 0
        for i in range(minLength - 1, n):
            if s[i] not in prime_digits:
                dp_prev[i] = 1

        # Iterate layers t = 2...k
        for part in range(2, (k + 1)):
            # Build prefix sums
            pref = [0] * n
            # multiply by is_cut_after because we can only start a new segment after a valid cut
            pref[0] = (dp_prev[0] * (1 if is_cut_after[0] else 0)) % MOD
            for idx in range(1, n):
                add = dp_prev[idx] * (1 if is_cut_after[idx] else 0)
                pref[idx] = (pref[idx - 1] + add) % MOD

            dp_curr = [0] * n
            min_end = part * minLength - 1
            # We only need to consider i form min_end to (n - 1).
            for i in range(min_end, n):
                if s[i] in prime_digits:
                    # Segment must end with non-prime
                    continue
                j = i - minLength
                if j >= 0:
                    dp_curr[i] = pref[j]
                else:
                    dp_curr[i] = 0
            dp_prev = dp_curr

        return dp_prev[n - 1] % MOD