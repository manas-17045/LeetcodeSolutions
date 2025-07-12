# Leetcode 1900: The Earliest and latest Rounds Where Players Compete
# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/
# Solved on 12th of July, 2025
from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        # convert to "a/b" representation
        a0 = firstPlayer - 1
        b0 = secondPlayer - firstPlayer - 1

        @lru_cache(None)
        def dfs(N: int, a: int, b: int):
            c = N - 2 - a - b
            # if they pair this round, they meet immediately
            if a == c:
                return (1, 1)

            P = N // 2
            has_solo = (N % 2 == 1)
            # fixed survivors in each region
            fixedA = fixedB = fixedC = 0
            branching = []  # list of (reg1,reg2) for matches that could go either way

            def region(pos):
                if pos <= a:
                    return 'A'
                elif pos == a+1:
                    return 'l'
                elif pos <= a+1+b:
                    return 'B'
                elif pos == a+1+b+1:
                    return 'r'
                else:
                    return 'C'

            # scan all pairings
            for k in range(1, P+1):
                p, q = k, N+1-k
                rp, rq = region(p), region(q)
                # if they meet, we would have returned above
                if 'l' in (rp, rq) or 'r' in (rp, rq):
                    continue
                if rp == rq:
                    # same region → one fixed survivor there
                    if rp == 'A':
                        fixedA += 1
                    elif rp == 'B':
                        fixedB += 1
                    else:
                        fixedC += 1
                else:
                    # cross-region → branch
                    branching.append((rp, rq))

            # handle solo if N is odd
            if has_solo:
                solo_pos = (N+1)//2
                rs = region(solo_pos)
                if rs == 'A':
                    fixedA += 1
                elif rs == 'B':
                    fixedB += 1
                elif rs == 'C':
                    fixedC += 1
                # if rs in {'l','r'}: that player just auto-advances

            # build all possible (A,B,C) survivor‐counts after this round
            states = {(fixedA, fixedB, fixedC)}
            for r1, r2 in branching:
                new_states = set()
                for x, y, z in states:
                    # winner from r1
                    if r1 == 'A':
                        new_states.add((x+1, y, z))
                    elif r1 == 'B':
                        new_states.add((x, y+1, z))
                    else:
                        new_states.add((x, y, z+1))
                    # winner from r2
                    if r2 == 'A':
                        new_states.add((x+1, y, z))
                    elif r2 == 'B':
                        new_states.add((x, y+1, z))
                    else:
                        new_states.add((x, y, z+1))
                states = new_states

            # recurse on each possible next (a',b')
            next_N = P + (1 if has_solo else 0)
            best_min, best_max = float('inf'), float('-inf')
            for x, y, z in states:
                # x+y+z = next_N - 2  (we exclude our two players themselves)
                emn, emx = dfs(next_N, x, y)
                best_min = min(best_min, emn)
                best_max = max(best_max, emx)

            # add this round
            return (best_min + 1, best_max + 1)

        e, l = dfs(n, a0, b0)
        return [e, l]