# Leetcode 2176: Count Equal and Divisible Pairs in an Array
# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        """
        Uses a nested loop approach to check all valid pairs (i, j).

        Args:
            nums: The input list of integers.
            k: The integer divisor.

        Returns:
            The total count of pairs satisfying all conditions.
        """

        # Initialize the count of good pairs
        count = 0
        # Get the length of the input array
        n = len(nums)

        # Iterate through all possible first indices 'i'
        for i in range(n):
            # Iterate through all possible second indices 'j' such that j > i
            for j in range(i + 1, n):
                # Check the two conditions required for a pair (i, j) to be sounted.
                # 1. The values at the indices must be equal.
                # 2. The product of the indices must be divisible by k.
                if nums[i] == nums[j] and (i * j) % k == 0:
                    # If both conditions are met, increment the counter.
                    count += 1

        # Return the final count of pairs satisfying the condition
        return count