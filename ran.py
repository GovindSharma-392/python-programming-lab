#WAP TO RETURN RANDOM NUMBER.
import random

l = [11, 12, 51, 14, 58, 64]
print(random.choice(l))

print("A random number between 0 and 1 is: ", end="")
print(random.random())

random.seed(5)

print("The mapped random number with 5 is: ", end="")
print(random.random())

random.seed(7)

print("The mapped random number with 7 is: ", end="")
print(random.random())