package othon.org.interviews.ctci.chapter_4_treesandgraphs;

public class FirstCommonAncestor {
    public static void main(String[] args) {
        TreeNode root = new TreeNode("A");
        root.left = new TreeNode("B");
        root.left.left = new TreeNode("D");
        root.left.right = new TreeNode("E");
        root.left.right.left = new TreeNode("G");

        root.right = new TreeNode("C");
        root.right.right = new TreeNode("F");

        System.out.println(firstAncestor(root, "D", "E"));
        System.out.println(firstAncestor(root, "D", "F"));
        System.out.println(firstAncestor(root, "G", "D"));
        System.out.println(firstAncestor(root, "C", "F"));
        System.out.println(firstAncestor(root, "C", "H"));
    }

    static <T> T firstAncestor(TreeNode<T> node, T v1, T v2) {
        if (node == null) {
            return null;
        }
        Result result = findAncestor(node, v1, v2);
        if (!result.ancestor) {
            return null;
        }
        return (T) result.node.value;
    }

    static <T> Result<T> findAncestor(TreeNode<T> node, T v1, T v2) {
        if (node == null) {
            return null;
        }
        Result leftResult = findAncestor(node.left, v1, v2);
        if (leftResult != null && leftResult.ancestor) {
            return leftResult;
        }
        Result rightResult = findAncestor(node.right, v1, v2);
        if (rightResult != null && rightResult.ancestor) {
            return rightResult;
        }
        if (leftResult != null && rightResult != null) {
            // i'm the ancestor
            return new Result(node, true);
        }
        boolean selfHasValue = hasValue(node, v1, v2);
//        if ((leftResult != null || rightResult != null) && selfHasValue) {
//            // i'm the ancestor
//            return new Result(node, true);
//        }
//        if (selfHasValue) {
//            return new Result(node, false);
//        } else {
//            return leftResult != null ? leftResult : rightResult;
//        }

        if (selfHasValue) {
            // i'm the ancestor
            return new Result(node, (leftResult != null || rightResult != null));
        }
        return leftResult != null ? leftResult : rightResult;
    }

    static <T> boolean hasValue(TreeNode<T> node, T v1, T v2) {
        if (node == null) {
            return false;
        }
        return node.value.equals(v1) || node.value.equals(v2);
    }

    static class Result<T> {
        TreeNode<T> node;
        boolean ancestor;

        Result(TreeNode<T> n, boolean a) {
            node = n;
            ancestor = a;
        }
    }
}


