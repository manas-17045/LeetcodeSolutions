# Leetcode 3621: Number of Integers With Popcount-Depth Equal to K I
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/
# Solved on 19th of December, 2025
import math


class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        """
        Calculates the number of integers x such that 1 <= x <= n and the popcount-depth of x is equal to k.

        :param n: The upper limit for the integers.
        :param k: The target popcount-depth.
        :return: The count of integers with the specified popcount-depth.
        """

        if k == 0:
            return 1

        def getDepth(num):
            depth = 0
            while num > 1:
                num = bin(num).count('1')
                depth += 1
            return depth

        validCounts = []
        for i in range(1, 61):
            if getDepth(i) == k - 1:
                validCounts.append(i)

        if not validCounts:
            return 0

        def countWithBits(limit, bits):
            binaryString = bin(limit)[2:]
            length = len(binaryString)
            result = 0
            currentSet = 0

            for i in range(length):
                if binaryString[i] == '1':
                    remainingLen = length - 1 - i
                    needed = bits - currentSet
                    if 0 <= needed <= remainingLen:
                        result += math.comb(remainingLen, needed)
                    currentSet += 1

            if currentSet == bits:
                result += 1

            return result

        total = 0
        for count in validCounts:
            total += countWithBits(n, count)

        if k == 1:
            total -= 1

        return total