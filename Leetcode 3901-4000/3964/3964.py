# Leetcode 3964: Minimum Lights to Illuminate a Road
# https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/
# Solved on 9th of July, 2026
class Solution:
    def minLights(self, lights: list[int]) -> int:
        """:
        Calculates the minimum number of additional lights needed to illuminate a road.
        
        :param lights: An array of integers where `lights[i]` represents the illumination range of a
                light at position `i`. A non-positive value indicates no light at that position.
        
        :return: The minimum number of additional lights required to illuminate the entire road.
        """
        n = len(lights)
        diffArray = [0] * (n + 1)
        for i in range(n):
            if lights[i] > 0:
                leftIndex = max(0, i - lights[i])
                rightIndex = min(n - 1, i + lights[i])
                diffArray[leftIndex] += 1
                diffArray[rightIndex + 1] -= 1

        isVisible = [False] * n
        currentSum = 0
        for i in range(n):
            currentSum += diffArray[i]
            if currentSum > 0:
                isVisible = True

        minBulbs = 0
        currentIndex = 0
        while currentIndex < n:
            if not isVisible[currentIndex]:
                minBulbs += 1
                currentIndex += 2
            else:
                currentIndex += 1
                
        return minBulbs