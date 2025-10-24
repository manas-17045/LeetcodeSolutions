# Leetcode 3377: Digit Operations to Make Two Integers Equal
# https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/
# Solved on 24th of October, 2025
import heapq


class Solution:
    isPrimeList = [True] * 10000
    isPrimeList[0] = isPrimeList[1] = False
    for p in range(2, 100):
        if isPrimeList[p]:
            for i in range(p * p, 10000, p):
                isPrimeList[i] = False

    def minOperations(self, n: int, m: int) -> int:
        """
        Calculates the minimum cost to transform integer n into integer m using digit operations.
        The cost of an operation is the value of the resulting number.
        Numbers that are prime cannot be formed or used in operations.

        :param n: The starting integer.
        :param m: The target integer.
        :return: The minimum cost to transform n to m, or -1 if not possible.
        """

        if self.isPrimeList[n] or self.isPrimeList[m]:
            return -1

        distances = [float('inf')] * 1000
        distances[n] = n
        priorityQueue = [(n, n)]

        while priorityQueue:
            currentCost, u = heapq.heappop(priorityQueue)

            if currentCost > distances[u]:
                continue

            if u == m:
                return currentCost

            s = str(u)
            numDigits = len(s)

            for i in range(numDigits):
                digit = int(s[i])
                power = 10**(numDigits - 1 - i)

                if digit < 9:
                    v = u + power
                    if not self.isPrimeList[v]:
                        newCost = currentCost + v
                        if newCost < distances[v]:
                            distances[v] = newCost
                            heapq.heappush(priorityQueue, (newCost, v))

                if digit > 0:
                    v = u - power
                    if not self.isPrimeList[v]:
                        newCost = currentCost + v
                        if newCost < distances[v]:
                            distances[v] = newCost
                            heapq.heappush(priorityQueue, (newCost, v))

        return -1