def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# 6+5+4+3+2+1 = 21
# 5+4+3+2+1 = 15
# 4+3+2+1 = 10
# 3+2+1 = 6
# 2+1 = 3
# 1 = 1
