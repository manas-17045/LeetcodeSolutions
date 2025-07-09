# Leetcode 2272: Substrings With Largest Variance
# https://leetcode.com/problems/substrings-with-largest-variance/
# Solved on 9th of July, 2025
class Solution:
    def largestVariance(self, s: str) -> int:
        """
        Calculates the largest variance between the counts of two different characters in a string.

        The variance is defined as the maximum difference between the count of a 'major' character
        and a 'minor' character in any substring.

        Args:
            s: The input string.

        Returns:
            The largest variance found.
        """
        letters = set(s)
        if len(letters) < 2:
            return 0

        ans = 0
        for major in letters:
            for minor in letters:
                if major == minor:
                    continue

                # Do two passes: forward and backward
                for seq in (s, reversed(s)):
                    curr = 0
                    has_minor = False
                    for c in seq:
                        if c == major:
                            curr += 1
                        elif c == minor:
                            curr -= 1
                            has_minor = True
                        else:
                            continue

                        # Only update once we have at least one minor
                        if has_minor:
                            ans = max(ans, curr)

                        # If our running sum goes negative, restart
                        if curr < 0:
                            curr = 0
                            has_minor = False

        return ans