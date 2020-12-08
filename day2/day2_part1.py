#!/usr/bin/python3
import re
valid_counter = 0

with open("input.txt","r") as passwords:
  for password_details in passwords:
    details = re.split('-| |: ',password_details)
    letter_count = details[3].count(details[2])
    if (int(details[0]) <= letter_count <= int(details[1])):
      valid_counter += 1

print("Valid passwords: {}".format(valid_counter))
    