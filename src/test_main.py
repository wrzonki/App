import unittest
import main


class TestMain(unittest.TestCase):
  def test_add(self):
    result = main.add(10, 5)
    self.assertEquals(result, 15)