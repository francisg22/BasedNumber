def compare_with_int_value(cls):
    def create_func(name):
        def _do_it(self, other):
            # print('%r %s %r' % (self, name, other))
            if isinstance(other, type(self)):
                return getattr(self._int_value, name)(other._int_value)
            else:
                return getattr(self._int_value, name)(other)
        return _do_it

    for name in ('__ge__','__gt__','__le__','__lt__','__eq__','__ne__'):
        setattr(cls, name, create_func(name))

    return cls
@compare_with_int_value
class based_number(object):
  def __init__(self, numberAsString, baseAsInt, sign = "p"):
    self.numberAsString = numberAsString
    self.baseAsInt = baseAsInt
    #self._int_value = based_number.ecode(numberAsString, baseAsInt)
    self._int_value = sum([int(c)*2**(int(k)) for k,c in enumerate(reversed(numberAsString))])
    
    

  def __getitem__(self,key):
    return self.numberAsString[key]
  #takes two numbers
  #based_number object it is called on has to be greater than num passed through
  
  def __sub__(self, num):
    num.normalize(self)
    
    rv = ''
    s = self.numberAsString
    s2 = num.numberAsString
    i = len(s)-1
    while i >= 0:
      a = int(s[i]) - int(s2[i])
      if(a == 1):
        rv = '1' + rv
      elif(a == 0):
        rv = '0' + rv
      elif(a==-1):
        n = 1
        if(i-n >= 0):
          while(int(s[i-n]) >= 0 and s[i-n] == '0'):
            n+=1
          s = s[:i-n] + '0' + s[i-n + 1:]
          for j in range(n):
            if(i == 0 or i == n-1 ):
              continue
            else:
                s = s[:i-j] + '1' + s[i-j + 1:]
          rv = '1' + rv
        else:
          rv = '1' + rv
      i -= 1
    return based_number(rv,2)
    
  def __add__(self,num):
    pass
    
  def left_shift(self,num):
    return based_number(self.numberAsString + ('0' * num) ,2)
    
  def division(self,num):
    rv = based_number('',2)
    current = based_number('',2)
    dividend = self
    divisor = num
    for i in range(len(dividend.numberAsString)):
      current = based_number(current.numberAsString + dividend.numberAsString[i],2) 
      if( divisor <= current):
        current = current - divisor
        temp = '1'
      else:
        temp = '0'
      rv = based_number(rv.numberAsString + temp,2) 
    return [rv,current]
      
        
      
      

      
    
    
    
      
      
      
     
      
  def normalize(self,num):
    if(len(self.numberAsString)<len(num.numberAsString)):
      diff = len(num.numberAsString) - len(self.numberAsString)
      add = '0' * diff
      self.numberAsString = add + self.numberAsString
    elif(len(self.numberAsString)>len(num.numberAsString)):
      diff = len(self.numberAsString) - len(num.numberAsString)
      add = '0' * diff
      num.numberAsString = add + self.numberAsString
  def compare(self,num):
    if(self._int_value > num._int_value):
      return True
    if (self._int_value == num._int_value):
      return True
    if(self._int_value < num._int_value):
      return True
    
      
      
        
        
        
        

if __name__ == "__main__":
  a = based_number("1100",2)
  b = based_number("101",2)
  c = based_number("001100",2)
  d = based_number("01100",2)
  print((c-d).numberAsString)
  # print(c._int_value)
  # print(d._int_value)
  # print(c-d)
  # f = c<d
  # print('f= ' + str(f))
  # f = c.subtract(d)
  # print('c - d=' + f)
  # f = based_number(f,2)
  # print(f.numberAsString)
  # print(based_number.to_decimal(f,2))
  print("a in binary = " + a.numberAsString + ' a in decimal = ' +str(a._int_value))
  print("b in binary = " + b.numberAsString + ' b in decimal = ' +str(b._int_value))
  

  # b.normalize(a)
  quotient = a.division(b)
  print('A / B')
  print('Quotient = ' + quotient[0].numberAsString + "     as int = " + str(quotient[0]._int_value))
  print('remainder = ' + quotient[1].numberAsString + "    as int = " + str(quotient[1]._int_value))
  