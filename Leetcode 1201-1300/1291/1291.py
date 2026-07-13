# Leetcode 1291: Sequential Digits
# https://leetcode.com/problems/sequential-digits/
# Solved on 13th of July, 2026
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        """
        Finds all sequential digits in the range of low and high
        A sequential digit number is a number that has digits in increasing order
        e.g., 12, 123, 1234, etc.
        
        :param low: the lower bound of the range
        :param high: the upper bound of the range
        :return: a list of sequential digits in the range
        """
        digitString = "123456789"
        resultList = []

        for numLength in range(2, 10):
            for startIndex in range(10 - numLength):
                currentNum = int(digitString[startIndex:startIndex + numLength])
                if low <= currentNum <= high:
                    resultList.append(currentNum)

        return resultList