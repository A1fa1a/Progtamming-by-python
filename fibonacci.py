#!/bin/python

import time

def fibonacci(num):
  prev, next = 0, 1

  for _ in range(1, num):
    prev, next = next, prev + next

  return next

s = time.perf_counter()
print(fibonacci(6))
e = time.perf_counter()
print(f"Done in {e - s:.4f}s")
