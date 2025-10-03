
word = input("enter a word does it have double letters or not? give it a thought.")

double = False
for i in range(len(word) - 1):
  if word[i]== word[i+1]:
    double = True
    
if double:
  print ("you are correct")
else:
  print ("NUH UH")




