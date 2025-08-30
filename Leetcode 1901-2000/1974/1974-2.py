# Leetcode 1974: Minimum Time to Type Word Using Special Typewriter
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
# Solved on 30th of August, 2025
class Solution:
    def minTypeToType(self, word: str) -> int:
        """
        Calculates the minimum time to type a given word on a circular keyboard.
        :param word: The word to be typed.
        :return: The minimum time required to type the word.
        """
        if not word:
            return 0

        time = 0
        cur = ord('a')
        for ch in word:
            target = ord(ch)
            diff = abs(target - cur)
            time += min(diff, (26 - diff))
            time += 1
            cur = target

        return time