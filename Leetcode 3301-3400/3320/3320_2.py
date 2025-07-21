# Leetcode 3320: Count The Number of Winning Sequences
# https://leetcode.com/problems/count-the-number-of-winning-sequences/
# Solved on 21st of July, 2025
class Solution:
    def countWinningSequences(self, s: str) -> int:
        """
        Counts the number of winning sequences based on a given string `s`.

        Args:
            s (str): A string consisting of 'F', 'W', or 'E' characters.

        Returns:
            int: The number of winning sequences modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        n = len(s)
        mp = {'F': 0, 'W': 1, 'E': 2}
        A = [mp[ch] for ch in s]

        delta = [[0] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                if b == a:
                    delta[a][b] = 0
                elif (b - a) % 3 == 1:
                    delta[a][b] = +1
                else:
                    delta[a][b] = -1

        size = 2 * n + 1
        dp_prev = [[0] * size for _ in range(4)]
        dp_prev[3][n] = 1

        for i in range(n):
            dp_curr = [[0] * size for _ in range(4)]
            a = A[i]
            for prev in range(4):
                row = dp_prev[prev]
                if not any(row):
                    continue
                for d in range(size):
                    ways = row[d]
                    if ways == 0:
                        continue
                    for b in range(3):
                        if b == prev:
                            continue
                        nd = d + delta[a][b]
                        if 0 <= nd < size:
                            dp_curr[b][nd] = (dp_curr[b][nd] + ways) % MOD
            dp_prev = dp_curr

        # Sum up all sequences where final diff > 0 => index d > n
        ans = 0
        for prev in range(3):
            for d in range((n + 1), size):
                ans = (ans + dp_prev[prev][d]) % MOD

        return ans