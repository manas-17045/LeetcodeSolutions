# Leetcode 3494: Find the Minimum Amount of Time to Brew Potions
# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/
# Solved on 9th of October, 2025
class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        """
        Calculates the minimum time to complete all skills using a sequence of potions.
        :param skill: A list of integers representing the skill points required for each task.
        :param mana: A list of integers representing the mana multiplier for each potion.
        :return: An integer representing the minimum total time to complete all skills.
        """
        n = len(skill)
        m = len(mana)
        # Prefix sums for potion 0
        prev_prefix = [0] * n
        s = 0
        mul0 = mana[0]
        for i in range(n):
            s += skill[i] * mul0
            prev_prefix[i] = s

        # If only one potion, its total processing time is the answer
        if m == 1:
            return prev_prefix[-1]

        S_prev = 0  # S_0 = 0
        # Iterate potions 1..m-1
        for j in range(1, m):
            mul = mana[j]
            cur_prefix = [0] * n
            s = 0
            for i in range(n):
                s += skill[i] * mul
                cur_prefix[i] = s

            # Compute S_j = max_i (S_{j-1} + prev_prefix[i] - cur_prefix[i-1])
            best = -10 ** 30
            Sp = S_prev
            Aprev = prev_prefix
            Acur = cur_prefix
            for i in range(n):
                left = Aprev[i]
                right = Acur[i - 1] if i > 0 else 0
                cand = Sp + left - right
                if cand > best:
                    best = cand

            S_prev = best
            prev_prefix = cur_prefix

        # Final completion time = start of last potion + total time of last potion
        return S_prev + prev_prefix[-1]