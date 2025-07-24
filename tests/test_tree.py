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


    def test_delete(self) -> None:
        self.t.insert(4, 2, 6, 1, 3, 5, 7)

        self.assertTrue(self.t.delete(2))
        self.assertIsNone(self.t.find(2))
        self.assertEqual(self.t.root, 4)
        self.assertIsNotNone(self.t.root.lchild)
        self.assertEqual(self.t.root.lchild, 3)
        self.assertEqual(self.t.root.lchild.parent, 4)
        self.assertIsNone(self.t.root.lchild.rchild)

        self.assertTrue(self.t.delete(3))
        self.assertIsNone(self.t.find(3))
        self.assertEqual(self.t.root, 4)
        self.assertIsNotNone(self.t.root.lchild)
        self.assertEqual(self.t.root.lchild, 1)
        self.assertIsNotNone(self.t.root.lchild.parent, 4)

        self.assertTrue(self.t.delete(6))
        self.assertIsNone(self.t.find(6))
        self.assertEqual(self.t.root, 4)
        self.assertIsNotNone(self.t.root.rchild)
        self.assertEqual(self.t.root.rchild, 7)
        self.assertEqual(self.t.root.rchild.parent, 4)
        self.assertIsNone(self.t.root.rchild.rchild)

        self.assertTrue(self.t.delete(5))
        self.assertIsNone(self.t.find(5))
        self.assertEqual(self.t.root, 4)
        self.assertIsNone(self.t.root.rchild.rchild)
        self.assertIsNone(self.t.root.rchild.lchild)

        self.assertTrue(self.t.delete(4))
        self.assertIsNone(self.t.find(4))
        self.assertEqual(self.t.root, 7)
        self.assertIsNotNone(self.t.root.lchild)
        self.assertEqual(self.t.root.lchild, 1)
        self.assertIsNone(self.t.root.rchild)

        self.assertTrue(self.t.delete(7))
        self.assertIsNone(self.t.find(7))
        self.assertEqual(self.t.root, 1)

        self.assertTrue(self.t.delete(1))
        self.assertIsNone(self.t.find(1))
        self.assertIsNone(self.t.root)


    def test_traverse(self) -> None:
        self.t.insert(4, 2, 6, 1, 3, 5, 7)

        self.assertEqual([k for k in self.t.traverse('preorder')],
                         [4, 2, 1, 3, 6, 5, 7])
        self.assertEqual([k for k in self.t.traverse('inorder')],
                         [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([k for k in self.t.traverse('postorder')],
                         [1, 3, 2, 5, 7, 6, 4])


    def test_rotate_root_left(self) -> None:
        self.t.insert(2, 1, 4, 3, 6, 5, 7)
        self.assertTrue(self.t._rotate_left(self.t.root))
        n4 = self.t.find(4)
        n2 = self.t.find(2)
        n6 = self.t.find(6)
        n1 = self.t.find(1)
        n3 = self.t.find(3)
        n5 = self.t.find(5)
        n7 = self.t.find(7)

        self.assertIsNotNone(n4)
        self.assertEqual(n4, self.t.root)
        self.assertIsNotNone(n4.lchild)
        self.assertEqual(n4.lchild, n2)
        self.assertIsNotNone(n4.lchild.parent)
        self.assertEqual(n4.lchild.parent, n4)
        self.assertIsNotNone(n4.rchild)
        self.assertEqual(n4.rchild, n6)
        self.assertIsNotNone(n4.rchild.parent)
        self.assertEqual(n4.rchild.parent, n4)

        self.assertIsNotNone(n2.lchild)
        self.assertEqual(n2.lchild, n1)
        self.assertIsNotNone(n2.lchild.parent)
        self.assertEqual(n2.lchild.parent, n2)
        self.assertIsNotNone(n2.rchild)
        self.assertEqual(n2.rchild, n3)
        self.assertIsNotNone(n2.rchild.parent)
        self.assertEqual(n2.rchild.parent, n2)

        self.assertIsNotNone(n6.lchild)
        self.assertEqual(n6.lchild, n5)
        self.assertIsNotNone(n6.lchild.parent)
        self.assertEqual(n6.lchild.parent, n6)
        self.assertIsNotNone(n6.rchild)
        self.assertEqual(n6.rchild, n7)
        self.assertIsNotNone(n6.rchild.parent)
        self.assertEqual(n6.rchild.parent, n6)

        self.assertIsNone(n1.lchild)
        self.assertIsNone(n1.rchild)
        self.assertIsNone(n3.lchild)
        self.assertIsNone(n3.rchild)
        self.assertIsNone(n5.lchild)
        self.assertIsNone(n5.rchild)
        self.assertIsNone(n7.lchild)
        self.assertIsNone(n7.rchild)


    def rotate_nonroot_left(self) -> None:
        self.t.insert(2, 1, 4, 3, 6, 5, 7)
        self.assertTrue(self.t._rotate_left(self.t.root.rchild))
        n4 = self.t.find(4)
        n2 = self.t.find(2)
        n6 = self.t.find(6)
        n1 = self.t.find(1)
        n3 = self.t.find(3)
        n5 = self.t.find(5)
        n7 = self.t.find(7)

        self.assertIsNotNone(n2)
        self.assertEqual(n2, self.t.root)
        self.assertIsNotNone(n2.lchild)
        self.assertEqual(n2.lchild, n1)
        self.assertIsNotNone(n2.lchild.parent)
        self.assertEqual(n2.lchild.parent, n2)
        self.assertIsNotNone(n2.rchild)
        self.assertEqual(n2.rchild, n6)
        self.assertIsNotNone(n2.rchild.parent)
        self.assertEqual(n2.rchild.parent, n2)

        self.assertIsNotNone(n6.lchild)
        self.assertEqual(n6.lchild, n4)
        self.assertIsNotNone(n4.parent)
        self.assertEqual(n4.parent, n6)
        self.assertIsNotNone(n6.rchild)
        self.assertEqual(n6.rchild, n7)
        self.assertIsNotNone(n7.parent)
        self.assertEqual(n7.parent, n6)

        self.assertIsNotNone(n4.lchild)
        self.assertEqual(n4.lchild, n3)
        self.assertIsNotNone(n3.parent)
        self.assertEqual(n3.parent, n4)
        self.assertIsNotNone(n4.rchild)
        self.assertEqual(n4.rchild, n5)
        self.assertIsNotNone(n5.parent)
        self.assertEqual(n5.parent, n4)

        self.assertIsNone(n3.lchild)
        self.assertIsNone(n3.rchild)
        self.assertIsNone(n5.lchild)
        self.assertIsNone(n5.rchild)
        self.assertIsNone(n7.lchild)
        self.assertIsNone(n7.rchild)


if __name__ == '__main__':
    unittest.main()
