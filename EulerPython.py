# =====================================================
# PROBLEM:
# Find the sum of all the multiples of 3 or 5 below 1000 
# =====================================================

def sum_3_5(n):
  return int(reduce((lambda num, sum: num + sum), 
  filter(lambda elt: elt % 3 == 0 or elt % 5 == 0, 
  range(1, n + 1))))

# =====================================
# PROBLEM:
# Design your own implementation of map
# =====================================

def my_map(f, lox):
  result = []
  for x in lox:
    result.append(f(x))

  return result

# ========================================
# PROBLEM:
# Design your own implementation of filter
# ========================================

def my_filter(f, lox)
  result = []
  for x in lox:
    if f(x) is True:
      result.append(x)

  return result


