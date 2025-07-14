import unittest
from avl.tree import Tree


class TestTree(unittest.TestCase):
    def setUp(self) -> None:
        self.t = Tree()

    def tearDown(self) -> None:
        del self.t

    def test_insert(self) -> None:
        self.t.insert(8)
        self.assertIsNotNone(self.t.root)
        self.t.insert(6)
        self.assertIsNotNone(self.t.root.lchild)
        self.assertEqual(self.t.root.lchild.key, 6)
        self.t.insert(9)
        self.assertIsNotNone(self.t.root.rchild)
        self.assertEqual(self.t.root.rchild.key, 9)

    def test_find(self) -> None:
        self.t.insert(8)
        self.assertTrue(self.t.find(8))
        self.t.insert(6)
        self.assertTrue(self.t.find(6))
        self.assertFalse(self.t.find(9))
        self.t.insert(9)
        self.assertTrue(self.t.find(9))


if __name__ == '__main__':
    unittest.main()
