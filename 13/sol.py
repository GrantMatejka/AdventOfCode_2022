import ast

def isIntEqual(left, right):
  if left < right:
    return True
  elif left > right:
    return False

def isEqual(left, right):
  L = left
  R = right
  if left is list and right is not list:
    R = [right]
  if left is not list and right is list:
    L = [left]

  print(L,R)
  # If the left list runs out of items first, the inputs are in the right order.
  for i in range(len(L)):
    # If the right list runs out of items first, the inputs are not in the right order.
    if i == len(R):
      return False

    lVal = L[i]
    rVal = L[i]
    result = None
    if isinstance(lVal, int) and isinstance(rVal, int):
      result = isIntEqual(lVal, rVal)
    else:
      result = isEqual(lVal, rVal)

    if result == False:
      return result

  return True

with open('test_input.txt', 'r') as f:
  parse = [p.split('\n') for p in f.read().split('\n\n')]
  pairs = [[ast.literal_eval(pair[0]), ast.literal_eval(pair[1])] for pair in parse]
  result = [isEqual(pair[0], pair[1]) for pair in pairs]
  print(result)
