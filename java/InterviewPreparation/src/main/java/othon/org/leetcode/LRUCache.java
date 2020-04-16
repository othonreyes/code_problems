package othon.org.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LRUCache {

    public static void main(String[] args) {
        LRUCache2 cache = new LRUCache2(2);
        cache.put(2, 1);
        cache.put(1, 1);
        cache.put(2, 3);
        cache.put(4, 1);
        System.out.println(cache.get(1));
        System.out.println(cache.get(2));
    }

    static class LRUCache2 implements Comparable<LRUCache2> {
        // have a map to check if we have the keys
        // havea  double linked list
        Map<Integer, Node> map;
        DoubleLinkedList list;
        int capacity;


        public LRUCache2(int capacity) {
            map = new HashMap<>();
            list = new DoubleLinkedList();
            this.capacity = capacity;
        }

        public int get(int key) {
            if (map.get(key) == null ) {
                return -1;
            }
            Node exNode = list.evict(map.get(key));
            map.put(key, list.addToHead(key, exNode.val)); // update the node
            return exNode.val;
        }

        public void put(int key, int value) {
            if (map.get(key) == null ) {
                if (list.size == capacity) {
                    // remove the last node
                    Node exNode = list.removeFromTail();
                    map.remove(exNode.key);
                }
            } else {
                Node exNode = list.evict(map.get(key));
                map.remove(exNode.key);
            }
            map.put(key, list.addToHead(key, value));
        }

        @Override
        public int compareTo(LRUCache2 o) {
            return 0;
        }

        // Double Linked list
        // evict
        // add to head

        class DoubleLinkedList {
            Node head;
            Node tail;
            int size;

            DoubleLinkedList () {
                head = new Node(-100, -100);
                tail = new Node(-100, -100);
                head.n = tail;
                tail.p = head;
            }

            Node evict(Node node) {
                size -= 1;
                Node prev = node.p;
                Node next = node.n;
                prev.n = next;
                next.p = prev;
                node.n = null;
                node.p = null;
                return node;
            }

            Node addToHead(int key, int val) {
                size += 1;
                Node node = new Node(key, val);
                Node headNext = head.n;
                head.n = node;
                node.p = head;
                headNext.p = node;
                node.n = headNext;
                return node;
            }

            Node removeFromTail() {
                if (size == 0) {
                    return null;
                }
                return evict(tail.p);
            }
        }

        class Node {
            int val;
            int key;
            Node n;
            Node p;
            Node(int k, int v) {
                val = v;
                key = k;
            }

            Node(int v, Node n, Node p) {
                val = v;
                this.n = n;
                this.p = p;
            }
        }
    }

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
}
