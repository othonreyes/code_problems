package othon.org.leetcode;

import java.util.ArrayDeque;
import java.util.Queue;

public class Walls_Gates {

    public static void main(String[] args) {

    }

    static class Solution {
        public void wallsAndGates(int[][] rooms) {
            Queue<Point> q = new ArrayDeque<>();
            for (int i = 0; i< rooms.length; i++) {
                for (int j = 0; j < rooms[i].length; j++) {
                    if(rooms[i][j] == 0) {
                        q.add(new Point(i, j));
                    }
                }
            }

            // Iterate while queue is not empty
            while (!q.isEmpty()) {
                int size = q.size();
                // iterate over the size of the queu
                for (int i = 0; i < size; i++ ) {
                    //pop put the queue element
                    Point p = q.remove();
                    int val = rooms[p.x][p.y] == 0 ? 1: rooms[p.x][p.y] + 1;
                    // EAST
                    updateRoomDistance(rooms, p.x + 1, p.y, val);
                    // NORTH
                    updateRoomDistance(rooms, p.x, p.y - 1, val);
                    // WEAST
                    updateRoomDistance(rooms, p.x - 1, p.y, val);
                    // SOUTH
                    updateRoomDistance(rooms, p.x, p.y + 1, val);
                }
            }
        }

        void updateRoomDistance(int[][]rooms, int x, int y, int val) {
            if (x<0 || x >= rooms[0].length || y < 0 || y >= rooms.length ) {
                return;
            }
            int r = rooms[y][x];
            // r miwght be a 0 or -1 or an updated value so we don't update it
            if (r < Integer.MAX_VALUE) {
                return;
            }
            rooms[y][x] = val;
        }

        class Point {
            int x;
            int y;

            Point(int i, int j) {
                y = i;
                x = j;
            }
        }
    }
}
