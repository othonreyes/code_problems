package othon.org.interviews.ctci.chapter_8_dp;

import java.time.Instant;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class FileSystem {

    class Node implements Comparable<Node> {
        String name;
        boolean access;
        Instant creationDate;

        public int compareTo(Node other) {
            if (other == null) return 1;
            return name.compareTo(other.name);
        }

        @Override
        public boolean equals(Object n) {
            if (n == null) return false;
            if (!(n instanceof Node)) return false;
            if (n == this) return true;
            return name.equals(((Node)n).name);
        }
    }

    class Folder extends Node {
        Map<String, Node> children = new TreeMap<>();

        Node get(String name) {
            // searches for the file in the current folder
            return null;
        }

        void add (Node n) {
            children.put(n.name,n);
        }

        Node delete(String n) {
            return children.remove(n);
        }
    }

    class File extends Node {
        int size;
        Instant modifiedDate;
    }
}
