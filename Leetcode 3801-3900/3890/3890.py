# Leetcode 3890: Integers With Multiple Sum of Two Cubes
# https://leetcode.com/problems/integers-with-multipl-sum-of-two-cubes/
# Solved on 12th of April, 2026
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        """
        Finds all integers up to n that can be expressed as the sum of two positive cubes
        in at least two different ways (Taxicab numbers).

        :param n: The upper limit for the sum of two cubes.
        :return: A sorted list of integers that satisfy the condition.
        """
        sumCounts = {}
        a = 1

        while True:
            cubeA = a * a * a
            if 2 * cubeA > n:
                break

            b = a
            while True:
                cubeB = b * b * b
                currentSum = cubeA + cubeB

                if currentSum > n:
                    break

                if currentSum in sumCounts:
                    sumCounts[currentSum] += 1
                else:
                    sumCounts[currentSum] = 1

                b += 1

            a += 1

        goodIntegers = []
        for currentSum, count in sumCounts.items():
            if count >= 2:
                goodIntegers.append(currentSum)

        goodIntegers.sort()
        return goodIntegers