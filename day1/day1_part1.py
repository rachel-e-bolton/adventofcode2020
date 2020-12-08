#!/usr/bin/python3

def checkSum(candidate, lines_list):
  """
  Function keeps iterating through list the until a complementary digit is found to sum to 2020. 
  Returns the complement.
  """
  for line in lines_list:
    complement = int(line)
    if candidate + complement == 2020:
      return complement

  return 0

with open("day1_input.txt", "r") as file_main:
  lines = file_main.readlines()
  lines_dup = file_main.readlines()

  for line in lines:
    candidate = int(line)
    complement = int(checkSum(candidate, lines))
    if candidate + complement == 2020:
      print("Candidate: {}".format(candidate))
      print("Complement: {}".format(complement))
      print("Product: {}".format((candidate*complement)))
      break


