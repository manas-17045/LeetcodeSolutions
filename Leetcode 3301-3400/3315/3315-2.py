# Leetcode 3315: Construct the Minimum Bitwise Array II
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/
# Solved on 14th of October, 2025
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        """
        Calculates a modified array where each element x is transformed based on its binary representation.
        If x is 2 or has no trailing ones in its binary representation, it's replaced by -1.
        Otherwise, it's replaced by x minus 2^(k-1), where k is the count of trailing ones.

        Args:
            nums: A list of integers.
        Returns:
            A list of integers representing the transformed array.
        """
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
                continue

            # Count trailing ones in x's binary representation
            t = x
            k = 0
            while (t & 1) == 1:
                k += 1
                t >>= 1

            if k == 0:
                ans.append(-1)
            else:
                ans.append(x - (1 << (k - 1)))

        return ans