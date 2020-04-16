package othon.org.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// https://leetcode.com/problems/binary-tree-right-side-view
public class BinaryTreeRightSideView {
    public static void main(String[] args) {
        Solution s = new Solution();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.right = new TreeNode(5);
        root.right = new TreeNode(3);
        root.right.right = new TreeNode(4);
        s.rightSideView(root);
    }

    static class Solution {
        public List<Integer> rightSideView(TreeNode root) {
            if (root == null) {
                return Collections.emptyList();
            }
            List<Integer> results = new ArrayList<>();
            Queue<List<TreeNode>> q = new LinkedList<>();
            q.offer(Arrays.asList(root));
            while (!q.isEmpty()) {
                List<TreeNode> ln = q.poll();
                results.add(ln.get(ln.size()-1).val);
                List<TreeNode> lc = new ArrayList<>();
                for (TreeNode n : ln) {
                    if (n.left != null) {
                        lc.add(n.left);
                    }
                    if (n.right != null) {
                        lc.add(n.right);
                    }
                }
                if (ln.isEmpty()) {
                    break;
                } else {
                    q.offer(lc);
                }
            }
            return results;
        }
    }
    static class TreeNode {
       int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
  }
}

