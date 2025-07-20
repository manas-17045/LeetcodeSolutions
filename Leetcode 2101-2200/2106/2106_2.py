# Leetcode 2106: Maximum Fruits Harvested After at Most K Steps
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
# Solved on 20th of July, 2025
class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        """
        Calculates the maximum total fruits that can be collected given a starting position and a maximum travel distance k.
        :param fruits: A list of lists, where each inner list `[position, count]` represents the position of a fruit tree and the number of fruits it has.
        :param startPos: The starting position.
        :param k: The maximum total distance that can be traveled.
        :return: The maximum total number of fruits that can be collected.
        """
        # Sort and unzip
        fruits.sort()
        pos = [p for p, _ in fruits]
        pref = [0]
        for _, cnt in fruits:
            pref.append(pref[-1] + cnt)

        def cost(i: int, j: int) -> int:
            left, right = pos[i], pos[j]
            if right <= startPos:
                return startPos - left
            if left >= startPos:
                return right - startPos

            dleft = startPos - left
            dright = right - startPos
            return min(2 * dleft - dright, (dleft + 2 * dright))

        n = len(fruits)
        ans = 0
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j < n and cost(i, j) <= k:
                j += 1
            total = pref[j] - pref[i]
            if total > ans:
                ans = total

        return ans