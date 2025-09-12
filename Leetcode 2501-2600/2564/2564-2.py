# Leetcode 2564: Substring XOR Queries
# https://leetcode.com/problems/substring-xor-queries/
# Solved on 12th of September, 2025
class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        """
        Finds the shortest substring in `s` whose integer value equals the XOR sum of each query pair.

        Args:
            s (str): The binary string.
            queries (list[list[int]]): A list of query pairs [first, second].
        Returns:
            list[list[int]]: A list of [start_index, end_index] for each query, or [-1, -1] if not found.
        """
        n = len(s)
        seen = {}
        MAX_LEN = 31

        # Build map of value
        for i in range(n):
            val = 0
            # Expand up to MAX_LEN bits from i
            for j in range(i, min(n, i + MAX_LEN)):
                val = (val << 1) | (1 if s[j] == '1' else 0)
                # Store if not seen or if this substring is strictly better
                if val not in seen:
                    seen[val] = [i, j]
                else:
                    prev_l, prev_r = seen[val]
                    prev_len = prev_r - prev_l + 1
                    curr_len = j - i + 1
                    # Prefer shorter, then smaller left index
                    if curr_len < prev_len or (curr_len == prev_len and i < prev_l):
                        seen[val] = [i, j]
                # No need to consider enormously large values (queries limited to <=1e9)
                if val > 10 ** 9:
                    break

        # Answer queries
        ans = []
        for first, second in queries:
            target = first ^ second
            if target in seen:
                ans.append(seen[target])
            else:
                ans.append([-1, -1])
        return ans