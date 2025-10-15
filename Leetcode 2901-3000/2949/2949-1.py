# Leetcode 2949: Count Beautiful Substrings II
# https://leetcode.com/problems/count-beautiful-substrings-ii/
# Solved on 14th of October, 2025
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        """
        Counts the number of "beautiful" substrings in a given string `s`.
        A substring is beautiful if the number of vowels and consonants are equal,
        and the product of the number of vowels and consonants is divisible by `k`.
        :param s: The input string.
        :param k: The integer divisor.
        :return: The total count of beautiful substrings.
        """
        def findRequiredFactor(numberK: int) -> int:
            requiredFactor = 1
            d = 2
            tempK = numberK
            while d * d <= tempK:
                if tempK % d == 0:
                    count = 0
                    while tempK % d == 0:
                        count += 1
                        tempK //= d
                    exponent = (count + 1) // 2
                    requiredFactor *= (d ** exponent)
                d += 1
            if tempK > 1:
                requiredFactor *= tempK

            return requiredFactor

        vowels = "aeiou"
        n = len(s)
        requiredVowelCountFactor = findRequiredFactor(k)
        period = 2 * requiredVowelCountFactor

        prefixSum = 0
        seenStates = {(0, 0): 1}
        beautifulCount = 0

        for index in range(n):
            char = s[index]
            if char in vowels:
                prefixSum += 1
            else:
                prefixSum -= 1

            remainder = (index + 1) % period
            currentState = (prefixSum, remainder)

            beautifulCount += seenStates.get(currentState, 0)
            seenStates[currentState] = seenStates.get(currentState, 0) + 1

        return beautifulCount