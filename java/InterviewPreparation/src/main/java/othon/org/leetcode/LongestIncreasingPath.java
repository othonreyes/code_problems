package othon.org.leetcode;

import java.util.PriorityQueue;
import java.util.Queue;

public class LongestIncreasingPath {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] input = new int[][] {
                new int[] {3,4,5},
                new int[] {3,2,6},
                new int[] {2,2,1}
        };
        int walls = s.longestIncreasingPath(input);
        System.out.println(walls);
    }

    static class Solution {
        public int longestIncreasingPath(int[][] matrix) {
            int r = matrix.length;
            int c = matrix[0].length;
            int[][] mem = new int[r][c];
            int maxPath = 0;
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    mem[i][j] = explore(matrix, i, j, r, c, mem);
                    maxPath = Math.max(maxPath, mem[i][j]);
                }
            }
            return maxPath;
        }

        int explore(int[][] matrix, int i, int j, int r, int c, int[][] mem) {
            Queue<Integer> q =  new PriorityQueue<>( (o1, o2)->o2-o1 );
            int path = 0;
            int val = 0;
            q.offer(matrix[i][j]);
            while (!q.isEmpty()) {
                path += 1;
                val = q.poll();
                // north
                if ( i - 1 >=0 && matrix[i-1][j] > val) {
                    if (mem[i-1][j] > 0) {
                        path += mem[i-1][j];
                        continue;
                    }
                    q.offer(matrix[i-1][j]);
                }
                // south
                if ( i + 1 < r && matrix[i+1][j] > val) {
                    if (mem[i+1][j] > 0) {
                        path += mem[i+1][j];
                        continue;
                    }
                    q.offer(matrix[i+1][j]);
                }
                // east
                if ( j - 1 >=0 && matrix[i][j- 1] > val) {
                    if (mem[i][j-1] > 0) {
                        path += mem[i][j-1];
                        continue;
                    }
                    q.offer(matrix[i][j - 1]);
                }
                // west
                if ( j + 1 < c && matrix[i][j + 1] > val) {
                    if (mem[i][j+1] > 0) {
                        path += mem[i][j+1];
                        continue;
                    }
                    q.offer(matrix[i][j + 1]);
                }
            }
            return path;
        }
    }
}
