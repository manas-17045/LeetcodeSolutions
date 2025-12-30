// Leetcode 3552: Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/
// Solved on 30th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of moves to traverse a grid from (0,0) to (m-1, n-1).
     * The grid can contain 'A'-'Z' for teleportation portals, '#' for obstacles, and '.' for empty cells.
     * @param matrix The input grid as an array of strings.
     * @return The minimum number of moves, or -1 if the destination is unreachable.
     */
    public int minMoves(String[] matrix) {
        int m = matrix.length;
        int n = matrix[0].length();
        char[][] grid = new char[m][n];
        List<Integer>[] portals = new ArrayList[26];
        for (int i = 0; i < 26; i++) {
            portals[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            grid[i] = matrix[i].toCharArray();
            for (int j = 0; j < n; j++) {
                char c = grid[i][j];
                if (c >= 'A' && c <= 'Z') {
                    portals[c - 'A'].add(i * n + j);
                }
            }
        }

        int[][] distance = new int[m][n];
        for (int[] row : distance) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        Deque<int[]> deque = new ArrayDeque<>();
        deque.addFirst(new int[]{0, 0});
        distance[0][0] = 0;

        boolean[] visitedPortals = new boolean[26];
        int[] directions = {0, 1, 0, -1, 0};

        while (!deque.isEmpty()) {
            int[] current = deque.pollFirst();
            int r = current[0];
            int c = current[1];
            int d = distance[r][c];

            if (r == m - 1 && c == n - 1) {
                return d;
            }

            char cell = grid[r][c];
            if (cell >= 'A' && cell <= 'Z') {
                int portalIndex = cell - 'A';
                if (!visitedPortals[portalIndex]) {
                    visitedPortals[portalIndex] = true;
                    for (int flat : portals[portalIndex]) {
                        int nr = flat / n;
                        int nc = flat % n;
                        if (d < distance[nr][nc]) {
                            distance[nr][nc] = d;
                            deque.addFirst(new int[]{nr, nc});
                        }
                    }
                }
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + directions[i];
                int nc = c + directions[i + 1];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != '#') {
                    if (d + 1 < distance[nr][nc]) {
                        distance[nr][nc] = d + 1;
                        deque.addLast(new int[]{nr, nc});
                    }
                }
            }
        }

        return -1;
    }
}