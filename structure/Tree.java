package structure;

import java.util.ArrayList;


public class Tree {

    private ArrayList<Node> nodes;
    private Node root;
    private int height;
    private int size;


    public Tree(Node root) {

        this.root = root;
        this.nodes = new ArrayList<Node>();
        this.nodes.add(root);
        this.height = 1;
        this.size = 1;
    }


    public Node getRoot() {

        return this.root;
    }


    public void setRoot(Node root) {

        this.root = root;
    }


    public ArrayList<Node> getNodes() {

        return this.nodes;
    }


    public int getSize() {

        return this.size;
    }


    public int getHeight() {

        return this.height;
    }


    private boolean addBiggerNode(Node father, Node newNode) {

        if (father.getRightSon() == null) {
            father.setRightSon(newNode);
            newNode.setFather(father);
            this.nodes.add(newNode);
            this.size++;
            if (father.getLeftSon() == null) {
                this.height++;
            } return true;
        } return false;
    }


    private boolean addLesserNode(Node father, Node newNode) {

        if (father.getLeftSon() == null) {
            father.setLeftSon(newNode);
            newNode.setFather(father);
            this.nodes.add(newNode);
            this.size++;
            if (father.getRightSon() == null) {
                this.height++;
            } return true;
        } return false;
    }


    public boolean insert(Node father, Node newNode) {

        if (father.getValue() != newNode.getValue()) {
            if (newNode.getValue() > father.getValue()) {
                if (this.addBiggerNode(father, newNode)) {
                    return true;
                } return insert(father.getRightSon(), newNode);
            }
            else {
                if (this.addLesserNode(father, newNode)) {
                    return true;
                } return insert(father.getLeftSon(), newNode);
            }
        } return false;
    }


    public boolean fetch(Node node, int val) {
        
        if (node != null) {
            if (val == node.getValue()) {
                return true;
            }
            else if (val > node.getValue()) {
                return fetch(node.getRightSon(), val);
            } return fetch(node.getLeftSon(), val);
        } return false;
    }


    public static void main(String[] args) {

        Node[] nodes = {
            new Node(2),
            new Node(5),
            new Node(6),
            new Node(7),
            new Node(8),
            new Node(15),
            new Node(18),
        };

        Tree tree = new Tree(nodes[3]);

        for (Node node : nodes) {
            tree.insert(tree.root, node);
        }

        System.out.println(tree.height);
    }
}