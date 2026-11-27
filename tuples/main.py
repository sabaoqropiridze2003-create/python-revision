# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)


### you can add tuples together

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

##removing items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# print(thistuple)

###deleting tuple

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits
# # green, yellow, *red = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(len(fruits))
a, b, c = fruits
print(b)