// Leetcode 3923: Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/
// Solved on 23rd of May, 2026
class Solution {
    /**
     * Calculates the minimum number of generations required to reach a target point.
     * In each generation, new points are created by taking the midpoint of any two existing points.
     *
     * @param points Initial set of 3D points where each coordinate is in the range [0, 6].
     * @param target The target 3D point to reach.
     * @return The minimum number of generations to reach the target, or -1 if unreachable.
     */
    public int minGenerations(int[][] points, int[] target) {
        boolean[] seen = new boolean[343];
        int[] allPoints = new int[343];
        int allSize = 0;
        int[] currentGen = new int[343];
        int currentSize = 0;
        int targetVal = target[0] * 49 + target[1] * 7 + target[2];

        for (int[] p : points) {
            int val = p[0] * 49 + p[1] * 7 + p[2];
            if (!seen[val]) {
                seen[val] = true;
                allPoints[allSize++] = val;
                currentGen[currentSize++] = val;
            }
        }

        if (seen[targetVal]) {
            return 0;
        }

        int generationCount = 1;

        while (true) {
            int[] nextGen = new int[343];
            int nextSize = 0;

            for (int i = 0; i < currentSize; i++) {
                int p1 = currentGen[i];
                int x1 = p1 / 49;
                int y1 = (p1 / 7) % 7;
                int z1 = p1 % 7;

                for (int j = 0; j < allSize; j++) {
                    int p2 = allPoints[j];
                    if (p1 == p2) {
                        continue;
                    }

                    int x2 = p2 / 49;
                    int y2 = (p2 / 7) % 7;
                    int z2 = p2 % 7;

                    int midX = (x1 + x2) / 2;
                    int midY = (y1 + y2) / 2;
                    int midZ = (z1 + z2) / 2;

                    int midVal = midX * 49 + midY * 7 + midZ;

                    if (midVal == targetVal) {
                        return generationCount;
                    }

                    if (!seen[midVal]) {
                        seen[midVal] = true;
                        nextGen[nextSize++] = midVal;
                    }
                }
            }

            if (nextSize == 0) {
                return -1;
            }

            for (int i = 0; i < nextSize; i++) {
                allPoints[allSize++] = nextGen[i];
                currentGen[i] = nextGen[i];
            }
            
            currentSize = nextSize;
            generationCount++;
        }
    }
}