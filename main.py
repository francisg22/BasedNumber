class based_number(object):
  def __init__(self, numberAsString, baseAsInt, sign = "p"):
    self.numberAsString = numberAsString
    self.baseAsInt = baseAsInt
    self._int_value = int(based_number.to_decimal(numberAsString, baseAsInt))
    self.sign = sign
    
  @staticmethod
  def to_decimal(num,base):
    return int(num,base)
  def subtract(self, num):
   #STRINGS HAVE TO BE THE SAME LENGTH (AS OF RN)
   #MAKE A FUNCTION TO ADD SOME ZEROS TO THE FRONT OF THE SMALLER STRING
    num.normalize(self)
    print(self.numberAsString)
    print(num.numberAsString)
    if(num._int_value > self._int_value):
      return "no"
    rv = ''
    s = self.numberAsString
    s2 = num.numberAsString
    i = len(s)-1
    # carry = [0] * (i + 1)
    while i >= 0:
      print(str(i) + " loop " + " a = " +s[i])
      print(str(i) + " loop " + " b = " +s2[i])
      a = int(s[i]) - int(s2[i])
      if(a == 1):
        rv = '1' + rv
      elif(a == 0):
        rv = '0' + rv
      elif(a==-1):
        n = 1
        if(i-n >= 0):
          while(int(s[i-n]) >= 0 and s[i-n] == '0'):
            
            # s = s[:i-n] + '1' + s[i-n + 1:]
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
      
            
        # carry[i-1] = -1
        
      
        
      print( str(i) + " loop " + rv)  
      i -= 1
    print(rv)
    
    
    return rv
    
  # def division(self,num):
  #   if(self._int_value < num._int_value):
  #     return "Number less than 0"
  #   rv = ""
  #   current = ""
  #   pos = 0
  #   # print(self.numberAsString)
  #   # print(self.numberAsString[pos:pos+len(num.numberAsString)])
  #   # while len(current)< len(num.numberAsString):
    
  #   current = based_number(self.numberAsString[pos:pos+len(num.numberAsString)],2)
    
  #   # print(current.numberAsString + ' '+ str(current._int_value))
  #   temp = current.subtract(num)
  #   if(temp == 'no'):
  #     current = based_number(self.numberAsString[pos:pos+1+len(num.numberAsString)],2)
  #   # print(current.numberAsString + ' '+ str(current._int_value))
  #   # print(num.numberAsString + ' ' +str(num._int_value))
  #   temp = current.subtract(num)
    # print( temp + ' ' + str(based_number.to_decimal(temp,2)))
      
  def normalize(self,num):
    if(len(self.numberAsString)<len(num.numberAsString)):
      diff = len(num.numberAsString) - len(self.numberAsString)
      add = '0' * diff
      self.numberAsString = add + self.numberAsString
    elif(len(self.numberAsString)>len(num.numberAsString)):
      diff = len(self.numberAsString) - len(num.numberAsString)
      add = '0' * diff
      num.numberAsString = add + self.numberAsString
    
      
      
        
        
        
        

if __name__ == "__main__":
  a = based_number("10010000",2)
  b = based_number("1100",2)
  c = based_number("1010010",2)
  d = based_number("101010",2)
  print(c._int_value)
  print(d._int_value)
  f = c.subtract(d)
  # print(based_number.to_decimal(f,2))
  print('c - d=' + f)
  # b.normalize(a)
  # print(a.division(b))
  print(a._int_value)
  print(b._int_value)