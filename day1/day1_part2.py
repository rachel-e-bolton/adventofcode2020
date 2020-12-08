#!/usr/bin/python3

# Loop through the list until we have 3 ints whose product is 2020
# Hold the first fixed, hold the second fixed and loop through the list, if nothing is found, iterate one on the second and repeat until we reach the end of the list in the second place, then iterate the first.

def findElements(candidates, elements, total):
  candidates.sort()

  for i in range(elements - 2):
    for j in range(i + 1, elements -1):
      for k in range(j + 1, elements):
        if (int(candidates[i]) + int(candidates[j]) + int(candidates[k])) == total:
          print("Factor 1: {}".format(candidates[i]))
          print("Factor 2: {}".format(candidates[j]))
          print("Factor 3: {}".format(candidates[k]))
          print("Product: {}".format((int(candidates[i]) * int(candidates[j]) * int(candidates[k]))))
          break

with open("day1_input.txt", "r") as file:
  lines = file.readlines()

  elements = len(lines)
  findElements(lines, elements, 2020)