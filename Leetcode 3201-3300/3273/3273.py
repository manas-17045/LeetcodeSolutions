# Leetcode 3273: Minimum Amount of Damage Dealt to Bob
# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/
# Solved on 19th of November, 2025
class Solution:
    def minDamage(self, power: int, damage: list[int], health: list[int]) -> int:
        """
        Calculates the minimum total damage dealt to Bob by strategically ordering enemy attacks.

        Args:
            power: The player's attack power.
            damage: A list of damage values for each enemy.
            health: A list of health values for each enemy.
        Returns:
            The minimum total damage dealt to Bob.
        """
        enemies = []
        for dmg, hp in zip(damage, health):
            killTime = (hp + power - 1) // power
            enemies.append((dmg, killTime))

        enemies.sort(key=lambda x: x[0] / x[1], reverse=True)

        totalDamage = 0
        currentTime = 0

        for dmg, killTime in enemies:
            currentTime += killTime
            totalDamage += dmg * currentTime

        return totalDamage