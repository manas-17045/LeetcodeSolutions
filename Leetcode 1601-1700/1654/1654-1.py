# Leetcode 1654: Minimum Jumps to Reach Home
# https://leetcode.com/problems/minimum-jumps-to-reach-home/
# Solved on 1st of September, 2025
import collections


class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        """
        Finds the minimum number of jumps to reach a target position x.

        Args:
            forbidden (list[int]): A list of positions that cannot be visited.
            a (int): The distance of a forward jump.
            b (int): The distance of a backward jump.
            x (int): The target position to reach.
        Returns:
            int: The minimum number of jumps to reach x, or -1 if it's not possible.
        """
        maxVal = x
        if forbidden:
            maxVal = max(x, max(forbidden))

        limit = maxVal + a + b

        forbiddenSet = set(forbidden)
        queue = collections.deque([(0, 0, False)])
        visited = {(0, False)}

        while queue:
            currentPos, currentJumps, wasLastBackward = queue.popleft()

            if currentPos == x:
                return currentJumps

            nextForwardPos = currentPos + a
            if nextForwardPos <= limit and (nextForwardPos,
                                            False) not in visited and nextForwardPos not in forbiddenSet:
                visited.add((nextForwardPos, False))
                queue.append((nextForwardPos, currentJumps + 1, False))

            if not wasLastBackward:
                nextBackwardPos = currentPos - b
                if nextBackwardPos >= 0 and (nextBackwardPos,
                                             True) not in visited and nextBackwardPos not in forbiddenSet:
                    visited.add((nextBackwardPos, True))
                    queue.append((nextBackwardPos, currentJumps + 1, True))

        return -1