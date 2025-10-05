# Leetcode 3352: Count K-Reducible Numbers Less Than N
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/
# Solved on 5th of October, 2025
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        """
        Counts the number of k-reducible numbers less than the given binary string `s`.
        :param s: A binary string representing the upper bound (exclusive).
        :param k: An integer representing the k-reducibility condition.
        :return: The count of k-reducible numbers less than `s`, modulo 1,000,000,007.
        """
        mod = 1_000_000_007
        strLen = len(s)

        ops = [-1] * (strLen + 2)
        if strLen >= 0:
            ops[1] = 0

        for i in range(2, strLen + 1):
            popCount = bin(i).count('1')
            ops[i] = 1 + ops[popCount]

        goodPopCounts = set()
        if k > 0:
            for i in range(1, strLen + 1):
                if ops[i] != -1 and ops[i] <= k - 1:
                    goodPopCounts.add(i)

        combinations = [[0] * (strLen + 1) for _ in range(strLen + 1)]
        for i in range(strLen + 1):
            combinations[i][0] = 1
            for j in range(1, i + 1):
                combinations[i][j] = (combinations[i - 1][j - 1] + combinations[i - 1][j]) % mod

        result = 0
        setBitsCount = 0
        for i in range(strLen):
            remainingLen = strLen - 1 - i
            if s[i] == '1':
                for p in goodPopCounts:
                    neededOnes = p - setBitsCount
                    if 0 <= neededOnes <= remainingLen:
                        result = (result + combinations[remainingLen][neededOnes]) % mod
                setBitsCount += 1

        return result