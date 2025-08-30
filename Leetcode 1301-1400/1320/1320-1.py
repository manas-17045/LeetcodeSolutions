# Leetcode 1320: Minimum Distance to Type a Word Using Two Fingers
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
# Solved on 30th of August, 2025
class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        Calculates the minimum distance to type a given word using two fingers.

        Args:
            word (str): The word to type.
        Returns:
            int: The minimum total distance traveled by the two fingers.
        """
        memo = {}
        coords = {chr(ord('A') + i): (i // 6, i % 6) for i in range(26)}

        def getDist(fingerOne, fingerTwo):
            if fingerOne is None or fingerTwo is None:
                return 0
            posOne = coords[fingerOne]
            posTwo = coords[fingerTwo]
            return abs(posOne[0] - posTwo[0]) + abs(posOne[1] - posTwo[1])

        def solve(index, otherFinger):
            if index == len(word):
                return 0

            state = (index, otherFinger)
            if state in memo:
                return memo[state]

            firstFinger = word[index - 1]
            targetChar = word[index]

            resOne = getDist(firstFinger, targetChar) + solve(index + 1, otherFinger)
            resTwo = getDist(otherFinger, targetChar) + solve(index + 1, firstFinger)

            result = min(resOne, resTwo)
            memo[state] = result
            return result

        if len(word) == 0:
            return 0

        return solve(1, None)