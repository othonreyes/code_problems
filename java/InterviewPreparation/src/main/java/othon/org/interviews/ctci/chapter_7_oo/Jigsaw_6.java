package othon.org.interviews.ctci.chapter_7_oo;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

public class Jigsaw_6 {
    public static void main(String[] args) {

    }

    class Jigsaw {
        Piece[] pieces;

        Piece solve() {
            Map<Edge, List<Piece>> map = new HashMap<>();
            for (Piece p: pieces) {
                if (p.down != null) {
                    map.computeIfAbsent(p.down, e -> new ArrayList<>()).add(p);
                }
                // do the smae for other edgess
            }
            Piece p = map.get(map.values().iterator().next()).get(0);
            while (!map.isEmpty()) {
                //for each edge of the piece
                // get the edge
                // join the edges by  link the pieces
                //remove the edge
            }
            return p;
        }
    }
    class Piece {
        Edge up;
        Edge down;
        Edge left;
        Edge right;
    }

    class Edge {
        Piece prev;
        Piece next;
    }
}
