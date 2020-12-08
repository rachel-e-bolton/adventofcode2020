#!/usr/bin/python3
index = 0
tree_count = 0

with open("input.txt", "r") as rows:
  for row in rows:
    row = row.strip()
    max_index = len(row) - 1

    if (row[index] == "#"):
      tree_count += 1

    if (index + 3 <= max_index):
      index += 3
    else:
      index = (index + 3 - max_index - 1)

print("Trees encountered: {}".format(tree_count))