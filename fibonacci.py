import numpy as np

def fibonacci(number_of_sequence):
  array = np.zeros(number_of_sequence)
  for x in range(0,number_of_sequence):
    if(x == 0 or x == 1):
      array[x] = 1
    else:
      array[x] = array[x-2] + array[x-1]
  return array

print(fibonacci(10))