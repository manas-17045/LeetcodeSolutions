# Leetcode 1499: Max Value of Equation
# https://leetcode.com/problems/max-value-of-equation/
# Solved on 19th of July, 2025
from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        """
        Finds the maximum value of the equation yi + yj + |xi - xj| for given points and a constraint k.

        Args:
            points: A list of lists, where each inner list [xi, yi] represents a point.
            k: An integer representing the maximum allowed difference between xi and xj.
        Returns:
            The maximum value of the equation.
        """
        # deque will store pairs (yi - xi, xi), in decreasing order of yi - xi
        dq = deque()
        res = float('-inf')

        for xj, yj in points:
            # Remove points from the front that are more than k away in x
            while dq and xj - dq[0][1] > k:
                dq.popleft()

            # If deque not empty, the front has the maximum (yi - xi) among valid i
            if dq:
                best_y_minus_x, xi = dq[0]
                res = max(res, best_y_minus_x + yj + xj)

            # Now insert current point (yj - xj, xj) into deque,
            # maintaining the deque in decreasing order of (yi - xi)
            curr = yj - xj
            while dq and curr >= dq[-1][0]:
                dq.pop()
            dq.append((curr, xj))

        return res