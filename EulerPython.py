# ======================================================
# PROBLEM:
# Find the sum of all the multiples of 3 or 5 below 1000 
# ======================================================

def sum_3_5(n):
  return int(reduce((lambda num, sum: num + sum), 
  filter(lambda elt: elt % 3 == 0 or elt % 5 == 0, 
  range(1, n + 1))))

# =====================================
# PROBLEM:
# Design your own implementation of map
# =====================================

def my_map(f, lox):
  return [f(x) for x in lox]

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

# Alternatively, one could also do:
# def my_filter(f, lox):
#   return [f(x) if f(x) is True for x in lox]

# =========================================================================
# PROBLEM:
# Design a function which determines whether a given string is a palindrom
# =========================================================================

def palindrome(str):
  if len(str) <= 1:
    return True
  else:
    start = 0
    end = len(str) - 1

    while end > start:
      if str[end] != str[start]:
        return False

      end -= 1
      start += 1

    return True

# =============================================
# PROBLEM:
# Design a function which interleaves two lists
# =============================================

def interleave(list1, list2):
  interleaved = []
  index = 0

  while len(list1) != 0 or len(list2) != 0:
    if len(list1) != 0:
      interleaved.append(list1[index])
    if len(list2) != 0:
      interleaved.append(list2[index])
    
    index += 1

  return interleaved


def binary_search(array, target, num_items):
  return search_helper(array, target, 0, num_items - 1)

def search_helper(array, target, begin_index, end_index):
  mid_index = begin_index + (end_index - begin_index) / 2

  if begin_index > end_index:
    return -1
  elif array[mid_index] == target:
    return mid_index
  elif array[mid




