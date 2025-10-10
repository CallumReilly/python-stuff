names = []

name = input ("Enter a name:")
if name:
  names.append(name)
while name:
  name = input ("Enter a name:")
  if name:
    names.append(name)

for name in names:
  print ("hi " + name)
