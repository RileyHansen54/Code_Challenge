# for number in range(0,101, 2):
#     print(number)
#
#
# x = 0
# for number in range(1,101):
#     x +=number
#
# print(x)
#
# y = (101 * 100)/2
# print(y)


for x in range(1,101):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
