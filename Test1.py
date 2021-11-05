import unittest
from main import matchingSocks

class TestMatchingSocks(unittest.TestCase):

    def test_match(self):

        res = matchingSocks(7, (1, 1, 3, 2, 3, 2, 4))
        self.assertEqual(res, 3)

if __name__ == '__main__':
    unittest.main()