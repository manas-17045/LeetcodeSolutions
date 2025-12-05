# Leetcode 3761: Minimum Absolute Distance Between Mirror Pairs
# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/
# Solved on 5th of December, 2025
class Solution:
    def minMirrorPairDistances(self, nums: list[int]) -> int:
        """
        Calculates the minimum absolute distance between "mirror pairs" in a list of integers.
        A mirror pair consists of two numbers where one is the reverse of the other (e.g., 123 and 321).

        Args:
            nums: A list of integers.

        Returns:
            The minimum absolute distance between any mirror pair. Returns -1 if no such pair exists.
        """
        minDist = float('inf')
        lastSeen = {}
        for i, num in enumerate(nums):
            if num in lastSeen:
                distance = i - lastSeen[num]
                if distance < minDist:
                    minDist = distance

            revNum = int(str(num)[::-1])
            lastSeen[revNum] = i

        return -1 if minDist == float('inf') else minDist