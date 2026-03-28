import time
import numpy as np

# 1M numbers
lst = list(range(1_000_000))
arr = np.array(lst)

# Python list sum
start = time.time()
sum(lst)
print("List sum time:", time.time()-start)

# NumPy array sum
start = time.time()
np.sum(arr)
print("NumPy sum time:", time.time()-start)