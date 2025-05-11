# Leetcode 1415: The k-th Lexicographical String of All Happy Strings of Length n
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Generates the k-th lexicographical happy string of length n.

        A happy string is a string that only contains the letters 'a', 'b', and 'c',
        and no two adjacent characters are the same.

        Args:
            n: The length of the happy string.
            k: The lexicographical rank of the desired happy string (1-indexed).

        Returns:
            The k-th lexicographical happy string of length n, or an empty string
            if k is greater than the total number of happy strings of length n.

        """

        total_happy_strings = 3 * (2 ** (n - 1))
        if k > total_happy_strings:
            return ""

        result = ""
        count = 0
        chars = ["a", "b", "c"]

        def backtrack(current_string):
            nonlocal result, count
            if count == k:
                return

            if len(current_string) == n:
                count += 1
                if count == k:
                    result = current_string
                return

            for char in chars:
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)

        backtrack("")
        return result