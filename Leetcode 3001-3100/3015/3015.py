# Leetcode 3015: Count the Number of Houses at a Certain Distance I
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/
# Solved on 4th of January, 2026
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        """
        Calculates the number of pairs of houses at a certain distance from each other.

        The houses are numbered from 1 to n. There's a special connection between house x and house y.
        The distance between two houses is the minimum number of steps to go from one house to another.

        Args:
            n: The total number of houses.
            x: The first house in the special connection.
            y: The second house in the special connection.

        Returns:
            A list of integers where counts[k] is the number of pairs of houses that have a distance of k+1.
        """
        counts = [0] * n

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                directDistance = abs(i - j)
                distanceViaX = abs(i - x) + 1 + abs(j - y)
                distanceViaY = abs(i - y) + 1 + abs(j - x)

                minimumDistance = min(directDistance, distanceViaX, distanceViaY)
                counts[minimumDistance - 1] += 2

        return counts