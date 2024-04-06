#!/bin/python

def readNums(array, target):
  array = input("Enter numbers seperated by comma : ").split(", ")
  nums = [0 for i in range(len(array))]

  for i in range(len(nums)):
    nums[i] = int(array[i])

  array = nums

#def twoSum(array=[]):
#  print(array)

array = []
target = 0

#twoSum(readNums(array, target))
readNums(array, target)

print(array)
