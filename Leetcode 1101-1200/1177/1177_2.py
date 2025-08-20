# Leetcode 1177: Can Make Palindrome from Substring
# https://leetcode.com/problems/can-make-palindrome-from-substring/
# Solved on 20th of August, 2025
class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        """
        Given a string s and an array of queries, determine if a substring can be rearranged to form a palindrome
        by changing at most k characters.

        Args:
            s (str): The input string.
            queries (list[list[int]]): A list of queries, where each query is [left, right, k].
        Returns:
            list[bool]: A list of booleans, where each boolean indicates whether the corresponding query can form a palindrome.
        """
        n = len(s)
        prefix = [0] * (n + 1)

        # Build prefix bitmasks
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ (1 << (ord(s[i]) - ord('a')))

        ans = []
        for l, r, k in queries:
            # Odd char count in substring
            mask = prefix[r + 1] ^ prefix[l]
            odd_count = bin(mask).count("1")
            ans.append(odd_count // 2 <= k)

        return ans