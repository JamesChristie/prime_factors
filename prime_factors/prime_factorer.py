class PrimeFactorer:
  def __init__(self, factorable):
    self.factorable = factorable
    self.result     = None

  def generate(self):
    self.result = []

    if self.factorable > 1:
      self.result.append(2)
