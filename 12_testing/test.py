#python -m unittest -v calls comments as well

import unittest
import main

# standard way of working with unittest
class TestMain(unittest.TestCase):
    
    def setUp(self) -> None:
        test_method = getattr(self, self._testMethodName)
        print(f'\nRUNNING: {self._testMethodName.upper()}\n**********')
        print(f'Docstring: {test_method.__doc__ or "No description"}')
        return super().setUp()
    
    
    def test_do_stuff(self):
        """
        Docstrings will be included like this.
        """
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_param = 'some string'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number.')

    def tearDown(self) -> None:
        print('***************************************************')
        print('DONE')

if __name__ == '__main__':
    unittest.main()