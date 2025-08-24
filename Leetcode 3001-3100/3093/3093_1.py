# Leetcode 3093: Longest Common Suffix Queries
# https://leetcode.com/problems/longest-common-suffix-queries/
# Solved on 24th of August, 2025
class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        """
        Finds the index of the word in wordsContainer that has the longest common suffix
        with each query word, prioritizing shorter words in case of ties.

        Args:
            wordsContainer: A list of strings to search within.
            wordsQuery: A list of strings to query against wordsContainer.
        Returns:
            A list of integers, where each integer is the index in wordsContainer
            corresponding to the best match for the respective query word.
        """
        trieRoot = {'children': {}, 'shortestLength': float('inf'), 'bestIndex': -1}

        bestIndexForRoot = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[bestIndexForRoot]):
                bestIndexForRoot = i

        trieRoot['shortestLength'] = len(wordsContainer[bestIndexForRoot])
        trieRoot['bestIndex'] = bestIndexForRoot

        for i, word in enumerate(wordsContainer):
            wordLength = len(word)
            currentNode = trieRoot

            for char in reversed(word):
                if char not in currentNode['children']:
                    currentNode['children'][char] = {
                        'children': {},
                        'shortestLength': wordLength,
                        'bestIndex': i
                    }

                currentNode = currentNode['children'][char]

                if wordLength < currentNode['shortestLength']:
                    currentNode['shortestLength'] = wordLength
                    currentNode['bestIndex'] = i

        resultList = []
        for query in wordsQuery:
            currentNode = trieRoot
            bestIndexForQuery = trieRoot['bestIndex']

            for char in reversed(query):
                if char in currentNode['children']:
                    currentNode = currentNode['children'][char]
                    bestIndexForQuery = currentNode['bestIndex']
                else:
                    break

            resultList.append(bestIndexForQuery)

        return resultList