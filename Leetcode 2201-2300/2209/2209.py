# Leetcode 3309: Minimum White Tiles After Covering With Carpets
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/
# Solved on 11th of December, 2025
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        """
        Calculates the minimum number of white tiles remaining after covering with carpets.

        Args:
            floor (str): A binary string representing the floor, where '1' is a white tile and '0' is a black tile.
            numCarpets (int): The number of carpets available.
            carpetLen (int): The length of each carpet.
        Returns:
            int: The minimum number of white tiles remaining.
        """
        numTiles = len(floor)
        if numCarpets * carpetLen >= numTiles:
            return 0

        dp = [0] * (numTiles + 1)
        for i in range(1, numTiles + 1):
            dp[i] = dp[i - 1] + int(floor[i - 1])

        for i in range(numCarpets):
            newDp = [0] * (numTiles + 1)
            for j in range(1, numTiles + 1):
                skipOption = newDp[j - 1] + int(floor[j - 1])
                coverOption = dp[max(0, j - carpetLen)]
                newDp[j] = min(skipOption, coverOption)
            dp = newDp

        return dp[numTiles]