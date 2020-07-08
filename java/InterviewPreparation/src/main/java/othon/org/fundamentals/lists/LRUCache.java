package othon.org.fundamentals.lists;

import java.util.HashMap;
import java.util.Map;

public class LRUCache {

    public static void main(String[] args) {
        Cache cache = new Cache(5);

        /**
         set(1,1) -> 1-1
         set(2,2) ->  22 11
         set(3,3) -> 33 22 11
         set (1,9) -> 19 33 22
         set (4,4) -> 44 19 33 22
         get (3) -> 3 -> 33 44 19 22
         set(5,5) -> 55 33 44 19 22
         set(6,6) -> 66 55 33 44 19
         get(2) -> -1 -> 66 55 33 44 19
         get(1) -> 9 -> 19 66 55 33 44
         */
        cache.set(1,1);
        System.out.println(cache.get(1));
        System.out.println(cache.toString());

        cache.set(2,2);
        cache.set(3,3);
        System.out.println(cache.toString());
        System.out.println(cache.get(2));
        System.out.println(cache.toString());
        System.out.println(cache.get(3));
        System.out.println(cache.toString());
        cache.set(1,9);
        cache.set(4,4);
        System.out.println(cache.get(3));
    }
}


/*

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

[H] -> 1 -> [T]

*/

class Node {
    int value;
    Node(int value) {
        this.value = value;
    }

    Node prev;
    Node next;

    @Override
    public String toString() {
        return "{" + (prev == null? null:"X") + "|" + value + "|" + (next == null? null:"X") + "}";
    }
}

class LinkedList {
    Node head;
    Node tail;
    int size;

    LinkedList() {
        head = new Node(Integer.MIN_VALUE);
        tail = new Node(Integer.MAX_VALUE);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }

    Node addNodeToHead(int value) { // 1
        Node newNode = new Node(value);
        Node nextNode = head.next; // 1

        head.next = newNode; // H<->2
        newNode.prev = head; //

        newNode.next = nextNode; //H->2->1-T
        nextNode.prev = newNode; // 2
        size += 1;
        return newNode;
    }

    Node removeFromTail() {
        if (size == 0) {
            return null;
        }
        Node prevTail = tail.prev;
        Node previous = prevTail.prev;
        previous.next = tail;
        tail.prev = previous;
        size -= 1;
        return prevTail;
    }
    //  [H] -> 1 -> [T]
  /*
  H->33->22->11->T
  */
    Node remove(Node node) {
        if (node == null) {
            return null;
        }
        Node prev = node.prev;
        Node next = node.next;

        prev.next = next; // bug
        next.prev = prev;

        node.prev = null;
        node.next = null;
        size -= 1;
        return node;
    }

    public int getSize() {
        return size;
    }

    @Override
    public String toString() {
        Node n = head;
        StringBuffer sb = new StringBuffer();
        while (n!=null) {
            sb.append(n.toString());
            sb.append("-");
            n = n.next;
        }
        return sb.toString();

    }

}

class Cache {
    int limit;
    Map<Integer, Node> map;
    LinkedList list;

    Cache(int limit) {
        if (limit<=0) {
            throw new IllegalArgumentException(":(");
        }
        this.limit = limit;
        map = new HashMap<>();
        list = new LinkedList();
    }

    int get(int key) {
        if (!map.containsKey(key)) {
            return -1;
        }
        Node node = map.get(key);
        list.remove(node);
        map.put(key, list.addNodeToHead(node.value)); // this step is needed to refresh the map
        return node.value;
    }

    void set(int key, int value) {     // k=2
        // if we reached the limit then remove it from the list
        if (limit == list.getSize()) {
            Node n = list.removeFromTail(); // we need the key to remove it from the map
            map.remove(n.value);
        }
        Node node = null;
        if (map.containsKey(key)) {
            list.remove(map.get(key));
        }
        node = list.addNodeToHead(value);
        map.put(key, node);
    }

    @Override
    public String toString() {
        return list.toString();
    }
}