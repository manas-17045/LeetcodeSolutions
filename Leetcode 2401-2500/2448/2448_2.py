# Leetcode 2448: Minimum Cost to Make Array Equal
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/
# Solved on 13th of July, 2025
class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        """
        Calculates the minimum cost to make all elements in `nums` equal to a single value.

        The cost to change an element `nums[i]` to a target value `x` is `abs(nums[i] - x) * cost[i]`.
        The goal is to find a target value `x` that minimizes the total cost.

        This problem can be rephrased as finding a weighted median.
        The solution iterates through each `nums[i]` as a potential target value `t`.
        For each `t`, it calculates the total cost:
        Sum of `(t - nums[j]) * cost[j]` for `nums[j] < t`
        + Sum of `(nums[k] - t) * cost[k]` for `nums[k] > t`.

        The `nums` and `cost` arrays are first paired and sorted by `nums` values.
        Prefix sums of `cost` and `num * cost` are precomputed to efficiently calculate
        the costs for elements to the left and right of the current target `t`.

        Args:
            nums: A list of integers.
            cost: A list of integers, where `cost[i]` is the cost associated with `nums[i]`.
        """
        # Pair up and sort by nums
        A = sorted(zip(nums, cost), key=lambda x: x[0])
        n = len(A)

        # Extract sorted nums and costs
        sorted_nums = [a for a, _ in A]
        sorted_cost = [c for _, c in A]

        # Prefix sums of cost and of num * cost
        prefix_cost = [0] * (n + 1)
        prefix_numcost = [0] * (n + 1)
        for i in range(n):
            prefix_cost[i + 1] = prefix_cost[i] + sorted_cost[i]
            prefix_numcost[i + 1] = prefix_numcost[i] + sorted_nums[i] * sorted_cost[i]

        total_cost = prefix_cost[n]
        total_numcost = prefix_numcost[n]

        ans = float('inf')

        for i in range(n):
            t = sorted_nums[i]
            left_cost = prefix_cost[i]
            left_numcost = prefix_numcost[i]
            right_cost = total_cost - prefix_cost[i + 1]
            right_numcost = total_numcost - prefix_numcost[i + 1]

            cur = t * left_cost - left_numcost + right_numcost - t * right_cost
            if cur < ans:
                ans = cur

        return int(ans)