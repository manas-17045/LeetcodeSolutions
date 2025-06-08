# Leetcode 2301: Match Substring After Replacement
# https://leetcode.com/problems/match-substring-after-replacement/
# Solved on 8th of June, 2025

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: list[list[str]]) -> bool:
        """
        Given two strings s and sub, and a list of character mappings, determine if sub can be a substring of s
        after applying zero or more character replacements according to the mappings.

        Args:
            s: The main string.
            sub: The substring to search for.
            mappings: A list of [old_char, new_char] pairs representing allowed replacements.

        Returns:
            True if sub can be a substring of s after replacements, False otherwise.
        """
        # Build map: old_char -> set of new_chars
        rep = {}
        for old, new in mappings:
            if old not in rep:
                rep[old] = set()
            rep[old].add(new)

        n, m = len(s), len(sub)
        # For each possible starting position in s
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                sc = s[i + j]
                cc = sub[j]
                if sc == cc:
                    continue
                # If no direct match, see if cc -> sc is allowed
                if cc in rep and sc in rep[cc]:
                    continue
                # Otherwise, this window falls
                match = False
                break
            if match:
                return True

        return False