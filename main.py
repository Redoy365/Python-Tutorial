class Math:
  def __init__(self):
    pass

  def sum(self,*arg):
    return arg[0]+arg[1]
  def sub(self,*arg):
    return arg[0]-arg[1]

Math = Math()

n = Math.sum(10,2)
print(n)
n = Math.sub(10,2)
print(n)