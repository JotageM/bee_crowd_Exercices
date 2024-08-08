
from math import sqrt
def is_prime(num):
  for i in range(2, int(sqrt(num))+1):
      if num % i == 0:
          return False
  return True

n = int(input())
for i in range(n):
    num = int(input())

    is_num_prime = is_prime(num)

    if (is_num_prime):
        print("Prime")
    else:
        print("Not Prime")  

