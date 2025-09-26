v = input ("enter the video length you want in __:__")
times = v.split(":")
min = int(times[0])
sec = int(times[1])

print (min*60 + sec)
