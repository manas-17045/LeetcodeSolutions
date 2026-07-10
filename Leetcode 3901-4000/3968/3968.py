# Leetcode 3968: Maximum Manhattan Distance After All Moves
# https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/
# Solved on 10th of July, 2026
class Solution:
    def maxDistance(self, moves: str) -> int:
        """
        Returns the maximum Manhattan distance after replacing each wildcard with
        'L', 'R', 'U', or 'D'.
        
        @param moves The string of moves.
        @return The maximum Manhattan distance.
        """
        netX = moves.count('R') - moves.count('L')
        netY = moves.count('U') - moves.count('D')
        wildcardCount = moves.count('_')
        return abs(netX) + abs(netY) + wildcardCount