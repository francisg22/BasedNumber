class based_number(object):
  def __init__(self, numberAsString, baseAsInt):
    self.numberAsString = numberAsString
    self.baseAsInt = baseAsInt
    self._int_value = int(based_number.to_decimal(numberAsString, baseAsInt))
  def to_decimal(num,base):
    return int(num,base)
#test


if __name__ == "__main__":
  a = based_number("01011",2)
  print(a._int_value)