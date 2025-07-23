import unittest
from avl.tree import Tree


class TestTree(unittest.TestCase):

    def setUp(self) -> None:
        self.t = Tree()

    def tearDown(self) -> None:
        del self.t


    def test_single_insert(self) -> None:
        self.assertTrue(self.t.insert(2))
        self.assertIsNotNone(self.t.root)
        self.assertEqual(self.t.root, 2)

        self.assertTrue(self.t.insert(1))
        self.assertIsNotNone(self.t.root.lchild)
        self.assertEqual(self.t.root.lchild, 1)
        self.assertIsNotNone(self.t.root.lchild.parent)
        self.assertEqual(self.t.root.lchild.parent, self.t.root)

        self.assertTrue(self.t.insert(3))
        self.assertIsNotNone(self.t.root.rchild)
        self.assertEqual(self.t.root.rchild, 3)
        self.assertIsNotNone(self.t.root.rchild.parent)
        self.assertEqual(self.t.root.rchild.parent, self.t.root)

        self.assertFalse(self.t.insert(2))
        self.assertFalse(self.t.insert(1))
        self.assertFalse(self.t.insert(3))


    def test_multi_insert(self) -> None:
        self.assertTrue(self.t.insert(2, 1, 3))

        self.assertIsNotNone(self.t.root)
        self.assertEqual(self.t.root, 2)

        self.assertIsNotNone(self.t.root.lchild)
        self.assertEqual(self.t.root.lchild, 1)
        self.assertIsNotNone(self.t.root.lchild.parent)
        self.assertEqual(self.t.root.lchild.parent, self.t.root)

        self.assertIsNotNone(self.t.root.rchild)
        self.assertEqual(self.t.root.rchild, 3)
        self.assertIsNotNone(self.t.root.rchild.parent)
        self.assertEqual(self.t.root.rchild.parent, self.t.root)

        self.assertTrue(self.t.insert(2, 1, 3, 4))

        self.assertIsNotNone(self.t.root.rchild.rchild)
        self.assertEqual(self.t.root.rchild.rchild, 4)
        self.assertIsNotNone(self.t.root.rchild.rchild.parent)
        self.assertEqual(self.t.root.rchild.rchild.parent, self.t.root.rchild)

        self.assertFalse(self.t.insert(2, 1, 3))


if __name__ == '__main__':
    unittest.main()
