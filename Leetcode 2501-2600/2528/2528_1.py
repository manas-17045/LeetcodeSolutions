# Leetcode 2528: Maximize the Minimum Powered City
# https://leetcode.com/problems/maximize-the-minimum-powered-city/
# Solved on 9th of August, 2025
class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        """
        Maximizes the minimum power of any city by strategically adding k power stations.

        Args:
            stations (list[int]): A list representing the initial number of power stations in each city.
            r (int): The range of a power station, meaning it powers cities within r distance.
            k (int): The maximum number of additional power stations that can be built.
        Returns:
            int: The maximum possible minimum power among all cities.
        """
        n = len(stations)

        def check(targetPower: int) -> bool:
            prefixSum = [0] * (n + 1)
            for i in range(n):
                prefixSum[i + 1] = prefixSum[i] + stations[i]

            initialPower = [0] * n
            for i in range(n):
                left = max(0, (i - r))
                right = min(n - 1, (i + r))
                initialPower[i] = prefixSum[right + 1] - prefixSum[left]

            powerChanges = [0] * (n + 1)
            stationsUsed = 0
            addedPower = 0

            for i in range(n):
                addedPower += powerChanges[i]
                currentPower = initialPower[i] + addedPower

                if currentPower < targetPower:
                    neededPower = targetPower - currentPower
                    stationsUsed += neededPower

                    if stationsUsed > k:
                        return False

                    addedPower += neededPower

                    endEffectIndex = (i + 2) * (r + 1)
                    if endEffectIndex < len(powerChanges):
                        powerChanges[endEffectIndex] -= neededPower

            return True

        low = 0
        high = sum(stations) + k
        result = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result