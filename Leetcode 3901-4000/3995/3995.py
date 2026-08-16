# Leetcode 3995: Minimum Cost to Convert String III
# https://leetcode.com/problems/minimum-cost-to-convert-string-iii/
# Solved on 16th of August, 2026
class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        """
        Calculates the minimum cost to convert the source string to the target string.
        
        @param source: The source string.
        @param target: The target string.
        @param rules: The rules for converting the source string.
        @param costs: The costs for the rules.
        @return: The minimum cost to convert the source string to the target string.
        """
        sourceLength = len(source)
        if source == target:
            return 0

        parsedRules = {}
        for i in range(len(rules)):
            rulePattern = rules[i][0]
            ruleReplacement = rules[i][1]
            ruleCost = costs[i] + rulePattern.count('*')
            ruleLength = len(rulePattern)

            if ruleLength not in parsedRules:
                parsedRules[ruleLength] = []

            parsedRules[ruleLength].append((rulePattern, ruleReplacement, ruleCost))

        minCosts = [float('inf')] * (sourceLength + 1)
        minCosts[0] = 0

        for i in range(sourceLength):
            if minCosts[i] == float('inf'):
                continue

            if source[i] == target[i]:
                if minCosts[i] < minCosts[i + 1]:
                    minCosts[i + 1] = minCosts[i]

            for ruleLength, ruleList in parsedRules.items():
                if i + ruleLength <= sourceLength:
                    targetSlice = target[i : i + ruleLength]
                    sourceSlice = source[i : i + ruleLength]

                    for rulePattern, ruleReplacement, ruleCost in ruleList:
                        if targetSlice == ruleReplacement:
                            isValidMatch = True
                            for j in range(ruleLength):
                                if rulePattern[j] != '*' and rulePattern[j] != sourceSlice[j]:
                                    isValidMatch = False
                                    break

                            if isValidMatch:
                                nextCost = minCosts[i] + ruleCost
                                if nextCost < minCosts[i + ruleLength]:
                                    minCosts[i + ruleLength] = nextCost

        return int(minCosts[sourceLength]) if minCosts[sourceLength] != float('inf') else -1