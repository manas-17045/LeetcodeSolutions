# Leetcode 3648: Minimum Sensors to Cover Grid
# https://leetcode.com/problems/minimum-sensors-to-cover-grid/
# Solved on 29th of December, 2025
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        """
        Calculates the minimum number of sensors required to cover an n x m grid.

        Args:
            n (int): The number of rows in the grid.
            m (int): The number of columns in the grid.
            k (int): The coverage radius of each sensor.
        Returns:
            int: The minimum number of sensors needed.
        """
        sensorCoverage = 2 * k + 1
        sensorsNeededForRows = (n + sensorCoverage - 1) // sensorCoverage
        sensorsNeededForCols = (m + sensorCoverage - 1) // sensorCoverage

        return sensorsNeededForRows * sensorsNeededForCols