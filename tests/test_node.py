import unittest
from avl.node import Node


class TestNode(unittest.TestCase):
    def setUp(self) -> None:
        self.n = Node(5)

    def tearDown(self) -> None:
        del self.n

    def test_isroot(self) -> None:
        self.assertTrue(self.n.isroot)
        self.n.parent = Node(2)
        self.assertFalse(self.n.isroot)

    def test_isleaf(self) -> None:
        self.assertTrue(self.n.isleaf)
        self.n.lchild = Node(2)
        self.assertFalse(self.n.isleaf)

    def test_height(self) -> None:
        self.assertEqual(self.n.height, 1)
        self.n.lchild = Node(3)
        self.n.lchild.parent = self.n
        self.assertEqual(self.n.lchild.height, 2)
        self.n.lchild.lchild = Node(2)
        self.n.lchild.lchild.parent = self.n.lchild
        self.assertEqual(self.n.lchild.lchild.height, 3)
        self.n.lchild.rchild = Node(4)
        self.n.lchild.rchild.parent = self.n.lchild
        self.assertEqual(self.n.lchild.rchild.height, 3)
        self.n.rchild = Node(6)
        self.n.rchild.parent = self.n
        self.assertEqual(self.n.rchild.height, 2)
        self.n.rchild.rchild = Node(8)
        self.n.rchild.rchild.parent = self.n.rchild
        self.assertEqual(self.n.rchild.rchild.height, 3)
        self.n.rchild.lchild = Node(7)
        self.n.rchild.lchild.parent = self.n.rchild
        self.assertEqual(self.n.rchild.lchild.height, 3)


if __name__ == '__main__':
    unittest.main()
