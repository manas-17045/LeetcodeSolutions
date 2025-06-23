# Leetcode 2081: Sum of k-Mirror Numbers
# https://leetcode.com/problems/sum-of-k-mirror-numbers/
# Solved on 23rd of June, 2025

class Solution:
    def kMod(self, k: int, n: int) -> int:
        """
        Finds the sum of the first `n` k-mirror numbers.
        A k-mirror number is a number that is a palindrome in base 10 and also a palindrome in base k.
        :param k: The base to check for palindrome property (2 <= k <= 9).
        :param n: The number of k-mirror numbers to find (1 <= n <= 30).
        """

        def toBaseKString(num: int, base: int) -> str:
            if num == 0:
                return "0"

            digits = []
            while num > 0:
                digits.append(str(num % base))
                num //= base

            return "".join(digits[::-1])

        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        kMirrorSum = 0
        countFound = 0

        # Start with palindromes of length 1
        currentLength = 1
        while countFound < n:
            # Calculate the length of the first half of the palindrome.
            halfLength = (currentLength + 1) // 2

            # Determine the range of numbers for the first half
            startHalfNum = 10**(halfLength - 1)
            endHalfNum = 10**halfLength

            for i in range(startHalfNum, endHalfNum):
                sHalf = str(i)

                # String representation of the Base-10 palindrome
                sNumPalindrome = ""
                if currentLength % 2 == 1:
                    sNumPalindrome = sHalf + sHalf[:1][::-1]
                else:
                    sNumPalindrome = sHalf + sHalf[::-1]

                # Convert to integer
                numPalindrome = int(sNumPalindrome)

                # Convert this Base-10 palindrome to Base-K string
                baseKStr = toBaseKString(numPalindrome, k)

                # Check if it's a palindrome in Base-K
                if isPalindrome(baseKStr):
                    kMirrorSum += numPalindrome
                    countFound += 1
                    if countFound == n:
                        # Found all required numbers
                        return kMirrorSum

            # Move to the next length of palindromes
            currentLength += 1

        return kMirrorSum