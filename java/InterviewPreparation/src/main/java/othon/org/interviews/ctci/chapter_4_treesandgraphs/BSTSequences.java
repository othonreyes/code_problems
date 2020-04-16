package othon.org.interviews.ctci.chapter_4_treesandgraphs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class BSTSequences {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(2);
        root.left = new TreeNode(1);
        root.right = new TreeNode(3);
        List<LinkedList> results = allSequence(root);
        for (LinkedList list : results) {
            System.out.println(list.stream()
                    .map(i -> String.valueOf(i))
                    .collect(Collectors.joining())
            );
        }

        root = new TreeNode(5);
        root.left = new TreeNode(3);
        root.right = new TreeNode(7);

        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(2);

        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(8);
        results = allSequence(root);
        for (LinkedList list : results) {
            System.out.println(list.stream().collect(Collectors.joining()));
        }
    }

    static <T> List<LinkedList<T>> allSequence(TreeNode<T> node) {
        List<LinkedList<T>> results = new ArrayList<>();
        if (node == null) {
            results.add(new LinkedList());
            return results;
        }

        LinkedList<T> prefix = new LinkedList<>();
        prefix.addFirst(node.value);

        // get sequences from left
        List<LinkedList<T>> leftSequence = allSequence(node.left);

        // get sequences from right
        List<LinkedList<T>> rightSequence = allSequence(node.right);

        //weave them
        for (LinkedList<T> left : leftSequence) {
            for (LinkedList<T> right : rightSequence) {
                weaveNodes(left, right, results, prefix);
            }
        }

        return results;
    }

    //techinique to combine lists -> doesn't produce all possible combinations but produce the combination of all elements
    private static <T> void weaveNodes(LinkedList<T> left, LinkedList<T> right, List<LinkedList<T>> results, LinkedList<T> prefix) {
        if (left.size() == 0 || right.size() == 0) {
            LinkedList<T> result = (LinkedList<T>) prefix.clone();
            result.addAll(left);
            result.addAll(right);
            results.add(result);
            return;
        }

        T headFrist = left.removeFirst();
        prefix.addLast(headFrist); // why?
        weaveNodes(left, right, results, prefix);
        prefix.removeLast();
        left.addFirst(headFrist);

        T headSecond = right.removeFirst();
        prefix.addLast(headSecond); // why?
        weaveNodes(left, right, results, prefix);
        prefix.removeLast();
        right.addFirst(headSecond);
    }
}
