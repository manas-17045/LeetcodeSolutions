# Leetcode 3443: Maximum Manhattan Distance After K Changes
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
# Solved on 20th of June, 2025

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """
        Calculates the maximum possible Manhattan distance from the origin after
        following a sequence of moves, with the ability to flip the direction
        of at most k moves.

        Args:
            s: A string representing the sequence of moves ('N', 'S', 'E', 'W').
            k: The maximum number of moves that can be flipped.

        Returns:
            The maximum possible Manhattan distance from the origin.
        """
        # Mapping moves to (dx, dy)
        d = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        # Our four sign-pairs (s_x, s_y)
        quads = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        # orig[q] = running sum of s_x*dx + s_y*dy in quad q
        orig = [0] * 4
        # cnt_bad[q] = how many steps so far had w_orig = -1 in quad q
        cnt_bad = [0] * 4

        ans = 0
        for c in s:
            dx, dy = d[c]
            # Update each quadrant
            for qi, (sx, sy) in enumerate(quads):
                w = (sx * dx) + (sy * dy)
                orig[qi] += w
                if w == -1:
                    cnt_bad[qi] += 1
                # Best with up to k flips is turning win(cn_bad, k) of those -1's to +1's -> gain 2 each
                candidate = orig[qi] + 2 * min(cnt_bad[qi], k)
                if candidate > ans:
                    ans = candidate
        return ans