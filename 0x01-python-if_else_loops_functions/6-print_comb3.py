#!/usr/bin/python3

#89 is the largest of these numbers
for i in range(1, 89):

  # switch places ex. 17 -> 71 then take the smaller
  if ((i/10 + (i % 10) * 10) < i) or i % 11 == 0:
    continue

  print("{:>02}, ".format(i), end="")

print("{}".format(89))
