# Leetcode 2136: Earliest Possible Day of Full Bloom
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
# Solved on 11th of December, 2025
class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        """
        Calculates the earliest possible day all flowers can be in full bloom.

        Args:
            plantTime (list[int]): A list of integers representing the time it takes to plant each flower.
            growTime (list[int]): A list of integers representing the time it takes for each flower to grow after planting.

        Returns:
            int: The earliest day all flowers are in full bloom.
        """
        flowerData = sorted(zip(plantTime, growTime), key=lambda x: x[1], reverse=True)
        currentPlantTime = 0
        maxBloomTime = 0

        for plant, grow in flowerData:
            currentPlantTime += plant
            maxBloomTime = max(maxBloomTime, currentPlantTime + grow)

        return maxBloomTime