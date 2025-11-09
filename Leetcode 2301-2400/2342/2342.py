# Leetcode 2342: Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
# Solved on 9th of November, 2025
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        """
        Given a 0-indexed array nums of integers, find the maximum sum of a pair of numbers from nums
        such that the sum of their digits are equal.
        :param nums: A list of integers.
        :return: The maximum sum of a pair with equal digit sums, or -1 if no such pair exists.
        """
        def getDigitSum(n: int) -> int:
            digitSum = 0
            while n > 0:
                digitSum += n % 10
                n //= 10
            return digitSum

        sumMap = {}
        maxSum = -1

        for num in nums:
            currentDigitSum = getDigitSum(num)

            if currentDigitSum in sumMap:
                prevMaxNum = sumMap[currentDigitSum]
                maxSum = max(maxSum, num + prevMaxNum)
                sumMap[currentDigitSum] = max(prevMaxNum, num)
            else:
                sumMap[currentDigitSum] = num

        return maxSum