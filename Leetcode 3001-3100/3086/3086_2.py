# Leetcode 3086: Minimum Moves to Pick K Ones
# https://leetcode.com/problems/minimum-moves-to-pick-k-ones/
# Solved on 27th of June, 2025
class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        """
        Calculates the minimum moves required to pick k ones.

        The problem asks for the minimum number of moves to make k ones
        adjacent to a chosen central position. A move is defined as:
        1. Changing a 0 to a 1: costs 2 moves. This can be done `maxChanges` times.
        2. Moving a 1 to an adjacent position: costs 1 move.

        The strategy involves iterating through possible numbers of existing ones
        (`onesByTwo`) that are picked directly (costing 0 moves to change, but
        potentially movement cost). The remaining `k - onesByTwo` ones must be
        obtained by changing zeros to ones, each costing 2 moves.

        The core idea is to use a sliding window approach on the `oneIndices`
        to find the minimum cost to gather `onesByTwo` ones, and combine this
        with the cost of changing zeros to ones.
        """
        # Collect positions of 1s
        one_indices = [i for i, v in enumerate(nums) if v == 1]
        n1 = len(one_indices)

        # Prefix sums of positions
        prefix = [0] * (n1 + 1)
        for i in range(n1):
            prefix[i + 1] = prefix[i] + one_indices[i]

        # We must pick k ones.
        min_x = max(0, (k - maxChanges))
        max_x = min(k, (min_x + 3), n1)

        ans = float('inf')

        # Try every feasible x in [min_x...max_x]
        for x in range(min_x, max_x + 1):
            cost1 = (k - x) * 2

            # Slide a window of size x over the one_indices
            for l in range(0, (n1 - x + 1)):
                r = l + x

                m1 = (l + r) // 2
                m2 = (l + r + 1) // 2

                cost2 = (prefix[r] - prefix[m2]) - (prefix[m1] - prefix[l])

                ans = min(ans, (cost1 + cost2))

        return ans