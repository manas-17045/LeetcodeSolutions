# Leetcode 3130: Find All Possible Stable Binary Arrays II
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/
# Solved on 12th of July, 2025
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        """
        Calculates the number of stable binary arrays.
        :param zero: The number of zeros allowed in the array.
        :param one: The number of ones allowed in the array.
        :param limit: The maximum consecutive occurrences of a single digit.
        :return: The number of stable binary arrays modulo 1,000,000,007.
        """
        mod = 1_000_000_007

        endsWithZero = [[0] * (one + 1) for _ in range(zero + 1)]
        endsWithOne = [[0] * (one + 1) for _ in range(zero + 1)]

        prefixSumZero = [[0] * (one + 1) for _ in range(zero + 1)]
        prefixSumOne = [[0] * (one + 1) for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            endsWithZero[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            endsWithOne[0][j] = 1

        for i in range(zero + 1):
            prefixSumZero[i][0] = endsWithZero[i][0]
        for j in range(one + 1):
            prefixSumOne[0][j] = endsWithOne[0][j]

        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    continue

                if i > 0:
                    val = prefixSumOne[i - 1][j]
                    if i - limit - 1 >= 0:
                        val = (val - prefixSumOne[i - limit - 1][j] + mod) % mod
                    endsWithZero[i][j] = (endsWithZero[i][j] + val) % mod

                if j > 0:
                    val = prefixSumZero[i][j - 1]
                    if j - limit - 1 >= 0:
                        val = (val - prefixSumZero[i][j - limit - 1] + mod) % mod
                    endsWithOne[i][j] = (endsWithOne[i][j] + val) % mod

                prefixSumZero[i][j] = ((prefixSumZero[i][j - 1] if j > 0 else 0) + endsWithZero[i][j]) % mod
                prefixSumOne[i][j] = ((prefixSumOne[i - 1][j] if i > 0 else 0) + endsWithOne[i][j]) % mod

        return (endsWithZero[zero][one] + endsWithOne[zero][one]) % mod