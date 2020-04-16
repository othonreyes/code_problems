package othon.org.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ContainVirus {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] input = new int[][] {
            new int[] {0,1,0,0,0,0,0,1},
            new int[] {0,1,0,0,0,0,0,1},
            new int[] {0,0,0,0,0,0,0,1},
            new int[] {0,0,0,0,0,0,0,0}
        };
        int walls = s.containVirus(input);
        System.out.println(walls);
    }

    static class Solution {
        public int containVirus(int[][] grid) {
            boolean noMoreInfections = true;
            int walls = 0;
            List<Cluster> clusters = new ArrayList<>();
            while (noMoreInfections) {
                // find the clusters
                for (int i = 0; i< grid.length; i++) {
                    for (int j = 0; j < grid[0].length; j++) {
                        if (grid[i][j] == 1) {
                            Cluster cluster = new Cluster();
                            cluster.findCluster(grid, i, j);
                            cluster.findInfectableCells(grid);
                            clusters.add(cluster);
                        }
                    }
                }
                // sort the clusters and
                Collections.sort(clusters);
                if (clusters.isEmpty()) {
                    return 0;
                }
                //pick the one with higher chance of infecting
                int last = clusters.size() - 1;
                Cluster mostDangerous = clusters.get(last);
                clusters.remove(last);

                // agreggate the number of walls
                walls += mostDangerous.infectableCells;

                // update chosen cluster as contained
                mostDangerous.contained(grid);
                // infect the rest of the world
                for (Cluster c: clusters) {
                    c.infect(grid);
                }
                // if no more infections then finish
                noMoreInfections = !clusters.isEmpty();
            }
            return walls;
        }

        class Point {
            int x;
            int y;
            Point(int i, int j) {
                x = j;
                y = i;
            }
        }
    /*
    1 = virus
    0 = uninfected
    -1 = identified
    2 = walled
    */

        class Cluster implements Comparable<Cluster> {
            int walls = 0;
            int infectableCells = 0;
            List<Point> cluster = new ArrayList<>();

            @Override
            public int compareTo(Cluster other) {
                if (other == null) {
                    return 1;
                }
                if (this.infectableCells == other.infectableCells) {
                    return 0;
                }
                return this.infectableCells > other.infectableCells ? 1 : -1;
            }

            void findCluster(int[][] grid, int i, int j) {
                if (i < 0 || j< 0 ||  grid.length==i || grid[0].length== j) {
                    return;
                }
                if (grid[i][j] != 1) {
                    return;
                }

                cluster.add(new Point(i, j));
                grid[i][j] = -1;
                findCluster(grid, i + 1, j);
                findCluster(grid, i - 1, j);
                findCluster(grid, i, j + 1);
                findCluster(grid, i, j - 1);
            }

            void findInfectableCells(int[][] grid) {
                for(Point p: cluster) {
                    explore(grid, p.y, p.x + 1);
                    explore(grid, p.y, p.x - 1);
                    explore(grid, p.y + 1, p.x);
                    explore(grid, p.y - 1, p.x);
                }
            }

            void explore(int[][] grid, int i, int j) {
                if (i < 0 || j< 0 ||  grid.length<=i || grid[0].length<= j) {
                    return;
                }
                if (grid[i][j] == 0) {
                    this.infectableCells += 1;
                }
            }

            void contained(int[][] grid) {
                for(Point p: cluster) {
                    grid[p.y][p.x] = 2;
                }
            }

            void infect(int[][] grid) {
                for(Point p: cluster) {
                    grid[p.y][p.x] = 1;
                    infect(grid, p.y, p.x + 1);
                    infect(grid, p.y, p.x - 1);
                    infect(grid, p.y + 1, p.x);
                    infect(grid, p.y - 1, p.x);
                }
            }

            void infect(int[][] grid, int i, int j) {
                if (i < 0 || j< 0 ||  grid.length==i || grid[0].length== j) {
                    return;
                }
                if (grid[i][j] == 0) {
                    grid[i][j] = 1;
                }
            }
        }
    }
}
