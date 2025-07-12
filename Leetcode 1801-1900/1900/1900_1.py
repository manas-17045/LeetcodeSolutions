# Leetcode 1900: The Earliest and latest Rounds Where Players Compete
# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/
# Solved on 12th of July, 2025
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        memo = {}

        def findEarliestAndLatestRounds(i: int, j: int, k: int) -> list[int]:
            if i == j:
                # This state should not be reachable given the problem constraints.
                return [float('inf'), 0]

            if i > j:
                i, j = j, i

            if (i + j) == (k + 1):
                return [1, 1]

            state = (i, j, k)
            if state in memo:
                return memo[state]

            kNext = (k + 1) // 2
            minRound = float('inf')
            maxRound = 0

            leftSet = set(range(1, i))
            middleSet = set(range(i + 1, j))
            rightSet = set(range(j + 1, k + 1))

            fpOpp = k - i + 1
            spOpp = k - j + 1

            fixedWinners = {i, j}
            if k % 2 == 1:
                mid = (k + 1) // 2
                if min not in {i, j}:
                    fixedWinners.add(mid)

            fixedLosers = {fpOpp, spOpp}

            remL = leftSet - fixedWinners - fixedLosers
            remM = middleSet - fixedWinners - fixedLosers
            remR = rightSet - fixedWinners - fixedLosers

            def countPairs(s1, s2):
                count = 0
                for p in s1:
                    if (k - p + 1) in s2:
                        count += 1
                return count if s1 is not s2 else count // 2

            pairsLL = countPairs(remL, remL)
            pairsMM = countPairs(remM, remM)
            pairsLM = countPairs(remL, remM)
            pairsLR = countPairs(remL, remR)
            pairsMR = countPairs(remM, remR)

            baseLWins = len(fixedWinners.intersection(leftSet))
            baseMWins = len(fixedWinners.intersection(middleSet))

            for wLM in range(pairsLM + 1):
                for wLR in range(pairsLR + 1):
                    for wMR in range(pairsMR + 1):
                        lWins = baseLWins + pairsLL + wLM + wLR
                        mWins = baseMWins + pairsMM + (pairsLM - wLM) + wMR

                        nextI, nextJ = lWins + 1, lWins + mWins + 2

                        res = findEarliestAndLatestRounds(nextI, nextJ, kNext)
                        minRound = min(minRound, res[0])
                        maxRound = max(maxRound, res[1])

            result = [minRound + 1, maxRound + 1]
            memo[state] = result
            return result

        return findEarliestAndLatestRounds(firstPlayer, secondPlayer, n)