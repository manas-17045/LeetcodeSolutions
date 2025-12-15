# Leetcode 3470: Permutations IV
# https://leetcode.com/problems/permutations-iv/
# Solved on 15th of December, 2025
import math


class Solution:
    def permute(self, n: int, k: int) -> list[int]:
        """
        Generates the k-th lexicographical permutation of numbers from 1 to n such that no two adjacent numbers have the same parity.
        :param n: The upper limit of the numbers to permute (1 to n).
        :param k: The k-th permutation to find.
        :return: A list of integers representing the k-th permutation, or an empty list if no such permutation exists.
        """
        remOdds = math.ceil(n / 2)
        remEvens = n // 2
        availableNumbers = list(range(1, (n + 1)))
        result = []
        currentK = k

        def countPerms(rOdds, rEvens, nextParity):
            total = rOdds + rEvens
            if total == 0:
                return 1

            if nextParity == 1:
                neededOdds = (total + 1) // 2
                neededEvens = total // 2
            else:
                neededEvens = (total + 1) // 2
                neededOdds = total // 2

            if rOdds == neededOdds and rEvens == neededEvens:
                return math.factorial(rOdds) * math.factorial(rEvens)

            return 0

        for i in range(n):
            found = False
            for idx, num in enumerate(availableNumbers):
                if i > 0:
                    prevNum = result[-1]
                    if (prevNum % 2) == (num % 2):
                        continue

                isOdd = (num % 2 != 0)
                tempRemOdds = remOdds - (1 if isOdd else 0)
                tempRemEvens = remEvens - (1 if not isOdd else 0)

                nextReq = 0 if isOdd else 1

                count = countPerms(tempRemOdds, tempRemEvens, nextReq)

                if currentK <= count:
                    result.append(num)
                    availableNumbers.pop(idx)
                    if isOdd:
                        remOdds -= 1
                    else:
                        remEvens -= 1
                    found = True
                    break
                else:
                    currentK -= count

            if not found:
                return []

        return result