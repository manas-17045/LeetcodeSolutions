# Leetcode 3777: Minimum Deletions to Make Alternating Substring
# https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/
# Solved on 24th of December, 2025
class Solution:
    def minDeletions(self, s: str, queries: list[list[int]]) -> list[int]:
        """
        Calculates the minimum deletions required to make substrings alternating based on queries.

        Args:
            s: The initial binary string (consisting of 'A' and 'B').
            queries: A list of queries. Each query is either a type 1 (flip character) or type 2 (count deletions).
        Returns:
            A list of integers, where each integer is the result of a type 2 query.
        """
        n = len(s)
        chars = list(s)
        bit = [0] * (n + 1)

        def update(index, val):
            i = index + 1
            while i <= n:
                bit[i] += val
                i += i & (-i)

        def query(index):
            i = index + 1
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & (-i)
            return total

        for i in range(n - 1):
            if chars[i] == chars[i + 1]:
                update(i, 1)

        result = []
        for q in queries:
            if q[0] == 1:
                idx = q[1]
                left = idx - 1

                if left >= 0:
                    isSame = 1 if chars[left] == chars[idx] else 0
                    update(left, 1 - 2 * isSame)

                if idx < n - 1:
                    isSame = 1 if chars[idx] == chars[idx + 1] else 0
                    update(idx, 1 - 2 * isSame)

                chars[idx] = 'B' if chars[idx] == 'A' else 'A'
            else:
                l, r = q[1], q[2]
                if l >= r:
                    result.append(0)
                else:
                    count = query(r - 1) - query(l - 1)
                    result.append(count)

        return result