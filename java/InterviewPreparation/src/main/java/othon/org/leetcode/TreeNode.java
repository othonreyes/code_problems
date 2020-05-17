package othon.org.leetcode;

import lombok.Data;

@Data
public class TreeNode {
    int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}
