# Leetcode 2644: Find the Maximum Divisibility Score
# https://leetcode.com/problems/find-the-maximum-divisibility-score/
# Solved on 2nd of December, 2025
class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        """
        Calculates the divisor with the maximum divisibility score.
        The divisibility score of a divisor is the number of times it divides an element in nums.
        If multiple divisors have the same maximum score, the smallest divisor is returned.

        :param nums: A list of integers.
        :param divisors: A list of integers representing potential divisors.
        :return: The divisor with the maximum divisibility score, or the smallest such divisor in case of a tie.
        """
        maxScore = -1
        result = 0

        for divisor in divisors:
            currentScore = 0
            for num in nums:
                if num % divisor == 0:
                    currentScore += 1

            if currentScore > maxScore:
                maxScore = currentScore
                result = divisor
            elif currentScore == maxScore:
                if divisor < result:
                    result = divisor

        return result