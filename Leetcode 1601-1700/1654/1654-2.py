# Leetcode 1654: Minimum Jumps to Reach Home
# https://leetcode.com/problems/minimum-jumps-to-reach-home/
# Solved on 1st of September, 2025
from collections import deque


class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        """
        Calculates the minimum number of jumps required to reach a target position x.

        Args:
            forbidden (list[int]): A list of positions that cannot be landed on.
            a (int): The distance of a forward jump.
            b (int): The distance of a backward jump.
            x (int): The target position.

        Returns:
            int: The minimum number of jumps, or -1 if x cannot be reached.
        """
        # Quick answer
        if x == 0:
            return 0

        forbidden_set = set(forbidden)

        max_forbidden = max(forbidden) if forbidden else 0
        limit = max(max_forbidden, x) + a + b + 10

        visited_forward = [False] * (limit + 1)
        visited_backward = [False] * (limit + 1)

        dq = deque()
        dq.append((0, False, 0))
        visited_forward[0] = False

        while dq:
            pos, last_was_backward, steps = dq.popleft()

            # Try forward jump
            nf = pos + a
            if nf == x:
                return steps + 1
            if nf <= limit and not visited_forward[nf] and nf not in forbidden_set:
                visited_forward[nf] = True
                dq.append((nf, False, steps + 1))

            # Try backward jump
            nb = pos - b
            if not last_was_backward:
                if nb == x:
                    return steps + 1
                if nb >= 0 and not visited_backward[nb] and nb not in forbidden_set:
                    visited_backward[nb] = True
                    dq.append((nb, True, steps + 1))

        return -1