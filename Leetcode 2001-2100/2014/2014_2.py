# Leetcode 2014: Longest Subsequence Repeated k Times
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/
# Solved on 27th of June, 2025
from collections import Counter


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        Finds the lexicographically largest string `res` such that `res` repeated `k` times
        is a subsequence of `s`.

        Args:
            s: The input string.
            k: The repetition factor.
        """
        n = len(s)
        # Build nxt array
        nxt = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for c in range(26):
                nxt[i][c] = nxt[i + 1][c]
            nxt[i][ord(s[i]) - 97] = i

        # Fast Check: is T repeated k times a subsequence of s?
        def ok(T: str) -> bool:
            pos = 0
            for _ in range(k):
                for ch in T:
                    c = ord(ch) - 97
                    if pos > n or nxt[pos][c] == n:
                        return False
                    pos = nxt[pos][c] + 1
            return True

        # Only letters that appear >= k times can ever work
        cnt = Counter(s)
        cand = [ch for ch, v in cnt.items() if v >= k]
        if not cand:
            return ""
        # Sort descending for lex-larget-first in put DFS
        cand.sort(reverse=True)

        maxL = n // k
        # Try each possible target length L from maxL down to 1
        for L in range(maxL, 0, -1):
            # DFS build prefix of length up to L
            def dfs(prefix: str) -> str:
                if len(prefix) == L:
                    return prefix
                for ch in cand:
                    newp = prefix + ch
                    # Prune immediately if can't fit k copies of newp
                    if ok(newp):
                        res = dfs(newp)
                        if res:
                            return res
                return ""
            ans = dfs("")
            if ans:
                return ans
        return ""