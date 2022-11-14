package structure;

import java.util.ArrayList;


public class Avl {

    private ArrayList<Tree> subTrees;


    public Avl(Tree firstTree) {

        this.subTrees = new ArrayList<Tree>();
        this.subTrees.add(firstTree);
        firstTree.add(firstTree.getRoot());
    }


    public ArrayList<Tree> getSubTrees() {

        return this.subTrees;
    }


    private boolean insertLeft(Tree tree, Node newNode) {

        Node root = tree.getRoot();

        if (root.getLeftSon() != null) {
            return false;
        }

        Tree newSubTree = new Tree(newNode);
        tree.setLeftSubTree(newSubTree);
        newSubTree.setUpperTree(tree);

        root.setLeftSon(newNode);
        newNode.setFather(root);

        this.subTrees.add(newSubTree);
        this.update(newSubTree, newNode);

        return true;
    }


    private boolean insertRight(Tree tree, Node newNode) {

        Node root = tree.getRoot();

        if (root.getRightSon() != null) {
            return false;
        }

        Tree newSubTree = new Tree(newNode);
        tree.setRightSubTree(newSubTree);
        newSubTree.setUpperTree(tree);

        root.setRightSon(newNode);
        newNode.setFather(root);

        this.subTrees.add(newSubTree);
        this.update(newSubTree, newNode);

        return true;
    }


    public boolean insert(Tree tree, Node newNode) {

        int rootValue = tree.getRoot().getValue();
        int newValue = newNode.getValue();

        if (rootValue == newValue) { return false; }

        if (newValue > rootValue) {
            if (this.insertRight(tree, newNode)) {
                return true;
            }
            return insert(tree.getRightSubTree(), newNode);
        }
        else {
            if (this.insertLeft(tree, newNode)) {
                return true;
            }
            return insert(tree.getLeftSubTree(), newNode);
        }
    }


    public boolean fetch(Node node, int value) {

        if (node == null) { //end of tree
            return false;
        }

        if (value == node.getValue()) {
            return true;
        }
        if (value > node.getValue()) {
            return fetch(node.getRightSon(), value);
        }
        return fetch(node.getLeftSon(), value);
    }


    public void update(Tree tree, Node newNode) {

        if (tree != null) {
            tree.add(newNode);
            this.update(tree.getUpperTree(), newNode);
        }
    }


    public static void main(String[] args) {

        // Node[] nodes = {
        //     new Node(50),
        //     new Node(30),
        //     new Node(70),
        //     new Node(20),
        //     new Node(40),
        //     new Node(60),
        //     new Node(80),
        //     new Node(10),
        //     new Node(25),
        //     new Node(35),
        //     new Node(45),
        //     new Node(55),
        //     new Node(65),
        //     new Node(75),
        //     new Node(85),
        // };

        Node[] nodes = {
            new Node(11),
            new Node(10),
            new Node(9),
            new Node(13),
            new Node(12),
            new Node(14),
            new Node(15),
            new Node(16),
        };

        Tree firstTree = new Tree(nodes[0]);
        Avl avl = new Avl(firstTree);
        for (Node node : nodes) {
            avl.insert(firstTree, node);
        }
        for (Tree tree : avl.getSubTrees()) {
            System.out.println(tree);
        }
    }
}