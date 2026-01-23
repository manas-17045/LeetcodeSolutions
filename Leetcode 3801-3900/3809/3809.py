# Leetcode 3809: Best Reachable Tower
# https://leetcode.com/problems/best-reachable-tower/
# Solved on 23rd of January, 2026
class Solution:
    def bestTower(self, towers: list[list[int]], center: list[int], radius: int) -> list[int]:
        """
        Finds the tower with the highest quality within a given Manhattan distance from a center point.
        In case of a tie in quality, the tower with the smallest x-coordinate is chosen.
        If there's still a tie, the tower with the smallest y-coordinate is chosen.

        :param towers: A list of towers, where each tower is represented as [x, y, quality].
        :param center: The center point [centerX, centerY].
        :param radius: The maximum Manhattan distance from the center.
        :return: The coordinates [x, y] of the best reachable tower.
        """
        bestCoordinates = [-1, -1]
        maxQuality = -1
        centerX, centerY = center

        for towerX, towerY, quality in towers:
            distance = abs(towerX - centerX) + abs(towerY - centerY)

            if distance <= radius:
                if quality > maxQuality:
                    maxQuality = quality
                    bestCoordinates = [towerX, towerY]
                elif quality == maxQuality:
                    if towerX < bestCoordinates[0] or (towerX == bestCoordinates[0] and towerY < bestCoordinates[1]):
                        bestCoordinates = [towerX, towerY]

        return bestCoordinates