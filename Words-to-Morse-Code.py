Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' , 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
TunaCode = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
a = list(input ("enter a word and it will translate to morse code"))
print (a)
for i in range(len(a)):
  for b in range(len(Alphabet)):
    if (Alphabet[b]  ==  a[i]):
      print (TunaCode[b])
