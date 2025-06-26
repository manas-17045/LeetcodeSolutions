# Leetcode 1702: Maximum Binary String After Change
# https://leetcode.com/problems/maximum-binary-string-after-change/
# Solved on 26th of June, 2025
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        """
        Transforms a binary string into the lexicographically largest possible binary string
        by applying two operations:
        1. "00" -> "10"
        2. "10" -> "01" (This operation is not directly used for maximization but implies flexibility)

        The strategy is to convert all '0's except one into '1's, pushing the remaining '0'
        as far right as possible.
        """
        n = len(binary)
        # Count zeros
        z = binary.count('0')
        # If fewer than 2 zeros, no beneficial merges possible
        if z <= 1:
            return binary

        # Find index of first '0'
        first_zero = binary.find('0')
        # The single zero in the final string ends up at this position
        zero_pos = first_zero + z - 1

        # Build result
        res = ['1'] * n
        res[zero_pos] = '0'

        return ''.join(res)