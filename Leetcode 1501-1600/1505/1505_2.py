# Leetcode 1505: Minimum Possible Integer After at Most K Adjacent Swaps On Digits
# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
# Solved on 19th of June, 2025
from collections import deque


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        # For each digit 0-9, keep a deque of its indices in 'num'
        pos = [deque() for _ in range(10)]
        for i, ch in enumerate(num):
            pos[int(ch)].append(i)

        # Fenwick / BIT for counting how many "alive" chars remain up to each index
        class BIT:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)

            def update(self, i, v):
                # i is 1-based
                while i <= self.n:
                    self.tree[i] += v
                    i += i & -i

            def query(self, i):
                # Sum from 1...i
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s

        bit = BIT(n)
        # Initially, every position is "alive" (=1)
        for i in range(1, (n + 1)):
            bit.update(i, 1)

        ans = []
        # Build result one character at a time
        for _ in range(n):
            # Try the smallest possible digit
            for d in range(10):
                if not pos[d]:
                    continue
                orig_idx = pos[d][0]
                # How many alive positions before orig_idx?
                # alive count up to orig_idx (1-based) minus one
                cost = bit.query(orig_idx + 1) - 1
                if cost <= k:
                    # We can afford to bring this digit forward
                    k -= cost
                    pos[d].popleft()
                    bit.update((orig_idx + 1), -1)
                    ans.append(str(d))
                    break

        return "".join(ans)