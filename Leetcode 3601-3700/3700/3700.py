# Leetcode 3700: Number of ZigZag Arrays II
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/
# Solved on 20th of December, 2025
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        """
        Calculates the number of zigzag arrays of length n with elements in the range [l, r].

        Args:
            n (int): The length of the zigzag array.
            l (int): The lower bound of the elements.
            r (int): The upper bound of the elements.

        Returns:
            int: The number of zigzag arrays modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        T = [[min(i, j) for j in range(m)] for i in range(m)]
        vec = list(range(m))

        k = (n - 2) // 2

        res = [[0] * m for _ in range(m)]
        for i in range(m):
            res[i][i] = 1

        base = T
        while k > 0:
            if k % 2 == 1:
                res = self.matMulSymmetric(res, base, MOD)
            base = self.matMulSymmetric(base, base, MOD)
            k //= 2

        newVec = [0] * m
        for i in range(m):
            s = 0
            row = res[i]
            for j in range(m):
                s += row[j] * vec[j]
            newVec[i] = s % MOD
        vec = newVec

        if (n - 2) % 2 == 1:
            dPrev = vec[::-1]
            currentSum = 0
            for i in range(m):
                val = dPrev[i]
                dPrev[i] = currentSum
                currentSum = (currentSum + val) % MOD
            vec = dPrev

        total = sum(vec) % MOD
        return (total * 2) % MOD

    def matMulSymmetric(self, A, B, mod):
        size = len(A)
        C = [[0] * size for _ in range(size)]
        for i in range(size):
            rowA = A[i]
            for j in range(i, size):
                rowB = B[j]
                s = 0
                for k in range(size):
                    s += rowA[k] * rowB[k]
                s %= mod
                C[i][j] = s
                C[j][i] = s
        return C