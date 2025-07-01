# Leetcode 3330: Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i/
# Solved on 1st of July, 2025
class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        Calculates the number of possible original strings that could have resulted in the given `word`
        after a single long-press operation.

        A long-press operation means replacing a character 'c' with 'cc', 'ccc', etc.
        Only one such long-press operation is allowed in the entire string.
        """
        n = len(word)
        if n == 0:
            # Empty string: only one possibility
            return 1

        # Start with the "no long-press" case
        count = 1
        i = 0
        while i < n:
            j = i + 1
            # Find end of the current run
            while j < n and word[j] == word[i]:
                j += 1
            run_len = j - i

            # If this run could be the one long-press, add (run_len - 1)
            if run_len >= 2:
                count += run_len - 1

            i = j

        return count