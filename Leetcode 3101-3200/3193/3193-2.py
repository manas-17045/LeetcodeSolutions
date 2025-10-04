# Leetcode 3193: Count the Number of Inversions
# https://leetcode.com/problems/count-the-number-of-inversions/
# Solved on 4th of October, 2025
class Solution:
    def numberOfPermutations(self, n: int, requirements: list[list[int]]) -> int:
        """
        Calculates the number of permutations of length `n` that satisfy the given inversion count requirements.
        :param n: The length of the permutation.
        :param requirements: A list of lists, where each inner list `[end, cnt]` specifies that the prefix of length
                            `end + 1` must have exactly `cnt` inversions.

        :returns: The number of valid permutations modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7

        req = {end: cnt for end, cnt in requirements}

        dp_prev = [1]

        if 0 in req:
            if req[0] != 0:
                return 0

        for s in range(2, n + 1):
            max_prev = len(dp_prev) - 1
            max_cur = s * (s - 1) // 2
            dp_cur = [0] * (max_cur + 1)

            pref = [0] * (max_prev + 1)
            running = 0
            for i in range(max_prev + 1):
                running += dp_prev[i]
                if running >= 1 << 63:
                    running %= MOD
                pref[i] = running % MOD

            for k in range(0, max_cur + 1):
                lower = k - (s - 1)
                if lower <= 0:
                    upper = min(k, max_prev)
                    if upper >= 0:
                        dp_cur[k] = pref[upper]
                    else:
                        dp_cur[k] = 0
                else:
                    if lower > max_prev:
                        dp_cur[k] = 0
                    else:
                        upper = min(k, max_prev)
                        if upper < lower:
                            dp_cur[k] = 0
                        else:
                            dp_cur[k] = (pref[upper] - (pref[lower - 1] if lower - 1 >= 0 else 0)) % MOD

            end = s - 1
            if end in req:
                required = req[end]
                if required < 0 or required > max_cur:
                    return 0
                val = dp_cur[required] % MOD
                dp_cur = [0] * (max_cur + 1)
                dp_cur[required] = val

            dp_prev = dp_cur

        return sum(dp_prev) % MOD