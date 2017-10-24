# =====================================================
# PROBLEM:
# Find the sum of all the multiples of 3 or 5 below 1000 
# =====================================================

def sum_3_5(n):
  return int(reduce((lambda num, sum: num + sum), 
  filter(lambda elt: elt % 3 == 0 or elt % 5 == 0, 
  range(1, n + 1))))

# ===============================================================
# PROBLEM:
# Find the difference between the sum of the squares of the first  
# one hundred natural numbers and the square of the sum.  
# ===============================================================

