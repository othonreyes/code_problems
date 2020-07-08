import java.util.Map;
import java.util.Queue;

// Question:
// Given a colored binary tree, find the largest single-color embedded tree. 
//
//              B
//             / \
//            B   R
//           / \   \
//          G   4G*  R
//             / \   \
//            2G  1G   R
//           /          \
//          G1           B
//         /
//        Y1
//
//                R3
//               / \
//              1R  R1
//             /
//            1B


z

TreeNode largestSingleColorEmbeddedTree(TreeNode root) {
    if (root == null) {
        return null;
    }
    Map<Integer, Item> map = new HashMap<>();
    dfs(root, map);
    
    TreeNode maxNode = null;
    int max = Integer.MIN_VALUE;
    for (Item item: map.values()) {
        if (item.consecutive>max) {
            maxNode = item.node;
            max = item.consecutive;
        }
    }
    return maxNode;
}

Accumulator dfs (TreeNode node, Map<Integer, Item> map) {
    if (node == null) {
        return null;
    }
    Accumulator leftAcc = dfs(node.left, map);
    int nodeColorAcc = 1;
    if (leftAcc != null) {
        if (leftAcc.color == node.color) {
            nodeColorAcc += leftAcc.consecutive;
        } else {
            updateMap(leftAcc, node.left, map);
        }
    }
    Accumulator rightAcc = dfs(node.right, map);
    if (rightAcc != null) {
        if (rightAcc.color == node.color) {
            nodeColorAcc += rightAcc.consecutive;
        } else {
            updateMap(rightAcc, node.right, map);
        }
    }    
    Accumulator acc = new Accumulator(node.color, nodeColorAcc);
    updateMap(acc, node, map);
    return acc;
}

void updateMap(Accumulator acc, TreeNode node, Map<Integer, Item> map) {
    if (acc == null || node == null) {
        return;
    }
    if (!map.containsKey(acc.color)) {
        map.put(acc.color, new Item(node, acc.consecutive));
    } else {
        Item currentMax = map.get(acc.color);
        if (currentMax.consecutive<acc.consecutive) {
            map.put(acc.color, new Item(node, acc.consecutive));
        }
    }
}

class Item {
    TreeNode node;
    int consecutive;
}

class Accumulator {
    int color;
    int consecutive;
}
