# Leetcode 3741: Minimum Distance Between Three Equal Elements II
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/
# Solved on 19th of November, 2025
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        """
        Calculates the minimum distance between three equal elements in the given list.
        The distance is defined as (index_k - index_i) * 2, where index_i, index_j, index_k
        are the indices of three equal elements such that index_i < index_j < index_k.
        The function aims to find the minimum such distance.

        Args:
            nums: A list of integers.

        Returns:
            The minimum distance found. Returns -1 if no three equal elements are found.
        """
        indicesMap = {}
        minDist = 2147483647
        found = False

        for i, num in enumerate(nums):
            if num not in indicesMap:
                indicesMap[num] = [i]
            else:
                currentIndices = indicesMap[num]
                if len(currentIndices) == 1:
                    currentIndices.append(i)
                else:
                    currentDist = (i - currentIndices[0]) * 2
                    if currentDist < minDist:
                        minDist = currentDist
                    found = True
                    currentIndices[0] = currentIndices[1]
                    currentIndices[1] = i

        if not found:
            return -1

        return minDist