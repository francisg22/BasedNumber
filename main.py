class based_number(object):
  def __init__(self, numberAsString, baseAsInt, sign = "p"):
    self.numberAsString = numberAsString
    self.baseAsInt = baseAsInt
    self._int_value = int(based_number.to_decimal(numberAsString, baseAsInt))
    self.sign = sign
  def to_decimal(num,base):
    return int(num,base)
  def subtract(self, num):
   #STRINGS HAVE TO BE THE SAME LENGTH (AS OF RN)
   #MAKE A FUNCTION TO ADD SOME ZEROS TO THE FRONT OF THE SMALLER STRING
    rv = '0'
    s = self.numberAsString
    s2 = num.numberAsString
    i = len(s)-1
    carry = [0] * (i + 1)
    while i >= 0:
      
      a = (int(carry[i]) + int(s[i])) - int(s2[i])
      if(a == 1):
        rv += '1'
      elif(a == 0):
        rv += '0' 
      else:
        rv += '1'
        carry[i-1] += -1
        
      i -= 1
    rv2 = rv[1:len(rv)]
    return rv2[::-1]

        
        
        
        

if __name__ == "__main__":
  a = based_number("111011",2)
  b = based_number("011101",2)
  print(a.subtract(b))
  print(a._int_value)
  print(b._int_value)