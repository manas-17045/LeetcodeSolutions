# Leetcode 2977: Minimum Cost to Convert String II
# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/
# Solved on 14th of September, 2025
class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        Calculates the minimum cost to convert the source string to the target string.

        Args:
            source (str): The original string.
            target (str): The target string to convert to.
            original (list[str]): A list of strings that can be converted.
            changed (list[str]): A list of strings that `original` strings can be changed to.
            cost (list[int]): The cost associated with each conversion from `original[i]` to `changed[i]`.

        Returns:
            int: The minimum cost to convert `source` to `target`. Returns -1 if conversion is not possible.
        """

        inf = float('inf')

        uniqueStrings = set(original) | set(changed)
        stringToId = {s: i for i, s in enumerate(uniqueStrings)}
        numStrings = len(uniqueStrings)

        dist = [[inf] * numStrings for _ in range(numStrings)]

        for i in range(numStrings):
            dist[i][i] = 0

        for i in range(len(original)):
            o = original[i]
            c = changed[i]
            co = cost[i]

            if o in stringToId and c in stringToId:
                u = stringToId[o]
                v = stringToId[c]
                dist[u][v] = min(dist[u][v], float(co))

        for k in range(numStrings):
            for i in range(numStrings):
                for j in range(numStrings):
                    if dist[i][k] != inf and dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        trie = {}
        for s, sId in stringToId.items():
            node = trie
            for char in s:
                node = node.setdefault(char, {})
            node['id'] = sId

        n = len(source)
        dp = [inf] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            # No-op if characters match
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            # Substring transformations
            sourcePrefixes = []
            node = trie
            for k in range(i, n):
                char = source[k]
                if char not in node:
                    break
                node = node[char]
                if 'id' in node:
                    sourcePrefixes.append((node['id'], k - i + 1))

            targetPrefixesMap = {}
            node = trie
            for k in range(i, n):
                char = target[k]
                if char not in node:
                    break
                node = node[char]
                if 'id' in node:
                    targetPrefixesMap[k - i + 1] = node['id']

            for u, length in sourcePrefixes:
                if length in targetPrefixesMap:
                    v = targetPrefixesMap[length]
                    j = i + length
                    transformCost = dist[u][v]
                    if transformCost != inf and dp[j] != inf:
                        dp[i] = min(dp[i], transformCost + dp[j])

        result = dp[0]
        return int(result) if result != inf else -1