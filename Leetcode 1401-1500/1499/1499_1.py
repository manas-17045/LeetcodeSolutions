# Leetcode 1499: Max Value of Equation
# https://leetcode.com/problems/max-value-of-equation/
# Solved on 19th of July, 2025
import collections


class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        """
        Finds the maximum value of the equation yi + yj + |xi - xj| for given points and k.
        :param points: A list of points, where each point is [xi, yi].
        :param k: An integer representing the maximum allowed difference between xi and xj.
        :return: The maximum value of the equation.
        """
        deque = collections.deque()
        maxValue = float('-inf')

        for j in range(len(points)):
            xj = points[j][0]
            yj = points[j][1]

            while deque and xj - points[deque[0]][0] > k:
                deque.popleft()

            if deque:
                i = deque[0]
                xi = points[i][0]
                yi = points[i][1]
                currentVal = xj + yj + yi - xi
                maxValue = max(maxValue, currentVal)

            yMinusX = yj - xj
            while deque and yMinusX >= points[deque[-1]][1] - points[deque[-1]][0]:
                deque.pop()

            deque.append(j)

        return maxValue