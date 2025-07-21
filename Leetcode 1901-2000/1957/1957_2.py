# Leetcode 1957: Delete Characters to Make Fancy String
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# Solved on 21st of July, 2025
class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Makes a "fancy" string by removing consecutive triplets of the same character.

        Args:
            s (str): The input string.

        Returns:
            str: The "fancy" string.
        """
        res = []
        for c in s:
            if len(res) >= 2 and res[-1] == res[-2] == c:
                continue
            res.append(c)
        return ''.join(res)