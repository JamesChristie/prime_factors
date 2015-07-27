import unittest

from prime_factors.prime_factorer import PrimeFactorer

class TestPrimeFactorerForOne(unittest.TestCase):
  def setUp(self):
    self.factorer = PrimeFactorer(1)
    self.factorer.generate()

  def test_one(self):
    self.assertEqual(self.factorer.result, [])

class TestPrimeFactorerForTwo(unittest.TestCase):
  def setUp(self):
    self.factorer = PrimeFactorer(2)
    self.factorer.generate()

  def test_two(self):
    self.assertEqual(self.factorer.result, [2])
