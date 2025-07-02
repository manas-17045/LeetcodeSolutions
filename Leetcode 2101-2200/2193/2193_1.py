# Leetcode 2193: Minimum Number of Moves to Make Palindrome
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
# Solved on 2nd of July, 2025
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        """
        Calculates the minimum number of moves required to make a given string a palindrome.

        A move consists of swapping two adjacent characters.
        The string is guaranteed to be transformable into a palindrome.

        Args:
            s: The input string.

        Returns:
            The minimum number of moves.
        """
        sList = list(s)
        totalMoves = 0

        left = 0
        right = len(sList) - 1

        while left < right:
            if sList[left] == sList[right]:
                left += 1
                right -= 1
                continue

            k = right - 1
            while k > left and sList[k] != sList[left]:
                k -= 1

            if k == left:
                sList[left], sList[left + 1] = sList[left + 1], sList[left]
                totalMoves += 1
            else:
                movesForCurrentPair = right - k
                totalMoves += movesForCurrentPair

                charToMove = sList[k]
                for i in range(k, right):
                    sList[i] = sList[i + 1]
                sList[right] = charToMove

                left += 1
                right -= 1

        return totalMoves