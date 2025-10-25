# Leetcode 2591: Distribute Money to Maximum Children
# https://leetcode.com/problems/distribute-money-to-maximum-children/
# Solved on 25th of October, 2025
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        """
        Distributes money to children such that as many children as possible receive exactly $8.

        Args:
            money (int): The total amount of money to distribute.
            children (int): The number of children.
        Returns:
            int: The maximum number of children that can receive exactly $8.
        """
        if money < children:
            return -1

        money -= children

        countEight = money // 7
        remainder = money % 7

        if countEight > children:
            return children - 1

        if countEight == children:
            if remainder == 0:
                return children
            else:
                return children - 1

        childrenLeft = children - countEight

        if childrenLeft == 1 and remainder == 3:
            return countEight - 1

        return countEight