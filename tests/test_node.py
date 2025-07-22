import unittest
from avl.node import Node


class TestNode(unittest.TestCase):
    def setUp(self) -> None:
        self.n = Node(5)

    def tearDown(self) -> None:
        del self.n

    def test_comparsions(self) -> None:
        self.assertEqual(self.n, Node(5))
        self.assertEqual(self.n, 5)
        self.assertGreater(self.n, Node(4))
        self.assertGreater(self.n, 4)
        self.assertGreaterEqual(self.n, Node(5))
        self.assertGreaterEqual(self.n, 5)
        self.assertGreaterEqual(self.n, Node(4))
        self.assertGreaterEqual(self.n, 4)
        self.assertLess(self.n, Node(6))
        self.assertLess(self.n, 6)
        self.assertLessEqual(self.n, Node(5))
        self.assertLessEqual(self.n, 5)
        self.assertLessEqual(self.n, Node(6))
        self.assertLessEqual(self.n, 6)
        self.assertNotEqual(self.n, Node(4))
        self.assertNotEqual(self.n, 4)


if __name__ == '__main__':
    unittest.main()
