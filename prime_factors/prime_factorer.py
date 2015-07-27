class PrimeFactorer:
  def __init__(self, factorable):
    self.factorable = factorable
    self.primes     = None

  def generate(self):
    self.primes = []

    if self.__two_is_factor():
      self.primes.append(2)
      self.factorable = int(self.factorable / 2)

    if self.factorable > 1:
      self.primes.append(self.factorable)

  # Private

  def __two_is_factor(self):
    remainder = self.factorable % 2
    return remainder == 0
