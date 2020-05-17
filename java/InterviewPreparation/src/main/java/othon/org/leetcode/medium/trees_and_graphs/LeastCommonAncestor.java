package othon.org.leetcode.medium.trees_and_graphs;

import lombok.extern.slf4j.Slf4j;
import lombok.var;
import othon.org.leetcode.SerializeAndDeserializeBinaryTree;
import othon.org.leetcode.TreeNode;
import sun.reflect.generics.tree.Tree;

/**
 * Link:
 * <p>
 * TODO:
 */

@Slf4j
public class LeastCommonAncestor {
    public static void main(String[] args) {
        Solution s = new Solution();
        TreeNode root = new TreeNode(1);
        var input = new SerializeAndDeserializeBinaryTree.Codec().deserialize("[3,5,1,6,2,0,8,null,null,7,4]");
        s.lowestCommonAncestor(input, input.left, input.left.right.right);
    }

    static class Solution {
        public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
            Result r = lca(root, p, q);
            return r.found? r.n : null;
        }

        Result lca (TreeNode n, TreeNode p, TreeNode q) {
            if (n == null) {
                return new Result();
            }
            if (n == p && n == q) {
                return new Result(n, true);
            }
            Result leftKiddo = lca(n.left, p,  q);
            if (leftKiddo.found) {
                return leftKiddo;
            }
            Result rightKiddo = lca(n.left, p,  q);
            if (rightKiddo.found) {
                return rightKiddo;
            }
            if (leftKiddo.n != null && rightKiddo.n != null) {
                return new Result(n, true);
            } else if (n == p || n == q) {
                boolean found = leftKiddo.n != null || rightKiddo.n != null;
                return new Result(n, found);
            } else {
                return new Result(leftKiddo.n !=null? leftKiddo.n: rightKiddo.n, false);
            }
        }

        class Result {
            TreeNode n;
            boolean found;
            Result(){}

            Result(TreeNode m) {n = m;}

            Result(TreeNode m, boolean maybe) {
                n = m;
                found = maybe;
            }
        }
    }
}
