# Leetcode 1397: Find All Good Strings
# https://leetcode.com/problems/find-all-good-strings/
# Solved on 14th of May, 2025

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        """
        Given integers n, s1, s2, and evil, return the number of good strings.

        A string is good if it has length n, is lexicographically greater than or equal to s1,
        is lexicographically less than or equal to s2, and does not contain evil as a substring.

        Since the answer may be very large, return it modulo 10^9 + 7.

        Args:
            n: The length of the good strings.
            s1: The lower bound string (inclusive).
            s2: The upper bound string (inclusive).
            evil: The forbidden substring.
        """
        MOD = 10**9 + 7
        L = len(evil)

        # Build KMP "failure" table for 'evil'
        lps = [0] * L
        j = 0
        for i in range(1, L):
            while j > 0 and evil[i] != evil[j]:
                j = lps[j - 1]
            if evil[i] == evil[j]:
                j += 1
            lps[i] = j

        # Build automaton: nxt[k][c] = length of matched prefix after
        # seeing character c when currently matched prefix length is k
        nxt = [[0] * 26 for _ in range(L + 1)]
        for k in range(L + 1):
            for ci in range(26):
                c = chr(ci + 97)
                if k < L and c == evil[k]:
                    nxt[k][ci] = k + 1
                else:
                    t = k
                    while t > 0 and (t == L or evil[t] != c):
                        t = lps[t - 1]
                    if t < L and evil[t] == c:
                        t += 1
                    nxt[k][ci] = t

        # dp[k][low][high]: number of ways at current position
        # with matched-prefix = k, low flag, high flag
        # low=1 means we've matched prefix == s1 so far;
        # 0 means already above s1
        # high=1 means matched prefix == s2 so far;
        # 0 means already below s2
        dp = [[[0] * 2 for _ in range(2)] for __ in range(L)]
        dp[0][1][1] = 1

        for pos in range(n):
            ndp = [[[0] * 2 for _ in range(2)] for __ in range(L)]
            c1 = ord(s1[pos]) - 97
            c2 = ord(s2[pos]) - 97

            for k in range(L):
                for low in (0, 1):
                    for high in (0, 1):
                        ways = dp[k][low][high]
                        if not ways:
                            continue
                        # Try all next characters
                        lo = c1 if low else 0
                        hi = c2 if high else 25
                        for ci in range(lo, hi + 1):
                            nk = nxt[k][ci]
                            # If we matched full 'evil', forbidden
                            if nk == L:
                                continue
                            nlow = low and (ci == c1)
                            nhigh = high and (ci == c2)
                            ndp[nk][nlow][nhigh] = (ndp[nk][nlow][nhigh] + ways) % MOD

            dp = ndp

        # Sum all safe states
        ans = 0
        for k in range(L):
            for low in (0, 1):
                for high in (0, 1):
                    ans = (ans + dp[k][low][high]) % MOD

        return ans