# Leetcode 1052: Grumpy Bookstore Owner
# https://leetcode.com/problems/grumpy-bookstore-owner/
# Solved on 5th of March, 2026
class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        """
        Calculates the maximum number of satisfied customers by using a technique to suppress grumpiness.

        :param customers: List of integers representing the number of customers at each minute.
        :param grumpy: Binary list where 1 indicates the owner is grumpy and 0 otherwise.
        :param minutes: Number of consecutive minutes the owner can use the technique to stay calm.
        :return: The maximum total number of satisfied customers possible.
        """
        baseSatisfied = 0
        currentAdditional = 0
        maxAdditional = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                baseSatisfied += customers[i]
            else:
                currentAdditional += customers[i]

            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    currentAdditional -= customers[i - minutes]

            if currentAdditional > maxAdditional:
                maxAdditional = currentAdditional

        return baseSatisfied + maxAdditional