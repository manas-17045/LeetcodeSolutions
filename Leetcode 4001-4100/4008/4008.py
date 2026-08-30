# Leetcode 4008: Minimum Initial Strength to Defeat All Monsters
# https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/
# Solved on 30th of August, 2026
class Solution:
    def minIntialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        """
        Calculates the minimum initial strength required to defeat all monsters.

        Parameters:
            monsters (list[int]): An array representing the strength of each monster.
            boosts (list[list[int]]): A list of boost ranges and values in the form [left, right, value].

        Returns:
            int: The minimum non-negative initial strength needed to defeat all monsters.
        """
        numMonsters = len(monsters)
        bonusDiff = [0] * (numMonsters + 1)

        for startIdx, endIdx, bValue in boosts:
            bonusDiff[startIdx] += bValue
            bonusDiff[endIdx + 1] -= bValue

        minStrength = 0
        prefixSum = 0
        cBonus = 0

        for idx in range(numMonsters):
            cBonus += bonusDiff[idx]
            mStrength = monsters[idx]
            if mStrength > cBonus:
                minStrength = max(minStrength, prefixSum + mStrength - cBonus)
            prefixSum += mStrength
        
        return minStrength