# Leetcode 831: Push Dominoes
# https://leetcode.com/problems/push-dominoes/
# Solved on

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Processes the given string of dominoes to determine their final positions after applying the forces
        caused by right-falling ('R') and left-falling ('L') dominoes. The dominoes are represented as a
        sequence of 'L', 'R', and '.', where 'L' represents a leftward-falling domino, 'R' represents a
        rightward-falling domino, and '.' represents a domino that is initially stable.

        :param dominoes: A string representing the initial positions of the dominoes.
        :return: A string representing the final positions of the dominoes after all forces are applied.
        :rtype: str
        """
        # Convert the string to a list for easier implementation
        dominoes = list(dominoes)
        n = len(dominoes)

        # Initialize forces array to track the net force on each domino
        forces = [0] * n

        # Process forces from left to right (right-falling dominoes)
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                # Starting a new rightward force
                force = n
            elif dominoes[i] == 'L':
                # Leftward dominoes stop rightward force
                force = 0
            else:
                # Decrement force (it diminishes with distance)
                force = max(force - 1, 0)

            forces[i] += force

        # Process forces from right to left (left-falling dominoes)
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                # Starting a new leftward force
                force = n
            elif dominoes[i] == 'R':
                # Rightward dominoes stop leftward force
                force = 0
            else:
                # Decrement force (it diminishes with distance)
                force = max(force - 1, 0)

            # Subtract the leftward force (negative force means falling left)
            forces[i] -= force

        # Determine final states based on net forces
        result = []
        for i in range(n):
            if forces[i] > 0:
                result.append('R')
            elif forces[i] < 0:
                result.append('L')
            else:
                result.append('.')

        return "".join(result)