package othon.org.interviews.ctci.chapter_4_treesandgraphs;

public class CheckSubtree {
    public static void main(String[] args) {
        TreeNode<Integer> root = new TreeNode(5);
        root.left = new TreeNode(3);
        root.right = new TreeNode(7);

        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(2);

        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(8);

        TreeNode<Integer> subtree = root.right;

        System.out.println(isSubtree(root, subtree));
    }

    private static boolean isSubtree(TreeNode<Integer> root, TreeNode<Integer> subtree) {
         return traverse(root, subtree);
    }

    private static boolean traverse(TreeNode<Integer> root, TreeNode<Integer> subtree) {
        return root != null && ( equals(root, subtree) || traverse(root.left, subtree) || traverse(root.right, subtree));
    }

    private static boolean equals(TreeNode<Integer> root, TreeNode<Integer> subtree) {
        if (root == null && subtree == null) {
            return true;
        }
        if (root == null || subtree == null) {
            return false;
        }
        return root.value == subtree.value && equals(root.left, subtree.left) && equals(root.right, subtree.right);
    }
}
