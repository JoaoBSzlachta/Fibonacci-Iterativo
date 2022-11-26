import time


class Fibonacci:

  def __init__(self):
    self.first = 0
    self.second = 1

  def Func(self, value):
    i = 0
    aux = 0
    temp = aux
    while (i < value):
      temp = aux
      if value == 1:
        print(self.first)
      elif value == 2:
        print(self.second)
      else:
        aux = self.first + self.second

        self.second = self.first
        self.first = aux
      i = i + 1
    print(temp)


start = time.time()
fib = Fibonacci()

fib.Func(30)

end = time.time()
print(f"{end - start}")
