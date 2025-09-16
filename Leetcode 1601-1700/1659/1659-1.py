# Leetcode 1659: Maximize Grid Happiness
# https://leetcode.com/problems/maximize-grid-happiness/
# Solved on 16th of September, 2025
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        """
        Calculates the maximum possible grid happiness.

        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.
            introvertsCount (int): The total number of introverts available.
            extrovertsCount (int): The total number of extroverts available.
        Returns:
            int: The maximum grid happiness achievable.
        """
        if m < n:
            m, n = n, m

        powersOfThree = [1] * (n + 1)
        for i in range(1, n + 1):
            powersOfThree[i] = powersOfThree[i - 1] * 3

        maskSize = powersOfThree[n]

        maskToConfig = []
        for i in range(maskSize):
            mask = i
            config = []
            for _ in range(n):
                config.append(mask % 3)
                mask //= 3
            maskToConfig.append(tuple(config))

        maskIntroverts = [config.count(1) for config in maskToConfig]
        maskExtroverts = [config.count(2) for config in maskToConfig]

        interactionCost =[[0, 0, 0,], [0, -60, -10], [0, -10, 40]]

        internalHappiness = []
        for maskVal, config in enumerate(maskToConfig):
            happiness = 0
            happiness += maskIntroverts[maskVal] * 120
            happiness += maskExtroverts[maskVal] * 40
            for c in range(n - 1):
                p1, p2 = config[c], config[c + 1]
                if p1 > 0 and p2 > 0:
                    happiness += interactionCost[p1][p2]
            internalHappiness.append(happiness)

        interactionHappiness = [[0] * maskSize for _ in range(maskSize)]
        for mask1, config1 in enumerate(maskToConfig):
            for mask2, config2 in enumerate(maskToConfig):
                happiness = 0
                for c in range(n):
                    p1, p2 = config1[c], config2[c]
                    if p1 > 0 and p2 > 0:
                        happiness += interactionCost[p1][p2]
                interactionHappiness[mask1][mask2] = happiness

        dp = [[[-1] * maskSize for _ in range(extrovertsCount + 1)] for _ in range(introvertsCount + 1)]

        for mask in range(maskSize):
            introvertsInMask = maskIntroverts[mask]
            extrovertsInMask = maskExtroverts[mask]
            if introvertsInMask <= introvertsCount and extrovertsInMask <= extrovertsCount:
                dp[introvertsInMask][extrovertsInMask][mask] = internalHappiness[mask]

        for r in range(1, m):
            newDp = [[[-1] * maskSize for _ in range(extrovertsCount + 1)] for _ in range(introvertsCount + 1)]

            for prevIntroverts in range(introvertsCount + 1):
                for prevExtroverts in range(extrovertsCount + 1):
                    for prevMask in range(maskSize):
                        if dp[prevIntroverts][prevExtroverts][prevMask] == -1:
                            continue

                        for mask in range(maskSize):
                            introvertsInMask = maskIntroverts[mask]
                            extrovertsInMask = maskExtroverts[mask]

                            newIntroverts = prevIntroverts + introvertsInMask
                            newExtroverts = prevExtroverts + extrovertsInMask

                            if newIntroverts <= introvertsCount and newExtroverts <= extrovertsCount:
                                currentVal = dp[prevIntroverts][prevExtroverts][prevMask] + internalHappiness[mask] + interactionHappiness[mask][prevMask]

                                if currentVal > newDp[newIntroverts][newExtroverts][mask]:
                                    newDp[newIntroverts][newExtroverts][mask] = currentVal

            dp = newDp

        maxHappiness = 0
        for i in range(introvertsCount + 1):
            for e in range(extrovertsCount + 1):
                for mask in range(maskSize):
                    if dp[i][e][mask] > maxHappiness:
                        maxHappiness = dp[i][e][mask]

        return maxHappiness