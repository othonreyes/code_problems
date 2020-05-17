package othon.org.interviews.ctci.chapter_10_sorting;

import lombok.extern.slf4j.Slf4j;
import lombok.val;
import sun.reflect.generics.tree.Tree;

import java.util.Arrays;

@Slf4j
public class RankNumber_10 {
    public static void main(String[] args) {
        int [] arr = new int[]{1,5,8,3,4,6};
        Ranker ranker = new Ranker();
        Arrays.stream(arr).forEach( i -> ranker.track(i));
        log.info("1 - {} == 0", ranker.getRankOf(1));
        log.info("5 - {} == 3", ranker.getRankOf(5));
    }

    /**
     * Use a BST
     */
    static class Ranker {
        RankNode root;
        void track(int x) {
            if (root == null) {
                root = new RankNode(x);
            } else {
                root.insert(x);
            }
        }

        int getRankOf(int x) {
            return root.search(x);
        }
    }

    static class RankNode {
        int val;
        RankNode left;
        RankNode right;
        int leftSize;
        RankNode(int n) {
            val = n;
        }

        void insert(int n) {
            if (n <= val) {
                if (left == null)
                    left = new RankNode(n);
                else
                    left.insert(n);
                leftSize += 1;
            } else {
                if (right == null)
                    right = new RankNode(n);
                else
                    right.insert(n);
            }
        }

        int search(int n) {
            if (n == val) {
                return leftSize;
            }
            if (n < val) {
                return left == null? -1: left.search(n);
            } else {
                int rightRank = right == null? -1: right.search(n);
                if (rightRank == -1) return -1;
                return leftSize + 1  + rightRank;
            }
        }
    }
}
