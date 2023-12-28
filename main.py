# Python Arbitrary Arguments
def my_function(*kids):

  print("The youngest child is " + kids[0])
  print("The youngest child is " + kids[1])
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")