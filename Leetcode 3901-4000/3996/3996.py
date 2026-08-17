# Leetcode 3996: Even Number of Knight Moves
# https://leetcode.com/problems/even-number-of-knight-moves/
# Solved on 17th of August, 2026
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        """
        Checks if the target can be reached from the start in an even number of moves.
        
        Args:
            start: The starting position of the knight.
            target: The target position of the knight.
        
        Returns:
            True if the target can be reached in an even number of moves, false otherwise.
        """
        startP = (start[0] + start[1]) % 2
        targetP = (target[0] + target[1]) % 2
        
        return startP == targetP