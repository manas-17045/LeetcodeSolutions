# Leetcode 3348: Smallest Divisible Digit Product II
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/
# Solved on 26th of November, 2025
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        """
        Finds the smallest number (as a string) that is greater than or equal to `num`
        and whose digit product is divisible by `t`.
        :param num: The input number as a string.
        :param t: The divisor.
        :return: The smallest number as a string, or "-1" if no such number exists.
        """
        tempT = t
        tCounts = [0] * 10
        for i in [2, 3, 5, 7]:
            while tempT % i == 0:
                tCounts[i] += 1
                tempT //= i

        if tempT > 1:
            return "-1"

        n = len(num)
        firstZero = -1
        for i in range(n):
            if num[i] == '0':
                firstZero = i
                break

        pCounts = [0] * 10
        if firstZero == -1:
            ok = True
            for c in num:
                d = int(c)
                for k in [2, 3, 5, 7]:
                    while d > 0 and d % k == 0:
                        pCounts[k] += 1
                        d //= k

            for k in [2, 3, 5, 7]:
                if pCounts[k] < tCounts[k]:
                    ok = False

            if ok:
                return num

        pCounts = [0] * 10
        limit = n - 1 if firstZero == -1 else firstZero

        # Calculate initial prefix counts up to limit
        for i in range(limit):
            d = int(num[i])
            for k in [2, 3, 5, 7]:
                while d > 0 and d % k == 0:
                    pCounts[k] += 1
                    d //= k

        for i in range(limit, -1, -1):
            startDigit = int(num[i]) + 1
            for d in range(startDigit, 10):
                currentCounts = list(pCounts)
                tempD = d
                for k in [2, 3, 5, 7]:
                    while tempD > 0 and tempD % k == 0:
                        currentCounts[k] += 1
                        tempD //= k

                remLen = n - 1 - i
                suffix = self.getSuffix(remLen, tCounts, currentCounts)
                if suffix is not None:
                    return num[:i] + str(d) + suffix

            if i > 0:
                prevD = int(num[i - 1])
                for k in [2, 3, 5, 7]:
                    while prevD > 0 and prevD % k == 0:
                        pCounts[k] -= 1
                        prevD //= k

        length = n + 1
        while True:
            suffix = self.getSuffix(length, tCounts, [0] * 10)
            if suffix is not None:
                return suffix
            length += 1

    def getSuffix(self, length, tCounts, currentCounts):
        needed = [0] * 10
        for k in [2, 3, 5, 7]:
            needed[k] = max(0, tCounts[k] - currentCounts[k])

        sb = []
        while needed[7] > 0:
            sb.append('7')
            needed[7] -= 1
        while needed[5] > 0:
            sb.append('5')
            needed[5] -= 1
        while needed[3] >= 2:
            sb.append('9')
            needed[3] -= 2
        while needed[2] >= 3:
            sb.append('8')
            needed[2] -= 3
        while needed[3] >= 1 and needed[2] >= 1:
            sb.append('6')
            needed[3] -= 1
            needed[2] -= 1
        while needed[2] >= 2:
            sb.append('4')
            needed[2] -= 2
        while needed[3] > 0:
            sb.append('3')
            needed[3] -= 1
        while needed[2] > 0:
            sb.append('2')
            needed[2] -= 1

        if len(sb) > length:
            return None

        sb.sort()

        res = []
        for k in range(length - len(sb)):
            res.append('1')
        res.extend(sb)

        return "".join(res)