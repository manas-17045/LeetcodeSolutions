# Leetcode 1655: Distribute Repeating Integers
# https://leetcode.com/problems/distribute-repeating-integers/
# Solved on 25th of July, 2025
import collections


class Solution:
    def canDistribute(self, nums: list[int], quantity: list[int]) -> bool:
        """
        Determines if it's possible to distribute items to customers such that each customer
        receives their requested quantity of items, using the available unique item types.
        :param nums: A list of integers representing the available items.
        :param quantity: A list of integers representing the quantity of items each customer wants.
        :return: True if it's possible to distribute items, False otherwise.
        """
        countsMap = collections.Counter(nums)
        itemCounts = list(countsMap.values())

        numCustomers = len(quantity)
        numUniqueItems = len(itemCounts)

        quantity.sort(reverse=True)

        subsetSums = [0] * (1 << numCustomers)
        for i in range(1, 1 << numCustomers):
            lowestBit = i & -i
            prevMask = i ^ lowestBit
            idx = lowestBit.bit_length() - 1
            subsetSums[i] = subsetSums[prevMask] + quantity[idx]

        memo = {}

        def solve(itemIndex, customerMask):
            if customerMask == (1 << numCustomers) - 1:
                return True

            if itemIndex == numUniqueItems:
                return False

            state = (itemIndex, customerMask)
            if state in memo:
                return memo[state]

            # Option 1: Skip this item type.
            if solve((itemIndex + 1), customerMask):
                memo[state] = True
                return True

            # Option 2: Use this item type to satisfy a subset of remaining customers.
            unhappyMask = ((1 << numCustomers) - 1) & ~customerMask
            currentCount = itemCounts[itemIndex]

            submask = unhappyMask
            while submask> 0:
                if subsetSums[submask] <= currentCount:
                    if solve(itemIndex + 1, customerMask | submask):
                        memo[state] = True
                        return True
                submask = (submask - 1) & unhappyMask

            memo[state] = False
            return False

        return solve(0, 0)