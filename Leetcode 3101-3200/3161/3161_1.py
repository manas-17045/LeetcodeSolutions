# Leetcode 3161: Block Placement Queries
# https://leetcode.com/problems/block-placement-queries/
# Solved on 6th of August, 2025
class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        """
        Processes a series of block placement queries on a 1D line.

        There are two types of queries:
        1. Type 1: Place an obstacle at a given coordinate.
           - query[0] == 1
           - query[1] == coordinate of the obstacle
        2. Type 2: Check if a block of a certain size can be placed within a given range.
           - query[0] == 2
           - query[1] == x (the end coordinate of the range [0, x])
           - query[2] == sz (the required size of the block)

        The function determines for each Type 2 query if there's a continuous
        segment of at least size `sz` available in the interval `[0, x]`.

        Args:
            queries: A list of queries, where each query is a list of integers.

        Returns:
            A list of booleans, where each boolean is the result of a Type 2
            query in the order they appeared in the input.
        """

        allCoords = {0}
        for q in queries:
            allCoords.add(q[1])

        sortedCoords = sorted(list(allCoords))
        coordToIndex = {c: i for i, c in enumerate(sortedCoords)}

        numCoords = len(sortedCoords)
        deltas = [sortedCoords[i + 1] - sortedCoords[i] for i in range(numCoords - 1)]

        numIntervals = len(deltas)
        if numIntervals == 0:
            results = []
            for q in queries:
                if q[0] == 2:
                    results.append(q[1] >= q[2])
            return results
        
        segTree = [None] * (4 * numIntervals)
        isObstacle = [False] * numCoords

        initialObstacles = {q[1] for q in queries if q[0] == 1}
        isObstacle[0] = True
        for obs in initialObstacles:
            isObstacle[coordToIndex[obs]] = True

        def merge(left, right, boundaryIndex):
            maxL, prefixL, suffixL, totalL = left
            maxR, prefixR, suffixR, totalR = right
            
            total = totalL + totalR
            if isObstacle[boundaryIndex]:
                mergedMax = max(maxL, maxR)
                prefix = prefixL
                suffix = suffixR
            else:
                mergedMax = max(maxL, maxR, suffixL + prefixR)
                prefix = prefixL
                if prefixL == totalL:
                    prefix = totalL + prefixR
                suffix = suffixR
                if suffixR == totalR:
                    suffix = totalR + suffixL

            return (mergedMax, prefix, suffix, total)

        def build(nodeIndex, start, end):
            if start == end:
                val = deltas[start]
                segTree[nodeIndex] = (val, val, val, val)
                return
            
            mid = (start + end) // 2
            build(2 * nodeIndex + 1, start, mid)
            build(2 * nodeIndex + 2, mid + 1, end)
            segTree[nodeIndex] = merge(segTree[2 * nodeIndex + 1], segTree[2 * nodeIndex + 2], mid + 1)

        def update(nodeIndex, start, end, boundaryIdx):
            if start > boundaryIdx or end < boundaryIdx - 1:
                return

            if start != end:
                mid = (start + end) // 2
                update(2 * nodeIndex + 1, start, mid, boundaryIdx)
                update(2 * nodeIndex + 2, mid + 1, end, boundaryIdx)
                segTree[nodeIndex] = merge(segTree[2 * nodeIndex + 1], segTree[2 * nodeIndex + 2], mid + 1)
        
        def query(nodeIndex, start, end, queryStart, queryEnd):
            if queryStart > queryEnd or start > queryEnd or end < queryStart:
                return (0, 0, 0, 0)
            
            if queryStart <= start and end <= queryEnd:
                return segTree[nodeIndex]
            
            mid = (start + end) // 2
            
            if queryEnd <= mid:
                return query(2*nodeIndex+1, start, mid, queryStart, queryEnd)
            if queryStart > mid:
                return query(2*nodeIndex+2, mid+1, end, queryStart, queryEnd)

            leftRes = query(2 * nodeIndex + 1, start, mid, queryStart, queryEnd)
            rightRes = query(2 * nodeIndex + 2, mid + 1, end, queryStart, queryEnd)
            
            return merge(leftRes, rightRes, mid + 1)
        
        build(0, 0, numIntervals - 1)

        queryResults = {}

        for i in range(len(queries) - 1, -1, -1):
            q = queries[i]
            if q[0] == 1:
                obsPos = q[1]
                idx = coordToIndex[obsPos]
                if isObstacle[idx]:
                    isObstacle[idx] = False
                    if idx > 0 and idx < numCoords:
                        update(0, 0, numIntervals - 1, idx)

            else:
                x, sz = q[1], q[2]
                idxX = coordToIndex[x]
                maxGap = 0
                if idxX > 0:
                    maxGap = query(0, 0, numIntervals - 1, 0, idxX - 1)[0]

                queryResults[i] = (maxGap >= sz)

        finalResults = []
        for i in range(len(queries)):
            if i in queryResults:
                finalResults.append(queryResults[i])

        return finalResults