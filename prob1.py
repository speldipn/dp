import time


def fact_recur(n):
  return 1 if n <= 1 else (n * fact_recur(n - 1))


def fact_travel(n):
  fact = 1
  for n in range(1, n + 1):
    fact *= n
  return fact


def measure(func):
  start = time.time()
  func(20)  # print number count
  end = time.time()
  print('elapsed time:', end - start)


def recurFactorial(count):
  print("[recursive]")
  for n in range(0, count + 1):
    print('{}! => {}'.format(n, fact_recur(n)))


def nonRecurFactorial(count):
  print("\n[non-recursive]")
  for n in range(0, count + 1):
    print('{}! => {}'.format(n, fact_travel(n)))


measure(recurFactorial)
measure(nonRecurFactorial)
