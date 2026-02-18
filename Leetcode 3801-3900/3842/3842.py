# Leetcode 3842: Toggle Light Bulbs
# https://leetcode.com/problems/toggle-light-bulbs/
# Solved on 18th of February, 2026
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        """
        Toggles the state of light bulbs based on the provided list of indices.

        :param bulbs: A list of integers representing the indices of bulbs to toggle.
        :return: A list of integers representing the indices of bulbs that are currently ON.
        """
        bulbStates = [False] * 101
        for currentBulb in bulbs:
            bulbStates[currentBulb] = not bulbStates[currentBulb]

        finalBulbs = []
        for i in range(1, 101):
            if bulbStates[i]:
                finalBulbs.append(i)

        return finalBulbs