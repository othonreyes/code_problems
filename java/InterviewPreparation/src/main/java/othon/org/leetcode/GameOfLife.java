package leetcode;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class GameOfLife {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] input = {
                {0,1,0},
                {0,0,1},
                {1,1,1},
                {0,0,0}};
        log.info("{}", input);
        s.gameOfLife(input);
        log.info("{}", input);
    }

    static class Solution {
        int[][] directions = {{-1, -1}, {-1, 0}, {-1, 1},
                            {0, -1}, {0, 1},
                            {1, -1}, {1, 0}, {1, 1}
                           };
        public void gameOfLife(int[][] board) {
            int r =board.length; // limit of ys
            int c =board[0].length; //limit of xs

            for(int i=0; i< r; i++){
                for(int j=0; j< c; j++){
                    int neighbors = explore(i,j,r,c, board);
                    if (board[i][j] == 1 && neighbors>3 || neighbors<2) {
                        board[i][j] = -1;
                    } else  if (board[i][j] == 0 && neighbors==3){
                        board[i][j] = 2;
                    }
                }
            }
            for(int i=0; i< r; i++){
                for(int j=0; j< c; j++){
                    if (board[i][j]==-1)
                        board[i][j]= 0;
                    else if (board[i][j]==2)
                        board[i][j]= 1;
                }
            }
        }

        int explore(int y, int x, int r, int c, int[][] board) {
            int n = 0;
            for (int k=0; k<directions.length;k++) {
                int dy = y + directions[k][0];
                int dx = x + directions[k][1];
                if (dy<0 || dx<0 || dy==r || dx == c || board[dy][dx]==0){
                    continue;
                }
                if (board[dy][dx] == 1 || board[dy][dx] == -1) {
                    n+=1;
                }
            }
            return n;
        }
    }
}

