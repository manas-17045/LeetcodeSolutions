# Leetcode 2484: Count Palindromic Subsequences
# https://leetcode.com/problems/count-palindromic-subsequences/
# Solved on 17th of August, 2025
class Solution:
    def countPalindromes(self, s: str) -> int:
        """
        Counts the number of palindromic subsequences of length 5 in the given string `s`.
        :param s: The input string consisting of digits.
        :return: The number of palindromic subsequences of length 5, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(s)
        if n < 5:
            return 0

        arr = [ord(c) - 48 for c in s]

        left_single = [0] * 10
        left_pairs = [[0] * 10 for _ in range(10)]
        for i in range(0, 2):
            x = arr[i]
            for d in range(10):
                left_pairs[d][x] += left_single[d]
            left_single[x] += 1

        right_single = [0] * 10
        right_pairs = [[0] * 10 for _ in range(10)]
        # Build by scanning from rightmost down to index 3 (inclusive)
        for i in range(n - 1, 2, -1):
            x = arr[i]
            for d in range(10):
                right_pairs[x][d] += right_single[d]
            right_single[x] += 1

        ans = 0
        # Iterate centers k from 2 to (n - 3) inclusive
        for k in range(2, n - 2):
            total_k = 0
            for a in range(10):
                la = left_pairs[a]
                for b in range(10):
                    rb_a = right_pairs[b][a]
                    if la[b] and rb_a:
                        total_k += la[b] * rb_a
            ans = (ans + total_k) % MOD

            # Prepare for next center
            x_left = arr[k]
            for d in range(10):
                left_pairs[d][x_left] += left_single[d]
            left_single[x_left] += 1

            # Remove index (k + 1) from right region (it was the leftmost of right).
            pos = k + 1
            if pos < n:
                x_rem = arr[pos]
                for d in range(10):
                    right_pairs[x_rem][d] -= (right_single[d] - (1 if d == x_rem else 0))
                right_single[x_rem] -= 1

        return ans % MOD