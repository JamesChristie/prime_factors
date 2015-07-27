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

class TestPrimeFactorerForThree(unittest.TestCase):
  def setUp(self):
    self.factorer = PrimeFactorer(3)
    self.factorer.generate()

  def test_two(self):
    self.assertEqual(self.factorer.result, [3])

class TestPrimeFactorerForFour(unittest.TestCase):
  def setUp(self):
    self.factorer = PrimeFactorer(4)
    self.factorer.generate()

  def test_four(self):
    self.assertEqual(self.factorer.result, [2, 2])
