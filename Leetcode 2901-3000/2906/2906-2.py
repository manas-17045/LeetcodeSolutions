# Leetcode 2906: Construct Product Matrix
# https://leetcode.com/problems/construct-product-matrix/
# Solved on 18th of October, 2025
class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Constructs a product matrix where each element `result[i][j]` is the product of all elements in `grid`
        except `grid[i][j]`, modulo 12345.

        Args:
            grid: A 2D list of integers representing the input matrix.
        Returns:
            A 2D list of integers representing the product matrix modulo 12345.
        """
        MOD = 12345
        primes = [3, 5, 823]  # 12345 = 3 * 5 * 823 (pairwise coprime)

        # Flatten grid values for easier iteration
        vals = [x for row in grid for x in row]
        n = len(vals)

        count_zero = {}
        total_prod = {}
        prod_nonzero = {}
        for p in primes:
            cz = 0
            tp = 1 % p
            pnz = 1 % p
            for a in vals:
                am = a % p
                tp = (tp * am) % p
                if am == 0:
                    cz += 1
                else:
                    pnz = (pnz * am) % p
            count_zero[p] = cz
            total_prod[p] = tp
            prod_nonzero[p] = pnz

        # Precompute CRT helpers
        M = MOD
        Mi = {p: M // p for p in primes}
        inv_Mi = {p: pow(Mi[p], -1, p) for p in primes}  # inverses exist since p is prime

        # For each element compute residues modulo each prime, then CRT-combine
        res_flat = []
        for a in vals:
            residues = {}
            for p in primes:
                am = a % p
                cz = count_zero[p]
                if cz >= 2:
                    r = 0
                elif cz == 1:
                    # If this element is the one ==0 (mod p), result is product of other (non-zero) elements mod p
                    r = prod_nonzero[p] if am == 0 else 0
                else:  # cz == 0
                    # Invert am modulo p (am != 0 here)
                    inv_am = pow(am, -1, p)
                    r = (total_prod[p] * inv_am) % p
                residues[p] = r

            # CRT combine residues -> result modulo 12345
            ans = 0
            for p in primes:
                ans += residues[p] * Mi[p] * inv_Mi[p]
            ans %= M
            res_flat.append(ans)

        # Reconstruct 2D matrix
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        out = []
        idx = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(res_flat[idx])
                idx += 1
            out.append(row)
        return out