# Leetcode 1840: Maximum Building Height
# https://leetcode.com/problems/maximum-building-height/
# Solved on 22nd of July, 2025
class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        """
        Calculates the maximum possible height of any building given a set of restrictions.

        Args:
            n (int): The total number of buildings, from 1 to n.
            restrictions (list[list[int]]): A list of restrictions, where each restriction
                                             is [building_index, max_height].
        Returns:
            int: The maximum possible height of any building.
        """
        # Always enforce that building 1 has height 0
        has_last = False
        new_rests = [[1, 0]]
        for x, h in restrictions:
            if x == 1:
                continue
            if x == n:
                has_last = True
            new_rests.append([x, h])

        # If there's no restriction at n, we can always grow up to n - 1 there
        if not has_last:
            new_rests.append([n, n - 1])

        # Sort by building index
        new_rests.sort(key=lambda r: r[0])

        # Forward pass
        for i in range(1, len(new_rests)):
            dist = new_rests[i][0] - new_rests[i - 1][0]
            new_rests[i][1] = min(new_rests[i][1], new_rests[i - 1][1] + dist)

        # Backward pass
        for i in range(len(new_rests) - 2, -1, -1):
            dist = new_rests[i + 1][0] - new_rests[i][0]
            new_rests[i][1] = min(new_rests[i][1], new_rests[i + 1][1] + dist)

        # Compute overall max.
        ans = 0
        # Take max over restriction heights
        for _, h in new_rests:
            ans = max(ans, h)

        # For each gap, the best you can do is the midpoint of the two adjusted endpoints
        for i in range(len(new_rests) - 1):
            x1, h1 = new_rests[i]
            x2, h2 = new_rests[i + 1]
            d = x2 - x1
            peak = (h1 + h2 + d) // 2
            ans = max(ans, peak)

        return ans