# Leetcode 4059: Lexicographically Largest Power Array
# https://leetcode.com/problems/lexicographically-largest-power-array/
# Solved on 27th of October, 2026
class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        """
        Calculates the lexicographically largest power array by optimally rearranging the elements based on set bits.

        Args:
            nums (list[int]): A list of integers representing the input array.

        Returns:
            list[int]: A list of 15 integers representing the maximized power array.
        """
        powerArray = [0] * 15
        currentGroups = [nums]

        for bitIndex in range(15):
            shiftAmount = 14 - bitIndex
            passedCount = 0
            nextGroups = []
            hasSplit = False

            for group in currentGroups:
                if hasSplit:
                    nextGroups.append(group)
                    continue

                setElements = []
                unsetElements = []

                for num in group:
                    if (num >> shiftAmount) & 1:
                        setElements.append(num)
                    else:
                        unsetElements.append(num)

                if len(setElements) == len(group):
                    passedCount += len(group)
                    nextGroups.append(group)
                else:
                    powerArray[bitIndex] = passedCount + len(setElements)

                    if setElements:
                        nextGroups.append(setElements)
                    
                    if unsetElements:
                        nextGroups.append(unsetElements)

                    hasSplit = True

            if not hasSplit:
                powerArray[bitIndex] = passedCount

            currentGroups = nextGroups

        return powerArray