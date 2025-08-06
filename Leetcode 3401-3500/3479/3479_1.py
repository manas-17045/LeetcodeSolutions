# Leetcode 3479: Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii/
# Solved on 6th of August, 2025
class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        """
        Calculates the number of fruits that cannot be placed into baskets.

        This function uses a segment tree to efficiently find a suitable basket for each fruit.
        A fruit can be placed in a basket if the basket's capacity is greater than or equal to the fruit's size.
        Each basket can only hold one fruit.

        Args:
            fruits: A list of integers representing the sizes of the fruits.
            baskets: A list of integers representing the capacities of the baskets.

        Returns:
            The number of fruits that could not be placed in any basket.
        """
        numBaskets = len(baskets)
        numFruits = len(fruits)

        if numBaskets == 0:
            return numFruits
        
        segTree = [0] * (4 * numBaskets)

        def build(node, start, end):
            if start == end:
                segTree[node] = baskets[start]
                return
            
            mid = (start + end) // 2
            leftNode = 2 * node
            rightNode = 2 * node + 1

            build(leftNode, start, mid)
            build(rightNode, mid + 1, end)
            
            segTree[node] = max(segTree[leftNode], segTree[rightNode])

        def update(node, start, end, idx):
            if start == end:
                segTree[node] -= 1
                return
            
            mid = (start + end) // 2
            leftNode = 2 * node
            rightNode = 2 * node + 1

            if start <= idx <= mid:
                update(leftNode, start, mid, idx)
            else:
                update(rightNode, mid + 1, end, idx)
            
            segTree[node] = max(segTree[leftNode], segTree[rightNode])
            
        def query(node, start, end, fruitSize):
            if segTree[node] < fruitSize:
                return -1
            
            if start == end:
                return start
            
            mid = (start + end) // 2
            leftNode = 2 * node
            rightNode = 2 * node + 1

            if segTree[leftNode] >= fruitSize:
                res = query(leftNode, start, mid, fruitSize)
                if res != -1:
                    return res
                
            return query(rightNode, mid + 1, end, fruitSize)
        
        build(1, 0, numBaskets - 1)

        placedCount = 0
        for fruit in fruits:
            basketIndex = query(1, 0, numBaskets - 1, fruit)
            if basketIndex != -1:
                placedCount += 1
                update(1, 0, numBaskets - 1, basketIndex)
                
        return numFruits - placedCount