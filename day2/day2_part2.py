#!/usr/bin/python3

import re
valid_counter = 0

with open("input.txt", "r") as passwords:
    for password_details in passwords:
        details = re.split('-| |: ', password_details)

        first_ind = int(details[0]) - 1
        second_ind = int(details[1]) - 1

        match_char = details[2]
        word = details[3]

        if (((word[first_ind] == match_char) and (word[second_ind] != match_char)) or ((word[first_ind] != match_char) and (word[second_ind] == match_char))):
          valid_counter += 1

print("Valid passwords: {}".format(valid_counter))
