package othon.org.leetcode;

import lombok.extern.slf4j.Slf4j;

import java.util.*;

@Slf4j
public class SerializeAndDeserializeBinaryTree {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);
        Codec c = new Codec();
        log.info("{}", c.serialize(root));
        TreeNode root2 = c.deserialize(c.serialize(root));
        log.info("{}", equals(root, root2));
    }

    private static boolean equals(TreeNode n1, TreeNode n2) {
        if (n1 == null && n2== null)
            return true;
        if (n1 != null && n2 != null && n1.val != n2.val)
            return false;
        if (n1 == null && n2!= null)
            return false;
        if (n1 != null && n2== null)
            return false;
        return true && equals(n1.left, n2.left) && equals(n1.right, n2.right);
    }

    /**
     * Definition for a binary tree node.
     * public class TreeNode {
     *     int val;
     *     TreeNode left;
     *     TreeNode right;
     *     TreeNode(int x) { val = x; }
     * }
     */
    static class Codec {

        static final String NULL = "null";
        // Encodes a tree to a single string.
        public String serialize(TreeNode root) {
            StringBuffer sb = new StringBuffer();
            if (root==null) {
                sb.append("[]");
                return sb.toString();
            }
            int height = height(root, 0);
            sb.append("[");
            Queue<List<TreeNode>> q = new ArrayDeque<>();
            q.offer(Arrays.asList(root));
            while (!q.isEmpty()) {
                List<TreeNode> parents = q.poll();
                List<TreeNode> children = new ArrayList<>(parents.size()*2);
                for (TreeNode p: parents) {
                    if (p == null) {
                        sb.append(NULL);
                    } else {
                        sb.append(String.valueOf(p.val));
                    }
                    sb.append(",");
                    // add the children
                    if (height>1) {
                        children.add(p.left);
                        children.add(p.right);
                    }
                }
                height -=1;
                if (!children.isEmpty())
                    q.offer(children);
            }
            //delete last comma
            sb.deleteCharAt(sb.length()-1);
            sb.append("]");
            return sb.toString();
        }

        private int height(TreeNode root, int height) {
            if (root == null) {
                return height;
            }
            return Math.max(height(root.left, height +1), height(root.right, height +1));
        }

        // Decodes your encoded data to tree.
        // doesn't work for input [5,2,3,null,null,2,4,3,1]
        // 31 / 48 test cases passed. :P
//        public TreeNode deserialize(String data) {
//            if (data == null || data.length()==0 || data.equals("[]"))
//                return null;
//            data = data.substring(1,data.length()-1);
//            String[] splitted = data.split(",");
//            int n = splitted.length;
//            int half = n/2 + 1;
//            // pseudo heap array
//            TreeNode[] nodes = new TreeNode[n];
//
//            for (int i=0; i<half; i++) {
//                if (nodes[i] == null && !splitted[i].equals(NULL)) {
//                    nodes[i] = new TreeNode(Integer.parseInt(splitted[i]));
//                }
//                TreeNode node = nodes[i];
//                int left = i * 2 + 1;
//                int right = i * 2 + 2;
//                if (left < n && !splitted[left].equals(NULL)) {
//                    node.left = new TreeNode(Integer.parseInt(splitted[left]));
//                    nodes[left] = node.left;
//                }
//                if (right < n && !splitted[right].equals(NULL)) {
//                    node.right = new TreeNode(Integer.parseInt(splitted[right]));
//                    nodes[right] = node.right;
//                }
//            }
//            return nodes[0];
//        }

        public TreeNode deserialize(String data) {
            if (data == null || data.length()==0 || data.equals("[]"))
                return null;
            data = data.substring(1,data.length()-1);
            String[] splitted = data.split(",");
            int n = splitted.length;
            Queue<TreeNode> q = new ArrayDeque<>();
            TreeNode root = new TreeNode(Integer.valueOf(splitted[0]));
            q.offer(root);
            int i = 1;
            while (!q.isEmpty()) {
                TreeNode node = q.poll();
                int left = i;
                int right = i + 1;
                if (left<n && !splitted[left].equals(NULL)) {
                    node.left = new TreeNode(Integer.valueOf(splitted[left]));
                    q.offer(node.left);
                }
                if (right<n && !splitted[right].equals(NULL)) {
                    node.right = new TreeNode(Integer.valueOf(splitted[right]));
                    q.offer(node.right);
                }
                i += 2;
                if (i>= n-1){
                    break;
                }
            }
            return root;
        }
    }

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
}
