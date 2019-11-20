def merge(a, b):
  start_index = len(b) - len(a)
  for i in a:
    b[start_index] = i
    start_index += 1
  return sorted(b)

def merge(a, b):
  a_index = len(a) - 1
  b_index = len(b) - len(a) - 1
  end = -1
  while a_index >= 0 and b_index >= 0:
    if a[a_index] > b[b_index]:
      b[end] = a[a_index]
      a_index -= 1
      end -= 1
    else:
      b[end] = b[b_index]
      b_index -= 1
      end -= 1
  if a_index < 0:
    for i in range(0, b_index):
      b[end] = b[b_index]
      b_index -= 1
      end -= 1
  else:
    for i in range(0, a_index):
      a[end] = a[a_index]
      a_index -= 1
      end -= 1
  return b
