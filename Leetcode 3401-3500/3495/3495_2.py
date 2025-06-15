# Leetcode 3495: Minimum Operations to Make Array Elements Zero
# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
# Solved on 14th of June, 2025

class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        """
        Calculates the minimum number of operations to cover all numbers within given query ranges.

        An operation can cover two numbers. The cost of covering a number 'n' is related to its
        position in a sequence of bands defined by powers of 4. Specifically, a number 'n'
        in the range [4^(k-1), 4^k - 1] requires 'k' "picks" to be covered. An operation
        can cover two "picks".

        The function first pre-calculates the bands and their corresponding 'k' values.
        Then, for each query [l, r], it calculates the total number of "picks" required
        by summing the picks for the overlapping parts of the query range with each band.
        Finally, it calculates the minimum operations for the query as ceil(total_picks / 2)
        and sums these up for all queries.

        :param queries: A list of lists, where each inner list is a query [l, r].
        :return: The total minimum number of operations for all queries.
        """
        bands = []
        pow4 = 1
        for k in range(1, 20):
            L = pow4
            pow4 *= 4
            R = pow4 - 1
            bands.append((L, R, k))
            if L > 10**9:
                break

        total_ops = 0
        for l, r in queries:
            picks = 0
            for L, R, k in bands:
                if r < L or R < l:
                    continue
                # Overlap length
                picks += k * (min(r, R) - max(l, L) + 1)
            # each operation handles two "picks", so ceil(picks/2)
            total_ops += (picks + 1) // 2

        return total_ops