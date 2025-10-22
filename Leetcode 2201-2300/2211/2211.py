# Leetcode 2211: Count Collisions on a Road
# https://leetcode.com/problems/count-collisions-on-a-road/
# Solved on 22nd of October, 2025
class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        Counts the total number of collisions that will happen on a road.

        Args:
            directions (str): A string representing the initial directions of cars.
                              'L' for left, 'R' for right, 'S' for stationary.
        Returns:
            int: The total number of collisions.
        """
        n = len(directions)
        if n <= 1:
            return 0

        leftPointer = 0
        while leftPointer < n and directions[leftPointer] == 'L':
            leftPointer += 1

        rightPointer = n - 1
        while rightPointer >= 0 and directions[rightPointer] == 'R':
            rightPointer -= 1

        if leftPointer >= rightPointer:
            return 0

        collisionCount = 0
        for i in range(leftPointer, rightPointer + 1):
            if directions[i] != 'S':
                collisionCount += 1

        return collisionCount