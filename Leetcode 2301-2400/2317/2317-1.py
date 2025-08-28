# Leetcode 2317: Maximum XOR After Operations
# https://leetcode.com/problems/maximum-xor-after-operations/
# Solved on 28th of August, 2025
class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible XOR sum of all elements in the array after any number of operations.
        An operation consists of choosing an index i and a bit position j, and if the j-th bit of nums[i] is set,
        then flipping the j-th bit of nums[i] and nums[k] for any k != i.
        :param nums: A list of integers.
        :return: The maximum possible XOR sum.
        """
        maximumValue = 0
        for num in nums:
            maximumValue |= num
        return maximumValue