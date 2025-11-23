# Leetcode 3072: Distribute Elements Into Two Arrays II
# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/
# Solved on 23rd of November, 2025
class BinaryIndexedTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, index):
        while index < len(self.tree):
            self.tree[index] += 1
            index += index & (-index)

    def query(self, index):
        summ = 0
        while index > 0:
            summ += self.tree[index]
            index -= index & (-index)
        return summ


class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        """
        Distributes elements into two arrays based on a specific comparison rule.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            list[int]: The concatenated result of the two arrays after distribution.
        """
        sortedNums = sorted(list(set(nums)))
        rankMap = {val: i + 1 for i, val in enumerate(sortedNums)}
        maxRank = len(sortedNums)

        bitOne = BinaryIndexedTree(maxRank)
        bitTwo = BinaryIndexedTree(maxRank)

        arrOne = [nums[0]]
        arrTwo = [nums[1]]

        bitOne.add(rankMap[nums[0]])
        bitTwo.add(rankMap[nums[1]])

        for i in range(2, len(nums)):
            currentVal = nums[i]
            currentRank = rankMap[currentVal]

            greaterCountOne = len(arrOne) - bitOne.query(currentRank)
            greaterCountTwo = len(arrTwo) - bitTwo.query(currentRank)

            if greaterCountOne > greaterCountTwo:
                arrOne.append(currentVal)
                bitOne.add(currentRank)
            elif greaterCountOne < greaterCountTwo:
                arrTwo.append(currentVal)
                bitTwo.add(currentRank)
            else:
                if len(arrOne) <= len(arrTwo):
                    arrOne.append(currentVal)
                    bitOne.add(currentRank)
                else:
                    arrTwo.append(currentVal)
                    bitTwo.add(currentRank)

        return arrOne + arrTwo
