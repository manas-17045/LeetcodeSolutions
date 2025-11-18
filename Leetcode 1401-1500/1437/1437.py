# Leetcode 1437: Check If All 1's Are at Least Length K Places Away
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# Solved on 17th of November, 2025
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        """
        Checks if all 1's in the given array are at least k places away from each other.

        Args:
            nums (list[int]): The input array of 0s and 1s.
            k (int): The minimum distance required between two 1s.
        Returns:
            bool: True if all 1s are at least k places away, False otherwise.
        """
        zeroCount = k

        for num in nums:
            if num == 1:
                if zeroCount < k:
                    return False
                zeroCount = 0
            else:
                zeroCount += 1

        return True