package othon.org.interviews.ctci.chapter_4_treesandgraphs;

public class GraphNode {

    public int value;

    public GraphNode[] adjacent;

    public GraphNode(int value, int neighbors) {
        this.value = value;
        this.adjacent = new GraphNode[neighbors];
    }

}
