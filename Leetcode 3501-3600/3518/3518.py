# Leetcode 3518: Smallest Palindromic Rearrangement II
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/
# Solved on 6th of December, 2025
import collections
import math
import sys
sys.setrecursionlimit(20000)


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        """
        Finds the k-th lexicographically smallest palindromic rearrangement of the input string s.

        Args:
            s (str): The input string.
            k (int): The 1-indexed rank of the desired palindromic rearrangement.

        Returns:
            str: The k-th lexicographically smallest palindromic rearrangement, or an empty string if k is too large.
        """
        freq = collections.Counter(s)
        half_freq = {}
        mid_char = ""

        for char, count in freq.items():
            if count % 2 == 1:
                mid_char = char
            if count // 2 > 0:
                half_freq[char] = count // 2

        half_len = len(s) // 2

        def get_log_perms(n, counts):
            val = math.lgamma(n + 1)
            for c in counts.values():
                val -= math.lgamma(c + 1)
            return val

        def get_exact_perms(n, counts):
            denom = 1
            for c in counts.values():
                denom *= math.factorial(c)
            return math.factorial(n) // denom

        initial_log = get_log_perms(half_len, half_freq)
        log_k = math.log(k) if k > 0 else 0

        if initial_log < log_k - 1e-9:
            if initial_log > log_k - 0.1:
                total = get_exact_perms(half_len, half_freq)
                if total < k: return ""
            else:
                return ""

        is_exact = False
        current_val = 0
        current_log = initial_log

        if current_log < log_k + 2.0:
            current_val = get_exact_perms(half_len, half_freq)
            if current_val < k: return ""
            is_exact = True

        result = []
        rem_len = half_len
        sorted_chars = sorted(half_freq.keys())

        for _ in range(half_len):
            for char in sorted_chars:
                if half_freq[char] > 0:
                    count = half_freq[char]

                    if is_exact:
                        branch_val = (current_val * count) // rem_len
                        if k <= branch_val:
                            result.append(char)
                            half_freq[char] -= 1
                            current_val = branch_val
                            rem_len -= 1
                            break
                        else:
                            k -= branch_val
                    else:
                        branch_log = current_log + math.log(count) - math.log(rem_len)

                        if branch_log > log_k + 0.5:
                            result.append(char)
                            half_freq[char] -= 1
                            current_log = branch_log
                            rem_len -= 1
                            break
                        else:
                            temp_freq = half_freq.copy()
                            temp_freq[char] -= 1
                            branch_val = get_exact_perms(rem_len - 1, temp_freq)

                            if k <= branch_val:
                                result.append(char)
                                half_freq[char] -= 1
                                current_val = branch_val
                                is_exact = True
                                rem_len -= 1
                                break
                            else:
                                k -= branch_val

        half_s = "".join(result)
        return half_s + mid_char + half_s[::-1]