# Leetcode 2983: Palindrome Rearrangement Queries
# https://leetcode.com/problems/palindrome-rearrangement-queries/
# Solved on 9th of July, 2025
class Solution:
    def canMakePalindromeQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        """
        This function determines if certain palindrome queries can be satisfied.
        A query consists of two substrings [l1, r1] and [c2, d2].
        The goal is to check if, by rearranging characters within these two substrings,
        the original string 's' can be transformed into a palindrome.

        The core idea is to:
        1. Identify all initially mismatched character pairs (s[i] != s[n-1-i]) in the original string.
        2. For each query, determine which of these mismatches fall within the union of the
           first substring [l1, r1] and the "mirrored" second substring [l2, r2] (where [l2, r2]
           corresponds to the indices [n-1-d2, n-1-c2] in the first half of the string).
        3. If there are any mismatches *outside* this union, then it's impossible to form a palindrome,
           because those characters cannot be changed.
        4. If all mismatches are within the union, then we need to check if the characters available
           in [l1, r1] and [c2, d2] (after accounting for fixed characters outside the union of their
           mirrored counterparts) are sufficient to form a palindrome. This means checking if the
           multiset of characters in the remaining parts of [l1, r1] is equal to the multiset of
           characters in the remaining parts of [c2, d2].

        Args:
            s (str): The input string.
            queries (list[list[int]]): A list of queries, where each query is [l1, r1, c2, d2].

        Returns:
            list[bool]: A list of booleans, where each boolean indicates if the corresponding query can be satisfied.
        """
        n = len(s)
        m = n // 2

        pref = [[0] * (n + 1) for _ in range(26)]
        for i, ch in enumerate(s):
            ci = ord(ch) - 97
            for c in range(26):
                pref[c][i + 1] = pref[c][i]
            pref[ci][i + 1] += 1

        # Precompute which pairs (i, (n - 1 - i)) are originally mismatched
        M = [0] * m
        for i in range(m):
            if s[i] != s[n - 1 - i]:
                M[i] = 1
        # Prefix sum of mismatches
        prefM = [0] * (m + 1)
        for i in range(m):
            prefM[i + 1] = prefM[i] + M[i]
        total_mismatches = prefM[m]

        def range_count(c: int, L: int, R: int) -> int:
            return pref[c][R + 1] - pref[c][L]

        def range_mismatches(L: int, R: int) -> int:
            if L > R:
                return 0
            return prefM[R + 1] - prefM[L]

        ans = []
        for l1, r1, c2, d2 in queries:
            # map the right-half substring [c2...d2] back to its first-half pair-indices
            l2 = n - 1 - d2
            r2 = n - 1 - c2

            in_union = (
                    range_mismatches(l1, r1)
                    + range_mismatches(l2, r2)
                    - range_mismatches(max(l1, l2), min(r1, r2))
            )
            if total_mismatches - in_union > 0:
                ans.append(False)
                continue

            # Gather the multiset of chars we can shuffle in each substring
            c1 = [range_count(c, l1, r1) for c in range(26)]
            c2 = [range_count(c, c2, d2) for c in range(26)]

            only_left = []
            ol = max(l1, l2)
            or_ = min(r1, r2)
            if ol <= or_:
                if l1 <= (ol - 1):
                    only_left.append((l1, (ol - 1)))
                if or_ + 1 <= r1:
                    only_left.append(((or_ + 1), r1))
            else:
                only_left.append((l1, r1))

            for L, R in only_left:
                jL, jR = (n - 1 - R), (n - 1 - L)
                for ch in range(26):
                    needed = pref[ch][jR + 1] - pref[ch][jL]
                    c1[ch] -= needed

            only_right = []
            if ol <= or_:
                if l2 <= (ol - 1):
                    only_right.append((l2, (ol - 1)))
                if or_ + 1 <= r2:
                    only_right.append(((or_ + 1), r2))
            else:
                only_right.append((l2, r2))

            for L, R in only_right:
                for ch in range(26):
                    needed = pref[ch][R + 1] - pref[ch][L]
                    c2[ch] -= needed

            # If any count went negative, we couldn't cover the fixed-side requirements
            if any(x < 0 for x in c1) or any(x < 0 for x in c2):
                ans.append(False)
                continue

            ans.append(c1 == c2)

        return ans