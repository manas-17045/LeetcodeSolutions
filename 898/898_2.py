# Leetcode 898: Bitwise ORs of Subarrays
# https://leetcode.com/problems/bitwise-ors-of-subarrays/
# Solved on 31st of July, 2025
class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """
        Calculates the number of distinct bitwise OR results of all possible subarrays of the given array.

        Args:
            arr: A list of integers.
        Returns:
            The number of distinct bitwise OR results.
        """
        # 'res' will hold all distinct OR-results seen so far.
        res = set()
        # 'rev' holds the OR-results of all subarrays ending at the previous index.
        prev = set()

        for x in arr:
            # Start new subarrays at x, and extend all prev subarrays by x.
            curr = {x}
            for y in prev:
                curr.add(x | y)

            # Merge all ending-at-i results into the global set.
            res |= curr
            # This becomes prev for the next iteration.
            prev = curr

        return len(res)