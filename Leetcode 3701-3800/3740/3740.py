# Leetcode 3740: Minimum Distance Between Three Equal Elements I
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/
# Solved on 10th of April, 2026
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        """
        Calculates the minimum distance between three equal elements in the list.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The minimum distance found, or -1 if no three equal elements exist.
        """
        indicesMap = {}
        for i in range(len(nums)):
            currentVal = nums[i]
            if currentVal not in indicesMap:
                indicesMap[currentVal] = []
            indicesMap[currentVal].append(i)

        minDist = -1

        for currentVal in indicesMap:
            idxList = indicesMap[currentVal]
            listLength = len(idxList)
            if listLength >= 3:
                for i in range(listLength - 2):
                    currentDist = 2 * (idxList[i + 2] - idxList[i])
                    if minDist == -1 or currentDist < minDist:
                        minDist = currentDist

        return minDist