"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
  # Convert the inputs to binary vectors.
  xvec = x.binary_vec
  yvec = y.binary_vec
  
  # Pad the shorter vector to match the length of the longer one.
  xvec, yvec = pad(xvec, yvec)
  # Base case: if both numbers are 1 or 0, multiply them directly.
  if x.decimal_val <= 1 and y.decimal_val <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)
  else:
    # Split the binary vectors of x and y into left and right parts.
    xvec_l, xvec_r = split_number(xvec) 
    yvec_l, yvec_r = split_number(yvec) 
    # multiply the left parts and the right parts of x and y.
    z1 = subquadratic_multiply(xvec_l, yvec_l) 
     # Multiply the sums of left and right halves of both x and y.
    z2 = subquadratic_multiply(
        BinaryNumber(xvec_l.decimal_val + xvec_r.decimal_val),
        BinaryNumber(yvec_l.decimal_val + yvec_r.decimal_val))
    z3 = subquadratic_multiply(xvec_r, yvec_r)
   
    # Shift the difference (z2 - z1 - z3) left by half the length (for the middle terms)
    bin_dif = BinaryNumber(z2.decimal_val - z1.decimal_val - z3.decimal_val)
    
   # Combine the results according to Karatsuba method:
  result = bit_shift(z1, len(xvec)).decimal_val + bit_shift(
      bin_dif, len(xvec) // 2).decimal_val + z3.decimal_val

  return BinaryNumber(result)



def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

