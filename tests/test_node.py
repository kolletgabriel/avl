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


if __name__ == '__main__':
    unittest.main()
