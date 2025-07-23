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


    def test_find(self) -> None:
        self.t.insert(4, 2, 1, 3, 6, 5, 7)

        n4 = self.t.find(4)
        n2 = self.t.find(2)
        n1 = self.t.find(1)
        n3 = self.t.find(3)
        n6 = self.t.find(6)
        n5 = self.t.find(5)
        n7 = self.t.find(7)

        self.assertIsNotNone(n4)
        self.assertEqual(n4, 4)
        self.assertIsNone(n4.parent)
        self.assertEqual(n4, self.t.root)
        self.assertIsNotNone(n4.lchild)
        self.assertEqual(n4.lchild, n2)
        self.assertIsNotNone(n4.lchild.parent)
        self.assertEqual(n4.lchild.parent, n4)
        self.assertIsNotNone(n4.rchild)
        self.assertEqual(n4.rchild, n6)
        self.assertIsNotNone(n4.rchild.parent)
        self.assertEqual(n4.rchild.parent, n4)

        self.assertIsNotNone(n2)
        self.assertEqual(n2, 2)
        self.assertIsNotNone(n2.parent)
        self.assertEqual(n2.parent, n4)
        self.assertIsNotNone(n2.lchild)
        self.assertEqual(n2.lchild, n1)
        self.assertIsNotNone(n2.lchild.parent)
        self.assertEqual(n2.lchild.parent, n2)
        self.assertIsNotNone(n2.rchild)
        self.assertEqual(n2.rchild, n3)
        self.assertIsNotNone(n2.rchild.parent)
        self.assertEqual(n2.rchild.parent, n2)

        self.assertIsNotNone(n1)
        self.assertEqual(n1, 1)
        self.assertIsNotNone(n1.parent)
        self.assertEqual(n1.parent, n2)
        self.assertIsNone(n1.lchild)
        self.assertIsNone(n1.rchild)

        self.assertIsNotNone(n3)
        self.assertEqual(n3, 3)
        self.assertIsNotNone(n3.parent)
        self.assertEqual(n3.parent, n2)
        self.assertIsNone(n3.lchild)
        self.assertIsNone(n3.rchild)

        self.assertIsNotNone(n6)
        self.assertEqual(n6, 6)
        self.assertIsNotNone(n6.parent)
        self.assertEqual(n6.parent, n4)
        self.assertIsNotNone(n6.lchild)
        self.assertEqual(n6.lchild, n5)
        self.assertIsNotNone(n6.lchild.parent)
        self.assertEqual(n6.lchild.parent, n6)
        self.assertIsNotNone(n6.rchild)
        self.assertEqual(n6.rchild, n7)
        self.assertIsNotNone(n6.rchild.parent)
        self.assertEqual(n6.rchild.parent, n6)

        self.assertIsNotNone(n5)
        self.assertEqual(n5, 5)
        self.assertIsNotNone(n5.parent)
        self.assertEqual(n5.parent, n6)
        self.assertIsNone(n5.lchild)
        self.assertIsNone(n5.rchild)

        self.assertIsNotNone(n7)
        self.assertEqual(n7, 7)
        self.assertIsNotNone(n7.parent)
        self.assertEqual(n7.parent, n6)
        self.assertIsNone(n7.lchild)
        self.assertIsNone(n7.rchild)

        n8 = self.t.find(8)
        self.assertIsNone(n8)


if __name__ == '__main__':
    unittest.main()
