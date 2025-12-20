# Leetcode 3699: Number of ZigZag Arrays I
# https://leetcode.com/problems/number-of-zigzag-arrays-i/
# Solved on 20th of December, 2025
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        """
        Calculates the number of zigzag arrays of length n with elements in the range [l, r].

        Args:
            n (int): The desired length of the zigzag array.
            l (int): The lower bound of the elements in the array (inclusive).
            r (int): The upper bound of the elements in the array (inclusive).

        Returns:
            int: The number of zigzag arrays modulo 10^9 + 7.
        """
        mod = 10**9 + 7
        m = r - l + 1

        up = [0] * m
        down = [0] * m

        for i in range(m):
            up[i] = i
            down[i] = m - 1 - i

        for _ in range(3, n + 1):
            newUp = [0] * m
            newDown = [0] * m

            currentSum = 0
            for i in range(m):
                newUp[i] = currentSum
                currentSum = (currentSum + down[i]) % mod

            currentSum = 0
            for i in range(m - 1, -1, -1):
                newDown[i] = currentSum
                currentSum = (currentSum + up[i]) % mod

            up = newUp
            down = newDown

        total = (sum(up) + sum(down)) % mod
        return total