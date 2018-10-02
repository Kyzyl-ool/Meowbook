from app.helper import mul
import unittest

class TestMul(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
