package othon.org.leetcode.medium;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.Arrays;

/**
 * Link:
 * <p>
 * TODO:
 */

@Slf4j
public class NQueensII {

    public static void main(String[] args) {
        Solution s = new Solution();
        var input = 4;
        log.info("total queeens {}", s.totalNQueens(4));
    }

    static class Solution {
        int count = 0;
        int[] board;
        public int totalNQueens(int n) {
            int row = n;
            board = new int[n];
            Arrays.fill(board, -1);
            placeQueens(0, n);
            return count;
        }
        void placeQueens(int row, int n) {
            if (row == n) {
                count += 1;
                return;
            }
            for (int col=0; col<n; col++) {
                //place the queen
                board[row] = col;
                if (!isUnderAttack(col, row)) {
                    placeQueens(row + 1, n);
                }
                board[row] = -1;
            }
        }

        boolean isUnderAttack(int row, int col) {
            for (int row2 =0 ; row2 <row; row2++) {
                int col2 = board[row2];
                if (col2 == col) {
                    return true;
                }
                int absCol = Math.abs(col-col2);
                int absRow = Math.abs(row - row2);
                if (absCol == absRow) {
                    return true;
                }
            }
            return false;
        }
    }
}
