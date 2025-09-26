w = input("use dashes for wormy length")


length = 0
valid = True

for tuna in w:
  if tuna == "-":
    length += 10
  else:
    valid = False

if length == 0:
  valid = False

if not valid:
  print ("Bad wormy")
else:
  print ("Good wormy your length is " + str (length) + " mm")
