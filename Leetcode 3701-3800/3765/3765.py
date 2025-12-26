# Leetcode 3765: Complete Prime Number
# https://leetcode.com/problems/complete-prime-number/
# Solved on 26th of December, 2025
class Solution:
    def completePrime(self, num: int) -> bool:
        """
        Checks if a given number is a "complete prime".
        A number is a complete prime if all its prefixes and suffixes are prime numbers.
        :param num: The integer to check.
        :return: True if the number is a complete prime, False otherwise.
        """
        def checkPrime(val):
            if val <= 1:
                return False
            if val <= 3:
                return True
            if val % 2 == 0 or val % 3 == 0:
                return False
            i = 5
            while i * i <= val:
                if val % i == 0 or val % (i + 2) == 0:
                    return False
                i += 6
            return True

        numString = str(num)
        totalLength = len(numString)

        for i in range(1, totalLength + 1):
            prefixVal = int(numString[:i])
            suffixVal = int(numString[totalLength - i:])

            if not checkPrime(prefixVal) or not checkPrime(suffixVal):
                return False

        return True