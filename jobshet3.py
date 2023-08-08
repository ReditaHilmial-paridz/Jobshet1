import random
from guess import tbkangka

tebak=int(input('tebak angka '))
jawab=random.randint(1,10)

jawaban1=tbkangka(tebak,jawab)

if jawaban1:
  print ("you win")
else:
  print ('you lose')