# Leetcode 3443: Maximum Manhattan Distance After K Changes
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
# Solved on 20th of June, 2025

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """
        Calculates the maximum possible Manhattan distance from the origin after
        following a sequence of moves, with the ability to change up to k moves.

        Args:
            s: A string representing the sequence of moves ('N', 'S', 'E', 'W').
            k: The maximum number of moves that can be changed.

        Returns: The maximum possible Manhattan distance.
        """
        n = len(s)
        overallMaxManhattanDistance = -float('inf')

        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        move_deltas = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        for A_coeff, B_coeff in directions:
            suboptimalMoveIndices = []
            for j in range(n):
                dx, dy = move_deltas[s[j]]
                contribution = A_coeff * dx + B_coeff * dy
                if contribution == -1:
                    suboptimalMoveIndices.append(j)

            numChangesToMake = min(k, len(suboptimalMoveIndices))

            indicesToChange = set()
            for i in range(numChangesToMake):
                indicesToChange.add(suboptimalMoveIndices[i])

            currentPathSum = 0
            maxSumForThisDirection = -float('inf')

            for t in range(n):
                dx, dy = move_deltas[s[t]]
                baseContribution = A_coeff * dx + B_coeff * dy

                if t in indicesToChange:
                    # This move was suboptimal (baseContribution -1), changed to optimal (contribution 1)
                    currentPathSum += 1
                else:
                    currentPathSum += baseContribution

                # Max sum at any point t for this direction
                if currentPathSum > maxSumForThisDirection:
                    maxSumForThisDirection = currentPathSum

            # Update overall max distance found
            if maxSumForThisDirection > overallMaxManhattanDistance:
                overallMaxManhattanDistance = maxSumForThisDirection

        return overallMaxManhattanDistance