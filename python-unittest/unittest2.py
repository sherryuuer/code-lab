import unittest
import to_be_test


class testmain(unittest.TestCase):

    def test_do_stuff3(self):
        test_param = None
        result = to_be_test.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self):
        test_param = ""
        result = to_be_test.do_stuff(test_param)
        self.assertEqual(result, "please enter number")


if __name__ == '__main__':
    unittest.main()


# how to run all unittest files
# >python3 -m unittest
# this one can list all the def test result
# >python3 -m unittest -v
