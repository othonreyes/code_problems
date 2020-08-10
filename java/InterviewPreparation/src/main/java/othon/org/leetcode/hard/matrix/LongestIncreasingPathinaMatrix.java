package othon.org.leetcode.hard.matrix;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.Arrays;

/**
 * Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/solution/
 * <p>
 /*
 Given a 2D int array, find the length of the longest decreasing path. You can move left, right, up and down.

 [9,8,7],
 [1,1,6],
 [1,1,5],

 Longest decreasing path is 9->8->7->6->5->1, with length 6

 [1,1,1],
 [1,9,1],
 [1,5,9],

 */

@Slf4j
public class LongestIncreasingPathinaMatrix {
    public static void main(String[] args) {
        int[][] matrix = new int[][]{
                {9,8,7},
                {1,1,6},
                {1,1,5}};
        Solution s = new Solution();

        int len = s.longestDecreasingPath(matrix);
        System.out.println(len);
    }

    static class Solution {
        int counter = Integer.MIN_VALUE;

        public int longestDecreasingPath(int[][] matrix) {
            int[][] dp = new int[matrix.length][matrix[0].length];
            for (int[] dpRow: dp) {
                Arrays.fill(dpRow, -1);
            }
            for (int i = 0; i< matrix.length; i++) {
                for (int j = 0; j< matrix[0].length; j++) {
                    traverse(matrix, dp, i, j, 1);
                }
            }

            int longest = Integer.MIN_VALUE;
            for (int[] dpRow: dp) {
                longest = Math.max(longest, Arrays.stream(dpRow).max().getAsInt());
            }
            return longest;
        }

        static int[][] dirs = {{1,0}, {-1,0}, {0,-1}, {0, 1}};

        static int traverse(int[][] matrix, int[][] dp, int y, int x, final int acc) {
            if (dp[y][x] > -1) {
                return dp[y][x];
            }
            int cell = matrix[y][x];
            log.info("Checking cell [{},{}] = {} and acc {}", y, x, cell, acc);
            int counter = acc;
            for (int i= 0 ; i< dirs.length; i++) {
                int newY = y + dirs[i][0];
                int newX = x + dirs[i][1];
                if (newY >=0 && newX >=0 && newY <matrix.length && newX <matrix[0].length
                        //&& cell < matrix[newY][newX]) { // the < is inverted
                        && cell > matrix[newY][newX]) {
                    log.info("Exploring new coordinates [{},{}]", newY, newX);
                    counter = Math.max(counter, traverse(matrix, dp, newY, newX, acc + 1));
                }
            }
            dp[y][x] = counter;
            log.info("Result [{},{}] = {}", y, x, counter);
            return dp[y][x];
        }
    }
}
