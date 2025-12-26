# Leetcode 3755: Find Maximum Balanced XOR Subarray Length
# https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/
# Solved on 26th of December, 2025
class Solution:
    def maxBalancedSubarray(self, nums: list[int]) -> int:
        """
        Finds the maximum length of a balanced XOR subarray.

        A subarray is balanced if the count of even numbers equals the count of odd numbers.

        :param nums: A list of integers.
        :return: The maximum length of a balanced XOR subarray.
        """
        seenStates = {(0, 0): -1}

        currentXor = 0
        balance = 0
        maxLength = 0
        for i, num in enumerate(nums):
            currentXor ^= num
            if num % 2 == 0:
                balance += 1
            else:
                balance -= 1

            currentState = (currentXor, balance)
            if currentState in seenStates:
                currentLength = i - seenStates[currentState]
                if currentLength > maxLength:
                    maxLength = currentLength
            else:
                seenStates[currentState] = i

        return maxLength