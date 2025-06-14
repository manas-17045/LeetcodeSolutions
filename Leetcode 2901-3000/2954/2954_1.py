# Leetcode 2954: Count the Number of Infection Sequences
# https://leetcode.com/problems/count-the-number-of-infection-sequences/
# Solved on 3rd of November, 2024

class Solution:
    def numberOfSequence(self, n: int, sick: list[int]) -> int:
        """
        Calculates the number of possible infection sequences.

        Args:
            n: The total number of people.
            sick: A list of indices of people who are initially sick.

        Returns:
            The number of possible infection sequences modulo 10^9 + 7.
        """

        MOD = 1_000_000_007

        factorials = [1] * (n + 1)
        factorial_inverses = [1] * (n + 1)

        for i in range(2, (n + 1)):
            factorials[i] = (factorials[i - 1] * i) % MOD

        factorial_inverses[n] = pow(factorials[n], (MOD - 2), MOD)

        for i in range((n - 1), -1, -1):
            factorial_inverses[i] = (factorial_inverses[i + 1] * (i + 1)) % MOD

        result = factorials[n - len(sick)]
        prev_sick = -1

        for i, curr_sick in enumerate(sick):
            healthy = curr_sick - prev_sick - 1
            prev_sick = curr_sick

            if healthy == 0:
                continue

            result = (result * factorial_inverses[healthy]) % MOD

            if i > 0:
                result = (result * pow(2, (healthy - 1), MOD)) % MOD

        last_healthy = n - sick[-1] - 1
        if last_healthy > 0:
            result = (result * factorial_inverses[last_healthy]) % MOD

        return result