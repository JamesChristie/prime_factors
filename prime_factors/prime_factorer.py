class PrimeFactorer:
  def __init__(self, factorable):
    self.factorable = factorable
    self.primes     = []

  def generate(self):
    factor_candidate = 2

    while self.factorable > 1:
      while self.__candidate_is_factor(factor_candidate):
        self.primes.append(factor_candidate)
        self.factorable = int(
          self.factorable / factor_candidate
        )
      factor_candidate += 1

  # Private

  def __candidate_is_factor(self, factor_candidate):
    remainder = self.factorable % factor_candidate
    return remainder == 0
