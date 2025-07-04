# Leetcode 831: Push Dominoes
# https://leetcode.com/problems/push-dominoes/
# Solved on

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Update the positions of fallen dominoes based on their initial states and
        the rules of domino falling behavior. Each domino can either be upright
        ('.'), pushed to fall to the right ('R') or pushed to fall to the left ('L').
        The function calculates the final states of the dominoes sequence after all
        dominoes have fallen to their resulting positions.

        :param dominoes: A string representing the initial state of a series of
                         dominoes, where each character is either '.', 'L', or 'R'.
        :return: A string representing the final state of the dominoes after they
                 have come to rest based on their initial arrangements and pushes.
        """
        n = len(dominoes)

        # Create a list of anchor points (indices and symbols 'L'/'R')
        # Include virtual boundaries: 'L' at index -1, 'R' at index n.
        anchors = [(-1, 'L')]
        for i, symbol in enumerate(dominoes):
            if symbol != '.':
                anchors.append((i, symbol))
        anchors.append((n, 'R'))

        # Convert the input string to a list for in-place modification
        res = list(dominoes)

        # Iterate through consecutive pairs of anchors (boundaries)
        for k in range(len(anchors) - 1):
            i, sym_i = anchors[k]   # Left anchor index and symbol
            j, sym_j = anchors[k + 1]   # Right anchor index and symbol

            # Length of the segment of '.' characters between the anchors
            segment_len = j - i - 1
            if segment_len <= 0:
                # No dots between this pair pf anchors, move to the next pair
                continue

            # Apply rules based on the symbols of the boundary anchors
            if sym_i == sym_j:
                # Case 1: L...L or R...R
                # All dominoes in the segment fall in the same direction
                fill_char = sym_i
                for idx in range(i + 1, j):
                    res[idx] = fill_char
            elif sym_i == 'R' and sym_j == 'L':
                # Case 2: R...L (Collision)
                # Dominoes fall towards the center
                fall_count = segment_len // 2   # Number falling from each side
                # Fill falling right
                for idx in range(i + 1, i + 1 + fall_count):
                    res[idx] = 'R'
                # Fill falling left
                for idx in range(j - fall_count, j):
                    res[idx] = 'L'
                # If segment_len is odd, the middle domino remains '.'
                # This happens implicitly as it's not overwritten.
            # Case 3: L...R
            # these anchors do not push Dominoes between L and R.
            # They remain '.' (no action needed as res is initialized with '.').
            # elif sym_i == 'L' and sym_j == 'R':
            #     pass # No change needed for dots between L and R

        # Join the modified list back into a string
        return "".join(res)