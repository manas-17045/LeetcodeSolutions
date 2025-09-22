# Leetcode 1977: Number of Ways to Separate Numbers
# https://leetcode.com/problems/number-of-ways-to-separate-numbers/
# Solved on 22nd of September, 2025
from array import array


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        """
        Calculates the number of ways to split a string `num` into a sequence of non-decreasing integers.

        Args:
            num: A string representing a large integer.
        Returns:
            The number of valid combinations modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        n = len(num)
        # Quick reject: first number cannot start with '0'
        if n == 0 or num[0] == '0':
            return 0

        # Precompute LCP (longest common prefix) table as array('H') rows for memory efficiency.
        # lcp[i][j] = length of longest common prefix of num[i:] and num[j:].
        lcp = [array('H', [0] * (n + 1)) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            row_i = lcp[i]
            row_ip1 = lcp[i + 1]
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    # safe to add 1 since lcp entry fits in unsigned short (n <= 3500)
                    row_i[j] = row_ip1[j + 1] + 1
                else:
                    row_i[j] = 0

        # prefix[j][k] = sum_{p=1..k} dp[j][p] where dp[j][p] is number of ways to split first j chars
        # with last number length p. We keep triangular structure: prefix[0] length 1, prefix[i] length i+1.
        prefix = [array('I', [0] * (i + 1)) for i in range(n + 1)]
        # prefix[0][0] = 0 (no ways for empty prefix except handled when j==0 below)

        for i in range(1, n + 1):  # i : length of prefix considered (1..n)
            row = prefix[i]  # this will be filled; row[0] remains 0
            # row[0] = 0 already
            for l in range(1, i + 1):  # l : length of last number in this prefix
                start_idx = i - l  # 0-based start index of last number
                if num[start_idx] == '0':
                    dp_val = 0
                else:
                    j = i - l  # prefix length before last number
                    if j == 0:
                        # whole prefix is a single number
                        dp_val = 1
                    else:
                        # sum of dp[j][p] for p = 1..min(l, j)
                        k = l if l <= j else j
                        total = prefix[j][k]
                        # if previous number has same length l (i.e., j >= l),
                        # we must exclude dp[j][l] when previous > current (lex compare)
                        if j >= l:
                            a = j - l  # 0-based start of previous number
                            b = start_idx  # 0-based start of current number
                            t = lcp[a][b]
                            if t < l and num[a + t] > num[b + t]:
                                # previous > current -> exclude dp[j][l]
                                prev_l = (prefix[j][l] - prefix[j][l - 1]) % MOD
                                total = (total - prev_l) % MOD
                        dp_val = total % MOD
                # prefix sum accumulation: row[l] = row[l-1] + dp_val
                row[l] = (row[l - 1] + dp_val) % MOD

        # Total ways to split full string = sum_{l=1..n} dp[n][l] = prefix[n][n]
        return prefix[n][n] % MOD