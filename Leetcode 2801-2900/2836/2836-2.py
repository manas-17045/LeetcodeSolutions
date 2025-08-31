# Leetcode 2836: Maximize Value of Function in a Ball Passing Game
# https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/
# Solved on 31st of August, 2025
class Solution:
    def getMaxFunctionValue(self, receiver: list[int], k: int) -> int:
        """
        Calculates the maximum function value achievable by starting at any player and performing k steps.
        :param receiver: A list where receiver[i] is the player that player i passes the ball to.
        :param k: The number of steps to perform.
        :return: The maximum possible sum of player indices encountered over k steps, including the starting player.
        """
        n = len(receiver)
        LOG = k.bit_length()  # maximum power of 2 needed

        next_player = [[0] * n for _ in range(LOG)]
        sum_score = [[0] * n for _ in range(LOG)]

        # Base case: 2^0 = 1 pass
        for i in range(n):
            next_player[0][i] = receiver[i]
            sum_score[0][i] = receiver[i]

        # Build binary lifting tables
        for j in range(1, LOG):
            for i in range(n):
                nxt = next_player[j - 1][i]
                next_player[j][i] = next_player[j - 1][nxt]
                sum_score[j][i] = sum_score[j - 1][i] + sum_score[j - 1][nxt]

        # Try each starting player
        ans = 0
        for start in range(n):
            cur = start
            score = start  # include starting index
            steps = k
            bit = 0
            while steps > 0:
                if steps & 1:
                    score += sum_score[bit][cur]
                    cur = next_player[bit][cur]
                steps >>= 1
                bit += 1
            ans = max(ans, score)

        return ans