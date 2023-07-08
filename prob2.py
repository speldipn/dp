def acc(num, idx):
  result = []
  printArr(num)
  recur(num, idx, result)
  printArr(result)

def recur(num, idx, result):
  if idx >= len(num):
    return 0

  arr = []
  for i in range(idx+1):
    arr.append(num[i])

  sum = 0
  for i in range(len(arr)):
    sum += arr[i]
  result.append(sum)

  return num[idx] + recur(num, idx + 1, result)

def printArr(arr):
  print(len(arr), arr)

sample = [1, 2, 3, 4, 5, 6]
acc(sample, 0)
