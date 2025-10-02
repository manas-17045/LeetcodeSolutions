# Leetcode 3677: Count Binary Palindromic Numbers
# https://leetcode.com/problems/count-binary-palindromic-numbers/
# Solved on 1st of October, 2025
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        """
        Counts the number of binary palindromic numbers less than or equal to n.

        Args:
            n: An integer.
        Returns:
            The count of binary palindromic numbers.
        """
        if n == 0:
            return 1

        s = bin(n)[2:]
        lengthOfN = len(s)
        count = 1

        for length in range(1, lengthOfN):
            halfLength = (length + 1) // 2
            count += (1 << (halfLength - 1))

        halfLengthN = (lengthOfN + 1) // 2
        firstHalfS = s[:halfLengthN]
        firstHalfNum = int(firstHalfS, 2)

        baseNum = 1 << (halfLengthN - 1)
        count += firstHalfNum - baseNum

        secondHalfS = firstHalfS[:(lengthOfN - halfLengthN)]
        reversedSecondHalfS = secondHalfS[::-1]
        palindromeS = firstHalfS + reversedSecondHalfS

        palindromeNum = int(palindromeS, 2)

        if palindromeNum <= n:
            count += 1

        return count