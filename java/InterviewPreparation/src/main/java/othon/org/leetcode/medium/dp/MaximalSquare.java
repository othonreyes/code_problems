package othon.org.leetcode.medium.dp;

import lombok.extern.slf4j.Slf4j;
import lombok.var;
import othon.org.leetcode.utils.Deserializer;

/**
 * Link:https://leetcode.com/problems/maximal-square/
 * <p>
 * Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
 *
 * Example:
 *
 * Input:
 *
 * 1 0 1 0 0
 * 1 0 1 1 1
 * 1 1 1 1 1
 * 1 0 0 1 0
 *
 * Output: 4
 */

@Slf4j
public class MaximalSquare {
    public static void main(String[] args) {
        Solution s = new Solution();
        var input = Deserializer.toIntMatrix("[[\"0\",\"0\",\"0\",\"1\"],[\"1\",\"1\",\"0\",\"1\"],[\"1\",\"1\",\"1\",\"1\"],[\"0\",\"1\",\"1\",\"1\"],[\"0\",\"1\",\"1\",\"1\"]]");
        log.info("Result {}", s.maximalSquare(input));
    }

    static class Solution {
        public int maximalSquare(int[][] matrix) {
            int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
            // at the begining of the iteration of the cols, dp contains the value of the previous rows.
            // then prev contains the value of the previous row and column
            int[] dp = new int[cols + 1];
            int maxsqlen = 0, prev = 0;
            for (int i = 1; i <= rows; i++) {
                for (int j = 1; j <= cols; j++) {
                    int temp = dp[j];
                    if (matrix[i - 1][j - 1] == 1) {
                        dp[j] = Math.min(Math.min(dp[j - 1], prev), dp[j]) + 1;
                        maxsqlen = Math.max(maxsqlen, dp[j]);
                    } else {
                        dp[j] = 0;
                    }
                    prev = temp;
                }
            }
            return maxsqlen * maxsqlen;
        }
    }
}
