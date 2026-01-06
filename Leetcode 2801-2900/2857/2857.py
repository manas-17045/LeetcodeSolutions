# Leetcode 2857: Count Pairs of Points With Distance K
# https://leetcode.com/problems/count-pairs-of-points-with-distance-k/
# Solved on 6th of January, 2026
class Solution:
    def countPairs(self, coordinates: list[list[int]], k: int) -> int:
        """
        Counts the number of pairs of points (p1, p2) such that the XOR sum of their coordinates equals k.
        That is, (p1.x ^ p2.x) + (p1.y ^ p2.y) == k.

        Args:
            coordinates: A list of points, where each point is represented as [x, y].
            k: The target XOR sum distance.
        Returns:
            The number of such pairs.
        """

        pairCount = 0
        pointMap = {}

        for x, y in coordinates:
            for diffX in range(k + 1):
                targetX = x ^ diffX
                targetY = y ^ (k - diffX)
                matchCount = pointMap.get((targetX, targetY))

                if matchCount:
                    pairCount += matchCount

            currentPoint = (x, y)
            pointMap[currentPoint] = pointMap.get(currentPoint, 0) + 1

        return pairCount