# Leetcode 2973: Find Number of Coins to Place in Tree Nodes
# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/
# Solved on 23rd of May, 2025
import collections


class Solution:
    def placedCoins(self, edges: list[list[int]], cost: list[int]) -> list[int]:
        """
        Calculates the maximum number of coins that can be placed at each node
        in a tree, based on the costs of the nodes in its subtree.

        For each node u, the number of coins is determined as follows:
        - If the subtree rooted at u has fewer than 3 nodes, 1 coin is placed.
        - If the subtree rooted at u has 3 or more nodes, the number of coins
          is the maximum of 0 and the largest product of three distinct node costs
          within the subtree. This largest product can be either the product of
          the three largest costs or the product of the two smallest costs and
          the largest cost (to handle negative costs).

        Args:
            edges: A list of lists representing the tree edges.
            cost: A list of integers where cost[i] is the cost of node i.

        Returns:
            A list of integers where ans[i] is the number of coins placed at node i.
        """
        n = len(cost)
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = [0] * n

        # dfs returns a pair: (sorted_list_of_extreme_costs, subtree_size)
        # sorted_list_of_extreme_costs contains costs from the current node's subtree:
        #   - if number of nodes in subtree <= 5, it contains all of their costs, sorted.
        #   - if number of nodes in subtree > 5, it contains the 2 smallest and 3 largest costs, sorted.
        def dfs(u: int, p: int) -> tuple[list[int], int]:
            # current_extreme_costs will store the sorted list of extreme costs for the subtree rooted at u.
            # Initially, it only has cost[u].
            current_extreme_costs: list[int] = [cost[u]]
            subtree_size: int = 1

            for v in adj[u]:
                if v == p:
                    continue

                child_extreme_costs, child_subtree_size = dfs(v, u)
                subtree_size += child_subtree_size

                # Merge child_extreme_costs into current_extreme_costs.
                # current_extreme_costs has at most 5 elements (or fewer if the processed part of subtree was small).
                # child_extreme_costs has at most 5 elements.
                # So, temp_combined has at most 5 (from current) + 5 (from child) = 10 elements. Sorting is fast.
                temp_combined = sorted(current_extreme_costs + child_extreme_costs)

                if len(temp_combined) <= 5:
                    current_extreme_costs = temp_combined
                else:
                    # Keep 2 smallest and 3 largest.
                    # e.g. if len(temp_combined) = 6, elements indexed 0..5.
                    # temp_combined[:2] -> elements at indices 0, 1.
                    # temp_combined[len(temp_combined)-3:] -> elements at indices 3, 4, 5.
                    # The resulting list of 5 elements is guaranteed to be sorted.
                    current_extreme_costs = temp_combined[:2] + temp_combined[len(temp_combined) - 3:]

            # Calculate ans[u]
            if subtree_size < 3:
                ans[u] = 1
            else:
                # current_extreme_costs is sorted. Its length 'k' will be min(subtree_size, 5).
                # Since subtree_size >= 3, k is guaranteed to be >= 3.
                k = len(current_extreme_costs)

                # Candidate 1: product of 3 largest values
                prod_3_largest = current_extreme_costs[k - 1] * current_extreme_costs[k - 2] * current_extreme_costs[k - 3]

                # Candidate 2: product of 2 smallest values and 1 largest values
                prod_2_smallest_1_largest = current_extreme_costs[0] * current_extreme_costs[1] * current_extreme_costs[k - 1]

                max_prod_val = max(prod_3_largest, prod_2_smallest_1_largest)

                if max_prod_val < 0:
                    ans[u] = 0
                else:
                    ans[u] = max_prod_val

            return current_extreme_costs, subtree_size

        dfs(0, -1)  # Start DFS from root 0, with no parent (-1).
        return ans