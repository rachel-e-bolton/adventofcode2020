#!/usr/bin/python3
product = 0

def slopeSpecificCount(across, down):
  index = 0
  tree_count = 0
  row_count = 0

  with open("input.txt", "r") as rows:
    for row in rows:
      if ((row_count % down) == 0):
        row = row.strip()
        max_index = len(row) - 1

        if (row[index] == "#"):
          tree_count += 1

        if (index + across <= max_index):
          index += across
        else:
          index = (index + across - max_index - 1)
      row_count += 1
    return tree_count

print("Slope 1: {} trees".format(slopeSpecificCount(1,1)))
print("Slope 2: {} trees".format(slopeSpecificCount(3,1)))
print("Slope 3: {} trees".format(slopeSpecificCount(5,1)))
print("Slope 4: {} trees".format(slopeSpecificCount(7,1)))
print("Slope 5: {} trees".format(slopeSpecificCount(1,2)))

product = (slopeSpecificCount(1,1)*slopeSpecificCount(3,1)*slopeSpecificCount(5,1)*slopeSpecificCount(7,1)*slopeSpecificCount(1,2))

print("Product of trees encountered: {}".format(product))
