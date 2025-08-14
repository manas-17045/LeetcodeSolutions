# Leetcode 3324: Find the Sequence of Strings Appeared on the Screen
# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/
# Solved on 14th of August, 2025
class Solution:
    def stringSequence(self, target: str) -> list[str]:
        """
        Generates a sequence of strings representing the intermediate states of a screen
        as characters are typed and incremented to form the target string.
        :param target: The final string to be formed.
        :return: A list of strings, each representing a state of the screen.
        """
        res: list[str] = []
        # Represent current screen as list of chars for efficient updates
        cur = []
        for ch in target:
            # Press key1: append 'a'
            cur.append('a')
            res.append("".join(cur))
            # Number of increments needed from 'a' to ch (0...25)
            steps = (ord(ch) - ord('a')) % 26
            for _ in range(steps):
                # Increment the last character with wrap
                last = cur[-1]
                cur[-1] = chr((ord(last) - ord('a') + 1) % 26 + ord('a'))
                res.append("".join(cur))

        return res