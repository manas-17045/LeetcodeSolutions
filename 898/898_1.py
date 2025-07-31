# Leetcode 898: Bitwise ORs of Subarrays
# https://leetcode.com/problems/bitwise-ors-of-subarrays/
# Solved on 31st of July, 2025
class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """
        Calculates the number of unique bitwise ORs of all possible subarrays.

        Args:
            arr: A list of integers.
        Returns:
            The total count of unique bitwise ORs of subarrays.
        """
        allResults = set()
        prevResults = set()

        for val in arr:
            currentResults = {val | prev for prev in prevResults} | {val}
            allResults.update(currentResults)
            prevResults = currentResults

        return len(allResults)