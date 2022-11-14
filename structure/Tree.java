package structure;

import java.util.ArrayList;


public class Tree {

    private Node root;
    private Tree upperTree;
    private Tree leftSubTree;
    private Tree rightSubTree;
    private ArrayList<Node> nodes;
    private ArrayList<Node> leaves;
    private int height;
    private int balanceFactor;
    private int size;


    public Tree(Node root) {

        this.root = root;
        this.nodes = new ArrayList<Node>();
        this.leaves = new ArrayList<Node>();
    }


    public                 Node getRoot()                         { return this.root;                   }
    public            Tree getUpperTree()                         { return this.upperTree;              }
    public          Tree getLeftSubTree()                         { return this.leftSubTree;            }
    public         Tree getRightSubTree()                         { return this.rightSubTree;           }
    public     ArrayList<Node> getNodes()                         { return this.nodes;                  }
    public    ArrayList<Node> getLeaves()                         { return this.leaves;                 }
    public                int getHeight()                         { return this.height;                 }
    public         int getBalanceFactor()                         { return this.balanceFactor;          }
    public                  int getSize()                         { return this.size;                   }


    public                 void setRoot( Node root                 ) { this.root = root;                   }
    public            void setUpperTree( Tree upperTree            ) { this.upperTree = upperTree;         }
    public          void setLeftSubTree( Tree leftSubTree          ) { this.leftSubTree = leftSubTree;     }
    public         void setRightSubTree( Tree rightSubTree         ) { this.rightSubTree = rightSubTree;   }
    public                void setNodes( ArrayList<Node> nodes     ) { this.nodes = nodes;                 }
    public               void setLeaves( ArrayList<Node> leaves    ) { this.leaves = leaves;               }
    public               void setHeight( int height                ) { this.height = height;               }
    public        void setBalanceFactor( int balanceFactor         ) { this.balanceFactor = balanceFactor; }
    public                 void setSize( int size                  ) { this.size = size;                   }


    private void checkLeaves() {
        
        ArrayList<Node> leaves = new ArrayList<Node>();

        for (Node node : this.nodes) {
            if (node.isLeaf()) {
                leaves.add(node);
            }
        }

        this.setLeaves(leaves);
    }


    private int countUpwardsFrom(Node node, int auxVar) {
        
        auxVar++;
        if (node == this.root) {
            return auxVar;
        }
        return countUpwardsFrom(node.getFather(), auxVar);
    }


    private void computeHeight() {
        
        int longestPath = 0;
        for (Node leaf : this.leaves) {
            int count = 0;
            int thisPath = this.countUpwardsFrom(leaf, count);
            if (thisPath > longestPath) {
                longestPath = thisPath;
            }
        }
        this.setHeight(longestPath);
    }


    private void computeBalanceFactor() {

        if (this.leftSubTree == null  &&  this.rightSubTree == null) {
            this.setBalanceFactor(0);
        }
        else if (this.leftSubTree == null) {
            int balanceFactor = -this.rightSubTree.getHeight();
            this.setBalanceFactor(balanceFactor);
        }
        else if (this.rightSubTree == null) {
            int balanceFactor = this.leftSubTree.getHeight();
            this.setBalanceFactor(balanceFactor);
        }
        else {
            int balanceFactor = this.leftSubTree.getHeight() - this.rightSubTree.getHeight();
            this.setBalanceFactor(balanceFactor);
        }
    }


    public void add(Node newNode) {

        this.nodes.add(newNode);
        this.leaves.add(newNode);
        this.checkLeaves();
        this.computeHeight();
        this.computeBalanceFactor();
        this.size++;
    }


    public String toString() {

        String nodesList = "";
        String leavesList = "";

        for (Node node : this.nodes) {
            nodesList += String.format("%d ", node.getValue());
        }

        for (Node leaf : this.leaves) {
            leavesList += String.format("%d ", leaf.getValue());
        }

        return String.format(
            "\nroot: %d\nnodes: %s\nleaves: %s\nheight: %d\nsize: %d\nfactor: %d",
            this.root.getValue(), nodesList, leavesList, this.height, this.size, this.balanceFactor
        );
    }


    public static void main(String[] args) {

    }
}