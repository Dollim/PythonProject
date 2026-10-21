
import random

pioche = [(i,j) for i in range(7) for j in range(i,7)]


print(pioche)

random.shuffle(pioche)

print(pioche)

main1= [pioche.pop() for _ in range(7)]
main2= [pioche.pop() for _ in range(7)]


print(main1)
print(main2)

print(pioche)

