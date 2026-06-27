import unittest
import to_be_test


class testmain(unittest.TestCase):

    def setUp(self):
        print("Run the function!")

    def test_do_stuff(self):
        """helloooooo!"""
        test_param = 10
        result = to_be_test.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "blala"
        result = to_be_test.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
        # or
        # self.assertTrue(isinstance(result, ValueError))

    def tearDown(self) -> None:
        return super().tearDown()
        # print("Clear up!")


if __name__ == '__main__':
    unittest.main()


# how to run all unittest files
# try these
# >python3 -m unittest
# this one can list all the def test result
# >python3 -m unittest -v

# need to use the python path
# PS C:\Users\sherr\Desktop\code-lab> cd .\python-concepts  
# PS C:\Users\sherr\Desktop\code-lab\python-concepts> C:/Users/sherr/AppData/Local/Programs/Python/Python311/python.exe -m unittest -v
# test_do_stuff (test1.testmain.test_do_stuff)
# helloooooo! ... Run the function!
# ok
# test_do_stuff2 (test1.testmain.test_do_stuff2) ... Run the function!
# ok
# test_do_stuff3 (test2.testmain.test_do_stuff3) ... ok     
# test_do_stuff4 (test2.testmain.test_do_stuff4) ... ok     

# ----------------------------------------------------------------------
# Ran 4 tests in 0.003s

# OK
# PS C:\Users\sherr\Desktop\code-lab\python-concepts> 
