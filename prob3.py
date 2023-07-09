def printTable(n): 
  print("[recursive]")
  for i in range(1, 10):
    print("{} x {} = {}".format(n, i, n*i))


def printRecurTable(n):
  print("\n[non-recursive]")
  recur(n, 1)

def recur(n, mul):
  if mul > 9: return
  print("{} x {} = {}".format(n, mul, n * mul))
  recur(n, mul + 1)

printTable(5)
printRecurTable(5)
