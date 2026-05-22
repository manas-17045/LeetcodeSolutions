# Leetcode 3921: Score Validator
# https://leetcode.com/problems/score-validator/
# Solved on 22nd of May, 2026
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        """
        Validates and calculates the final score and event counter based on a list of events.

        :param events: A list of strings representing game events.
        :return: A list of two integers: [final score, event counter].
        """
        currentScore = 0
        currentCounter = 0

        for currentEvent in events:
            if currentEvent == "W":
                currentCounter += 1
                if currentCounter == 10:
                    break
            elif currentEvent in ("WD", "NB"):
                currentScore += 1
            else:
                currentScore += int(currentEvent)

        return [currentScore, currentCounter]