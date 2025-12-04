import random
import my_module

print(random.randint(1,10))
print(my_module.my_fav_number)
print(random.random()*(2**40))


luck = random.randint(1,2)

if luck == 1:
    print("Heads")
else:
    print("Tails")