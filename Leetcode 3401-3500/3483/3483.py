# Leetcode 3483: Unique 3-Digit Even Numbers
# https://leetcode.com/problems/unique-3-digit-even-numbers/
# Solved on 11th of September, 2026
class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        """
        Calculates the number of distinct three-digit even numbers without leading zeros
        that can be formed using the provided digits.

        Parameters:
            digits (List[int]): A list of single-digit integers from 0 to 9.

        Returns:
            int: The total count of unique three-digit even numbers that can be created.
        """
        digitFrequencies = [0] * 10
        for singleDigit in digits:
            digitFrequencies[singleDigit] += 1
        
        validCount = 0

        for candidateNumber in range(100, 1000, 2):
            hundredsDigit = candidateNumber // 100
            tensDigit = (candidateNumber // 10) % 10
            unitsDigit = candidateNumber % 10

            digitFrequencies[hundredsDigit] -= 1
            digitFrequencies[tensDigit] -= 1
            digitFrequencies[unitsDigit] -= 1

            if (
                digitFrequencies[hundredsDigit] >= 0
                and digitFrequencies[tensDigit] >= 0
                and digitFrequencies[unitsDigit] >= 0
            ):
                validCount += 1

            digitFrequencies[hundredsDigit] += 1
            digitFrequencies[tensDigit] += 1
            digitFrequencies[unitsDigit] += 1

        return validCount