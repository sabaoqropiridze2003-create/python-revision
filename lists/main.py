# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])



# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("banana")
# print(thislist)

# thislist1 = ["apple", "banana", "cherry"]
# thislist2 = ["mango", "cherry", "avocade"]
# thislist1.extend(thislist2)
# print(thislist1)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# # thislist.remove("apple")
# # thislist.pop(0)
# # thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[1]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits.sort(reverse=True)
# print(fruits)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]

# thislist.sort(key=myfunc)

# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key=str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# newlist = thislist.copy()
# print(newlist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# newlist = list(thislist)
# print(newlist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# newlist = thislist[:]
# print(newlist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

colors = ["red", "green", "blue"]
print(colors[0])
colors[1] = "yellow"
colors.append("purple")
colors.remove("red")
print(colors)