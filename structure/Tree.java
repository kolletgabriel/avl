package structure;

import java.util.ArrayList;


public class Tree {

    private Node root;
    private Tree leftSubTree;
    private Tree rightSubTree;
    private ArrayList<Node> nodes;
    private ArrayList<Node> leaves;
    private int height;
    private int size;


    public Tree(Node root) {

        this.root = root;
        this.nodes = new ArrayList<Node>();
        this.nodes.add(root);
        this.leaves = new ArrayList<Node>();
        this.leaves.add(root);
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


    public void setNodes(ArrayList<Node> nodes) {

        this.nodes = nodes;
    }


    public void setLeaves(ArrayList<Node> leaves) {

        this.leaves = leaves;
    }


    public int getSize() {

        return this.size;
    }


    public int getHeight() {

        return this.height;
    }


    public void setLeftSubTree() {

        ArrayList<Node> subTreeNodes = new ArrayList<Node>();
        for (Node node : this.nodes) {
            if (node.getValue() < this.root.getValue()) {
                subTreeNodes.add(node);
            }
        }

    }


    private int traceBack(Node node, int count) {

        if (node.getFather() != null) {
            count++;
            return traceBack(node.getFather(), count);
        }
        return count;
    }


    private void checkLeaves() {

        for (Node node : this.nodes) {
            if (!node.isLeaf()) {
                this.leaves.remove(node);
            }
        }
    }


    private void computeHeight() {

        for (Node leaf : this.leaves) {
            int count = 1;
            int pathLength = this.traceBack(leaf, count);
            if (pathLength > this.height) {
                this.height = pathLength;
            }
        }
    }


    private void updateStats(Node newNode) {

        this.nodes.add(newNode);
        this.leaves.add(newNode);
        this.checkLeaves();
        this.computeHeight();
        this.size++;
    }


    private boolean addBiggerNode(Node father, Node newNode) {

        if (father.getRightSon() == null) {
            father.setRightSon(newNode);
            newNode.setFather(father);
            this.updateStats(newNode);

            return true;
        }
        return false;
    }


    private boolean addSmallerNode(Node father, Node newNode) {

        if (father.getLeftSon() == null) {
            father.setLeftSon(newNode);
            newNode.setFather(father);
            this.updateStats(newNode);

            return true;
        }
        return false;
    }


    public boolean insert(Node father, Node newNode) {

        if (father.getValue() != newNode.getValue()) {
            if (newNode.getValue() > father.getValue()) {
                if (this.addBiggerNode(father, newNode)) {
                    return true;
                }
                return insert(father.getRightSon(), newNode);
            }
            else {
                if (this.addSmallerNode(father, newNode)) {
                    return true;
                }
                return insert(father.getLeftSon(), newNode);
            }
        }
        return false;
    }


    public boolean fetch(Node node, int val) {
        
        if (node != null) {
            if (val == node.getValue()) {
                return true;
            }
            else if (val > node.getValue()) {
                return fetch(node.getRightSon(), val);
            }
            return fetch(node.getLeftSon(), val);
        }
        return false;
    }


    public static void main(String[] args) {

        Node[] nodes = {
            new Node(7),
            new Node(2),
            new Node(5),
            new Node(6),
            new Node(8),
            new Node(15),
            new Node(18),
        };

        Tree tree = new Tree(nodes[0]);

        for (Node node : nodes) {
            tree.insert(tree.root, node);
        }


    }
}