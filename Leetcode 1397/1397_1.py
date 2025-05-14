# Leetcode 1397: Find All Good Strings
# https://leetcode.com/problems/find-all-good-strings/
# Solved on 14th of May, 2025

from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        """
        Given integers n, s1, s2, and evil, return the number of good strings.

        A string is good if it has length n, is lexicographically greater than or equal to s1,
        is lexicographically less than or equal to s2, and does not contain evil as a substring.
        Since the answer may be very large, return it modulo 10^9 + 7.

        Args:
            n: The length of the strings to consider.
            s1: The lower lexicographical bound for good strings.
            s2: The upper lexicographical bound for good strings.
            evil: The substring that good strings must not contain.

        Returns:
            The number of good strings modulo 10^9 + 7.

        """
        MOD = 10**9 + 7
        m = len(evil)

        # 1. Precompute LPS array for KMP
        lps = [0] * m   # lps[i] = length of longest proper prefix of evil[0...i] that is also suffix
        # Constraints: m = evil.length >= 1.
        # If m = 1 (e.g. evil = "a") lps loop (i = 1; while i < 1) won't run. lps will be [0]. Correct.
        length = 0
        i = 1
        while i < m:
            if evil[i] == evil[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # 2. Precompute KMP automation transition table
        # kmp_next_state[current_len][char_code] = next_len
        # current_len is the length of current suffix of built string that is a prefix of evil (KMP state)
        # It ranges from 0 to (m - 1).
        # next_len is the new length after appending char_code. It can be up to m.
        kmp_next_state = [[0] * 26 for _ in range(m)]
        for current_match_len_state in range(m):    # KMP states are 0 to (m - 1)
            for char_code in range(26):
                char_to_append = chr(ord('a') + char_code)

                # Find next KMP state using standard KMP logic
                temp_match_len = current_match_len_state
                while temp_match_len > 0 and evil[temp_match_len] != char_to_append:
                    temp_match_len = lps[temp_match_len - 1]

                # Check if current char evil[temp_match_len] extends match
                if evil[temp_match_len] == char_to_append:
                    temp_match_len += 1
                kmp_next_state[current_match_len_state][char_code] = temp_match_len

        @lru_cache(None)
        def dp(idx: int, evil_len_matched_so_far: int, is_tight_s1: bool, is_tight_s2: bool) -> int:
            # Base cases
            if evil_len_matched_so_far == m:
                # Matched `evil` string completely
                return 0
            if idx == n:
                # Successfully built a string of length n without forming 'evil'
                return 1

            res = 0

            # Determine character range for current position idx
            lower_bound_char_code = ord(s1[idx]) - ord('a') if is_tight_s1 else 0
            upper_bound_char_code = ord(s2[idx]) - ord('a') if is_tight_s2 else 25

            for char_code in range(lower_bound_char_code, upper_bound_char_code + 1):
                # Update tightness flags for the next character
                new_tight_s1 = is_tight_s1 and (char_code == lower_bound_char_code)
                new_tight_s2 = is_tight_s2 and (char_code == upper_bound_char_code)

                # Determine the new length of matchd evil prefix
                # evil_len_matched_so_far is guaranteed to be < m because of the base case above.
                # So, it's a valid index for kmp_next_state's first dimension (0 to (m - 1)).
                new_evil_len_matched = kmp_next_state[evil_len_matched_so_far][char_code]

                res = (res + dp(idx + 1, new_evil_len_matched, new_tight_s1, new_tight_s2)) % MOD

            return res

        # Initial DP call
        # Start at index 0
        # No part of evil matched yet (length 0).
        # Bounds are tight for both s1 and s2.
        ans = dp(0, 0, True, True)

        # Clear cache for potential multiple test cases in some environments.
        dp.cache_clear()

        return ans