package othon.org.interviews.ctci.chapter_4_treesandgraphs;

public class TreeNode<T> {
    T value;
    TreeNode<T> left;
    TreeNode<T> right;

    TreeNode(T v) {
        this.value = v;
    }
}
