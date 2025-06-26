# Leetcode 2311: Longest Binary Subsequence Less Than or Equal to K
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
# Solved on 26th of June, 2025
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        Finds the length of the longest binary subsequence of `s` whose decimal value
        is less than or equal to `k`.

        The strategy is to prioritize including '0's as they contribute to the length
        without increasing the value. For '1's, we greedily include them from the
        right (least significant bit) as long as the current value does not exceed `k`.

        Args:
            s (str): The input binary string.
            k (int): The maximum allowed decimal value for the subsequence.
        Returns:
            int: The length of the longest binary subsequence.
        """
        n = len(s)

        numZeros = s.count('0')

        numOnesChosen = 0
        currentValue = 0
        powerOfTwo = 1

        for i in range((n - 1), -1, -1):
            if powerOfTwo > k:
                break

            if s[i] == '1':
                if currentValue + powerOfTwo <= k:
                    currentValue += powerOfTwo
                    numOnesChosen += 1

            if i == 0:
                break

            powerOfTwo *= 2

        return numZeros + numOnesChosen